"""Bộ máy sinh câu hỏi Tiếng Việt từ kho dữ liệu soạn tay.

Khác Toán (đáp án tính bằng code), Tiếng Việt lấy đáp án từ kho từ ngữ đã
được soạn và rà tay trong lop*_tv.py. Bộ máy chỉ ghép kho thành câu hỏi, chọn
đáp án nhiễu từ các nhóm KHÁC nên đáp án đúng luôn khớp kho.
"""
import random
from core import M, T


def _tron(rng, dung, ds, n=3):
    s = [x for x in dict.fromkeys(ds) if x != dung]
    if len(s) < n:
        raise ValueError
    return rng.sample(s, n)


def _chon_mau(rng, mau):
    return rng.choice(mau) if isinstance(mau, (list, tuple)) else mau


# ============================================================= TRẮC NGHIỆM
def mc_nhom(nhom, hoi, kho=1):
    """nhom {tên: [từ]}, hoi {tên: 'chỉ con vật'} -> Từ nào dưới đây chỉ con vật?"""
    ks = list(nhom)
    def f(rng):
        k = rng.choice(ks)
        w = rng.choice(nhom[k])
        khac = [x for kk in ks if kk != k for x in nhom[kk] if x not in nhom[k]]
        return M(f"Từ nào dưới đây {hoi[k]}?", w, _tron(rng, w, khac), kho)
    return f


def mc_nhan(nhom, nhan, kho=1):
    """Cho từ, chọn nhãn nhóm. nhan {tên: 'chỉ con vật'}; cần >= 4 nhãn."""
    ks = list(nhom)
    def f(rng):
        k = rng.choice(ks)
        w = rng.choice(nhom[k])
        if any(w in nhom[kk] for kk in nhom if kk != k):
            raise ValueError
        sai = [nhan[kk] for kk in nhan if kk != k]
        return M(f"Từ \"{w}\" là từ:", nhan[k], _tron(rng, nhan[k], sai), kho)
    return f


def mc_cap(cap, mau, hai_chieu=True, kho=1):
    """cap [(a, b)]; mau 'Từ trái nghĩa với \"{}\" là:'. Nhiễu lấy từ các cặp khác,
    loại mọi từ đã là bạn của a để không có hai đáp án đúng."""
    ban = {}
    for a, b in cap:
        ban.setdefault(a, set()).add(b)
        if hai_chieu:
            ban.setdefault(b, set()).add(a)
    ds = list(ban)
    def f(rng):
        a = rng.choice(ds)
        b = rng.choice(sorted(ban[a]))
        khac = [x for x in ds if x != a and x not in ban[a]]
        return M(_chon_mau(rng, mau).replace("{}", a), b, _tron(rng, b, khac), kho)
    return f


def mc_dungsai(items, hoi="Từ nào viết đúng chính tả?", kho=1):
    """items [(đúng, [sai...])]; nhiễu = các dạng sai của chính từ đó, bù bằng dạng sai của từ khác."""
    tatca_sai = [s for _, ss in items for s in ss]
    def f(rng):
        d, ss = rng.choice(items)
        nhieu = list(ss)
        rng.shuffle(nhieu)
        nhieu = nhieu[:3]
        if len(nhieu) < 3:
            them = [x for x in tatca_sai if x not in ss and x != d]
            rng.shuffle(them)
            nhieu += them[: 3 - len(nhieu)]
        return M(_chon_mau(rng, hoi), d, nhieu, kho)
    return f


def mc_dien_am(items, hoi="Chọn âm, vần thích hợp điền vào chỗ trống:", kho=1):
    """items [(khung có dấu _, đáp án, [3 nhiễu])]; nhiễu soạn tay để chỉ đáp án đúng tạo từ có nghĩa."""
    def f(rng):
        kh, d, sai = rng.choice(items)
        return M(f"{_chon_mau(rng, hoi)} {kh}", d, list(sai), kho)
    return f


# ---- biến thể chính tả tự động (cặp/nhóm phụ âm đầu dễ lẫn) -------------------------
_HOI = dict(zip("ảẳẩẻểỉỏổởủửỷ", "ãẵẫẽễĩõỗỡũữỹ"))
_NGA = {v: k for k, v in _HOI.items()}


def _dau(syl, nhom):
    for p in sorted(nhom, key=len, reverse=True):
        if syl.startswith(p):
            if p == "n" and syl[1:2] in ("g", "h"):
                continue
            if p == "g" and syl[1:2] == "i":
                continue
            return p
    return None


def bien_the(cum, nhom):
    """Các cách viết SAI của cụm từ khi lẫn phụ âm đầu trong nhom (vd ('ch','tr'))."""
    from itertools import product
    tu = cum.split()
    idx = [(i, _dau(t, nhom)) for i, t in enumerate(tu)]
    idx = [(i, p) for i, p in idx if p]
    out = []
    for chon in product(*[nhom for _ in idx]):
        t2 = list(tu)
        for (i, p), q in zip(idx, chon):
            t2[i] = q + tu[i][len(p):]
        s = " ".join(t2)
        if s != cum and s not in out:
            out.append(s)
    return out


