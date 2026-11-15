"""Lõi sinh ngân hàng câu hỏi Toán tiểu học.

Mọi đáp án đều do code tính ra, không gõ tay, nên không có đáp án sai số.
Mỗi chủ đề (bài) có một danh sách "mẫu câu"; build() gọi các mẫu lần lượt
với số ngẫu nhiên (seed cố định) cho đến khi đủ 20 trắc nghiệm + 10 tự luận,
bỏ câu trùng đề.
"""
import random
from decimal import Decimal
from fractions import Fraction

TEN = ["Nam", "Lan", "Hoa", "Minh", "Mai", "An", "Bình", "Cúc", "Dũng", "Hà",
       "Khoa", "Linh", "Phúc", "Quang", "Thảo", "Tuấn", "Vy", "Hùng", "Huy",
       "Nga", "Sơn", "Trang", "Yến", "Đạt", "Giang", "Hải", "Khánh", "Lâm",
       "Oanh", "Phương"]
VAT = ["viên bi", "quyển vở", "cái kẹo", "bông hoa", "quả cam", "quả táo",
       "con tem", "tấm thẻ", "quả trứng", "cái bánh", "chiếc bút chì"]
CH = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
THU = ["Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy", "Chủ nhật"]


# ----------------------------------------------------------------- định dạng
def fmt(n, tach=True):
    """Số nguyên, tách nghìn bằng dấu chấm kiểu Việt Nam (12.345)."""
    n = int(n)
    if tach and abs(n) >= 1000:
        return f"{n:,}".replace(",", ".")
    return str(n)


def tp(x):
    """Số thập phân kiểu Việt Nam: dấu phẩy, bỏ số 0 thừa."""
    d = Decimal(x).normalize()
    s = format(d, "f")
    return s.replace(".", ",")


def ps(f):
    """Phân số a/b (đã là Fraction); số nguyên thì in số nguyên."""
    f = Fraction(f)
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"


def hs(f):
    """Hỗn số: 2 3/4."""
    f = Fraction(f)
    n, r = divmod(f.numerator, f.denominator)
    if r == 0:
        return str(n)
    if n == 0:
        return f"{r}/{f.denominator}"
    return f"{n} {r}/{f.denominator}"


def _doc3(n, dau):
    tram, chuc, dv = n // 100, n // 10 % 10, n % 10
    p = []
    if tram > 0 or not dau:
        p.append(CH[tram] + " trăm")
    if chuc == 0:
        if dv > 0:
            p.append(("linh " + CH[dv]) if (tram > 0 or not dau) else CH[dv])
    elif chuc == 1:
        p.append("mười" + (" lăm" if dv == 5 else (" " + CH[dv] if dv > 0 else "")))
    else:
        s = CH[chuc] + " mươi"
        if dv == 1:
            s += " mốt"
        elif dv == 5:
            s += " lăm"
        elif dv > 0:
            s += " " + CH[dv]
        p.append(s)
    return " ".join(p)


def doc_so(n):
    """Đọc số tự nhiên bằng chữ, đến hàng nghìn tỉ."""
    n = int(n)
    if n == 0:
        return "không"
    ten_lop = ["", "nghìn", "triệu", "tỉ", "nghìn tỉ"]
    nhom = []
    while n > 0:
        nhom.append(n % 1000)
        n //= 1000
    out = []
    dau = True
    for i in range(len(nhom) - 1, -1, -1):
        g = nhom[i]
        if g == 0:
            continue
        s = _doc3(g, dau)
        dau = False
        out.append((s + " " + ten_lop[i]).strip())
    return " ".join(out)


# ------------------------------------------------------------------ đáp án nhiễu
def so_gan(rng, d, lo=0, hi=None, buoc=(1, 2, 10)):
    """3 số nguyên gần d, khác d, khác nhau, trong [lo, hi]."""
    cand = []
    for mult in (1, 2, 3):
        for b in buoc:
            for dau in (-1, 1):
                x = d + dau * b * mult
                if x != d and x >= lo and (hi is None or x <= hi) and x not in cand:
                    cand.append(x)
    if len(cand) < 3:
        raise ValueError("thiếu số gần")
    gan = [x for x in cand if abs(x - d) <= max(buoc) * 2]
    pool = gan if len(gan) >= 3 else cand
    rng.shuffle(pool)
    return pool[:3]


