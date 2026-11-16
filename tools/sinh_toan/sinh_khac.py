import json, sys, importlib, os
sys.path.insert(0, os.path.dirname(__file__))
from core import build
from kbcore import chapter
from bosung import EXTRA
# mã môn -> (tên môn, tiền tố id)
MON = {"khtn": ("KHTN", "K"), "ta": ("Tiếng Anh", "A"), "ly": ("Vật lí", "L"), "hoa": ("Hóa học", "H"), "sinh": ("Sinh học", "S"),
       "su": ("Lịch sử", "U"), "dia": ("Địa lí", "D"), "gdcd": ("GDCD", "G"), "ktpl": ("Kinh tế & Pháp luật", "P"), "tin": ("Tin học", "I"),
       "van": ("Ngữ văn", "N"), "tn": ("Tự nhiên và Xã hội", "X"), "kh": ("Khoa học", "C"), "lsdl": ("Lịch sử và Địa lí", "Y"), "dd": ("Đạo đức", "O")}
def main(mods):
    tn_all, tl_all = [], []
    for name in mods:
        m = importlib.import_module(name)
        mon, pre = MON[m.MON]
        for lop, chs in m.DATA.items():
            for stt, c in enumerate(chs, 1):
                ten, text = c[0], c[1]; mode = c[2] if len(c) > 2 else "kn"
                text = text + EXTRA.get((m.MON, lop, stt), '')
                mcs, tls = chapter(text, mode)
                nm, nt = min(40, len(mcs)), min(15, len(tls))
                while True:
                    try:
                        tn, tl = build(lop, stt, ten, mcs, tls, seed=lop * 1000 + stt + sum(map(ord, m.MON)) * 7, mon=mon, pre=pre, khoa_dap_an=True, n_mc=nm, n_tl=nt)
                        break
                    except RuntimeError as e:
                        if "trắc nghiệm" in str(e) and nm > 6: nm -= 1
                        elif "tự luận" in str(e) and nt > 6: nt -= 1
                        else: raise
                if len(tn) < 30: print('CẢNH BÁO <30 TN:', mon, lop, ten, len(tn))
                tn_all += tn; tl_all += tl
    return tn_all, tl_all
if __name__ == "__main__":
    tn, tl = main(sys.argv[1].split(","))
    out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    def ghi(ten, khoa, ds):
        with open(f"{out}/{ten}", "w", encoding="utf-8") as f:
            f.write('{"' + khoa + '": [\n' + ",\n".join(json.dumps(x, ensure_ascii=False) for x in ds) + "\n]}\n")
    ghi("cau_hoi_mon_khac.json", "cau_hoi", tn); ghi("tu_luan_mon_khac.json", "tu_luan", tl)
    print(len(tn), "trắc nghiệm,", len(tl), "tự luận")