def doi_thanh(cum):
    """Đổi hỏi<->ngã ở các tiếng có dấu hỏi/ngã (mọi tổ hợp), trả các cách viết sai."""
    from itertools import product
    tu = cum.split()
    dsd = {i: "".join(_HOI.get(c, _NGA.get(c, c)) for c in t) for i, t in enumerate(tu)}
    idx = [i for i in dsd if dsd[i] != tu[i]]
    out = []
    for chon in product([0, 1], repeat=len(idx)):
        if not any(chon):
            continue
        t2 = list(tu)
        for i, c in zip(idx, chon):
            if c:
                t2[i] = dsd[i]
        out.append(" ".join(t2))
    return out


def khung(cum, nhom):
    """Khung điền: thay phụ âm đầu trong nhom bằng '_', trả (khung, 'ch, tr')."""
    tu = cum.split()
    dap = []
    for i, t in enumerate(tu):
        p = _dau(t, nhom)
        if p:
            tu[i] = "_" + t[len(p):]
            dap.append(p)
    return " ".join(tu), dap


def mc_cs_nhom(cums, nhom, hoi="Cách viết nào đúng chính tả?", kho=1):
    """Chính tả lẫn phụ âm đầu: cums danh sách cụm từ ĐÚNG; nhiễu sinh tự động."""
    cums = [c for c in cums if len(bien_the(c, nhom)) >= 3]
    def f(rng):
        c = rng.choice(cums)
        return M(_chon_mau(rng, hoi), c, rng.sample(bien_the(c, nhom), 3), kho)
    return f


def mc_cs_thanh(cums, hoi="Cách viết nào đúng chính tả?", kho=2):
    cums = [c for c in cums if len(doi_thanh(c)) >= 3]
    def f(rng):
        c = rng.choice(cums)
        return M(_chon_mau(rng, hoi), c, rng.sample(doi_thanh(c), 3), kho)
    return f


def tl_cs_thanh(cums, de="Viết lại cho đúng chính tả:", n=4, kho=2):
    cums = [c for c in cums if doi_thanh(c)]
    def f(rng):
        ch = rng.sample(cums, n)
        sai = [rng.choice(doi_thanh(c)) for c in ch]
        return T(f"{de}\n" + ", ".join(sai), "; ".join(f"{s} → {c}" for s, c in zip(sai, ch)), kho)
    return f


def mc_cs_dien(cums, nhom, tapchon, hoi="Điền cùng một chữ vào các chỗ trống:", kho=1):
    """Điền phụ âm đầu: lấy cụm mà mọi chỗ trống cùng một đáp án (vd 'chăm chỉ' -> ch)."""
    its = []
    for c in cums:
        kh, dap = khung(c, nhom)
        if dap and len(set(dap)) == 1 and dap[0] in tapchon:
            its.append((kh, dap[0]))
    def f(rng):
        kh, d = rng.choice(its)
        return M(f"{_chon_mau(rng, hoi)} {kh}", d, [x for x in tapchon if x != d][:3], kho)
    return f


def tl_cs_dien(cums, nhom, de="Điền vào chỗ trống:", n=4, kho=2):
    def f(rng):
        ch = rng.sample(cums, n)
        ks = [khung(c, nhom) for c in ch]
        if any(not d for _, d in ks):
            raise ValueError
        return T(f"{de}\n" + "; ".join(k for k, _ in ks), "; ".join(c for c in ch), kho)
    return f


def tl_cs_sua(cums, nhom, de="Viết lại cho đúng chính tả:", n=4, kho=2):
    cums = [c for c in cums if bien_the(c, nhom)]
    def f(rng):
        ch = rng.sample(cums, n)
        sai = [rng.choice(bien_the(c, nhom)) for c in ch]
        return T(f"{de}\n" + ", ".join(sai), "; ".join(f"{s} → {c}" for s, c in zip(sai, ch)), kho)
    return f


def mc_cau_chon(items, nhan, hoi, kho=1):
    """items [(câu, nhãn)]. Chọn câu có nhãn `nhan`; nhiễu là câu nhãn khác."""
    dung = [c for c, l in items if l == nhan]
    sai = [c for c, l in items if l != nhan]
    def f(rng):
        d = rng.choice(dung)
        return M(hoi, d, _tron(rng, d, sai), kho)
    return f


def mc_cau_nhan(items, lua_chon, hoi="Câu \"{c}\" thuộc kiểu nào?", kho=2):
    """items [(câu, nhãn)]; cho câu, chọn nhãn trong lua_chon (>=4)."""
    def f(rng):
        c, l = rng.choice(items)
        return M(_chon_mau(rng, hoi).replace("{c}", c), l, _tron(rng, l, lua_chon), kho)
    return f