def dec_gan(rng, d, lo=Decimal(0)):
    """Nhiễu cho số thập phân: dịch dấu phẩy, ±0,1, ±1."""
    d = Decimal(d)
    cand = [d * 10, d / 10, d + Decimal("0.1"), d - Decimal("0.1"), d + 1, d - 1,
            d + Decimal("0.01"), d - Decimal("0.01")]
    out = []
    for x in cand:
        if x >= lo and x != d and tp(x) not in [tp(y) for y in out] and tp(x) != tp(d):
            out.append(x)
    if len(out) < 3:
        raise ValueError("thiếu nhiễu thập phân")
    rng.shuffle(out)
    return out[:3]


def sai_dau(dung):
    """Đáp án nhiễu cho câu chọn dấu >, <."""
    return ["<" if dung == ">" else ">", "=", "Không so sánh được"]


# ------------------------------------------------------------------ dựng câu
def M(q, dung, sai, kho=1):
    return ("MC", q, str(dung), [str(s) for s in sai], kho)


def T(de, goiy, kho=1):
    return ("TL", de, goiy, kho)


def hai_ten(rng):
    return rng.sample(TEN, 2)


def vat(rng):
    return rng.choice(VAT)


def giai(loi, phep, kq, dv):
    return f"Bài giải\n{loi}\n{phep} = {kq} ({dv})\nĐáp số: {kq} {dv}."


def chon3(rng, ds, dung):
    """3 đáp án sai chọn từ ds (loại trùng đáp án đúng)."""
    ds = [x for x in dict.fromkeys(map(str, ds)) if x != str(dung)]
    if len(ds) < 3:
        raise ValueError("thiếu nhiễu")
    rng.shuffle(ds)
    return ds[:3]


# ------------------------------------------------------------------ dựng chủ đề
def build(lop, stt, ten_bai, mcs, tls, seed, n_mc=20, n_tl=10):
    rng = random.Random(seed)
    tn, seen = [], set()
    i = tries = 0
    while len(tn) < n_mc and tries < 6000:
        fn = mcs[i % len(mcs)]
        i += 1
        tries += 1
        try:
            it = fn(rng)
        except ValueError:
            continue
        _, q, dung, sai, kho = it
        if q in seen:
            continue
        opts = list(dict.fromkeys([dung] + sai))
        if len(opts) != 4:
            continue
        seen.add(q)
        rng.shuffle(opts)
        tn.append(dict(noi_dung=q, cac_dap_an=opts, dap_an_dung=opts.index(dung), do_kho=kho))
    if len(tn) < n_mc:
        raise RuntimeError(f"Lớp {lop} bài {stt} '{ten_bai}': chỉ sinh được {len(tn)}/{n_mc} trắc nghiệm")
    tl, seen = [], set()
    i = tries = 0
    while len(tl) < n_tl and tries < 6000:
        fn = tls[i % len(tls)]
        i += 1
        tries += 1
        try:
            it = fn(rng)
        except ValueError:
            continue
        _, de, goiy, kho = it
        if de in seen:
            continue
        seen.add(de)
        tl.append(dict(de=de, goi_y=goiy, do_kho=kho))
    if len(tl) < n_tl:
        raise RuntimeError(f"Lớp {lop} bài {stt} '{ten_bai}': chỉ sinh được {len(tl)}/{n_tl} tự luận")
    tn.sort(key=lambda x: x["do_kho"])
    tl.sort(key=lambda x: x["do_kho"])
    chu_de = f"Toán lớp {lop}"
    for k, x in enumerate(tn, 1):
        x.update(id=f"T{lop}-{stt:02d}-TN-{k:02d}", chu_de=chu_de, bai=ten_bai, mon="Toán", lop=lop)
    for k, x in enumerate(tl, 1):
        x.update(id=f"T{lop}-{stt:02d}-TL-{k:02d}", chu_de=chu_de, bai=ten_bai, mon="Toán", lop=lop)
    return tn, tl