def mc_dien_tu(items, hoi="Chọn từ thích hợp điền vào chỗ trống:", kho=2):
    """items [(câu có ___, đúng, [nhiễu tùy chọn])]; thiếu nhiễu thì lấy đáp án đúng của câu khác."""
    tatca = [it[1] for it in items]
    def f(rng):
        it = rng.choice(items)
        c, d = it[0], it[1]
        sai = list(it[2]) if len(it) > 2 else []
        if len(sai) < 3:
            sai += [x for x in tatca if x != d and x not in sai]
        return M(f"{_chon_mau(rng, hoi)} {c}", d, _tron(rng, d, sai), kho)
    return f


def mc_nghia(items, hoi="\"{x}\" có nghĩa là gì?", kho=2, nhom=None):
    """items [(x, nghĩa)]; nhiễu là nghĩa của mục khác; nhom {x: tên nhóm} loại các nghĩa gần giống cùng nhóm."""
    def f(rng):
        x, n = rng.choice(items)
        khac = [m for y, m in items if y != x and (nhom is None or nhom.get(y) != nhom.get(x))]
        return M(_chon_mau(rng, hoi).replace("{x}", x), n, _tron(rng, n, khac), kho)
    return f


def mc_ngc(items, hoi, kho=2):
    """Nghĩa -> từ: items [(x, nghĩa)]; hoi 'Từ nào có nghĩa: {n}?'"""
    ds = [x for x, _ in items]
    def f(rng):
        x, n = rng.choice(items)
        return M(_chon_mau(rng, hoi).replace("{n}", n), x, _tron(rng, x, ds), kho)
    return f


def mc_ktra(items, kho=2):
    """Câu hỏi soạn tay: items [(câu hỏi, đúng, [nhiễu 3])]."""
    def f(rng):
        q, d, s = rng.choice(items)
        return M(q, d, list(s), kho)
    return f


# ================================================================= TỰ LUẬN
def tl_nhom(nhom, hoi, de="Xếp các từ sau vào nhóm thích hợp:", n=2, m=3, kho=2):
    """Chọn n nhóm, mỗi nhóm m từ; trộn rồi yêu cầu xếp. hoi {tên: 'Từ chỉ con vật'}."""
    ks = list(nhom)
    def f(rng):
        ch = rng.sample(ks, n)
        ws = []
        goi = []
        for k in ch:
            w = rng.sample(nhom[k], m)
            ws += w
            goi.append(f"{hoi[k]}: {', '.join(w)}")
        rng.shuffle(ws)
        return T(f"{de}\n{', '.join(ws)}", "\n".join(goi), kho)
    return f


def tl_cap(cap, mau, n=3, kho=2):
    """Tìm từ ... của các từ: a, b, c (gợi ý: a - b ...)."""
    def f(rng):
        ch = rng.sample(cap, n)
        return T(f"{_chon_mau(rng, mau)} {', '.join(a for a, _ in ch)}", "; ".join(f"{a} - {b}" for a, b in ch), kho)
    return f


def tl_dungsai(items, de="Các từ sau viết sai chính tả, hãy viết lại cho đúng:", n=4, kho=2):
    def f(rng):
        ch = rng.sample(items, n)
        return T(f"{de}\n{', '.join(ss[0] for _, ss in ch)}", "; ".join(f"{ss[0]} → {d}" for d, ss in ch), kho)
    return f


def tl_dien_am(items, de="Điền vào chỗ trống:", n=5, kho=2):
    def f(rng):
        ch = rng.sample(items, n)
        return T(f"{de}\n{'; '.join(k for k, _ in ch)}", "; ".join(k.replace("_", d) for k, d in ch), kho)
    return f


def tl_cau_nhan(items, de, n=3, kho=2):
    """items [(câu, nhãn)] -> Xác định ...: liệt kê câu, gợi ý nhãn."""
    def f(rng):
        ch = rng.sample(items, n)
        return T(f"{de}\n" + "\n".join(f"{i + 1}. {c}" for i, (c, _) in enumerate(ch)), "\n".join(f"{i + 1}. {l}" for i, (_, l) in enumerate(ch)), kho)
    return f


def tl_dien_tu(items, de="Điền từ thích hợp vào chỗ trống:", n=3, kho=2):
    def f(rng):
        ch = rng.sample(items, n)
        return T(f"{de}\n" + "\n".join(f"{i + 1}. {it[0]}" for i, it in enumerate(ch)), "\n".join(f"{i + 1}. {it[1]}" for i, it in enumerate(ch)), kho)
    return f


def tl_cur(items, kho=2):
    """Đề soạn tay: items [(đề, gợi ý)] hoặc [(đề, gợi ý, độ khó)]."""
    def f(rng):
        it = rng.choice(items)
        return T(it[0], it[1], it[2] if len(it) > 2 else kho)
    return f
