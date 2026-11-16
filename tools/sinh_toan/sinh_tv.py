import json, sys, importlib, os
sys.path.insert(0, os.path.dirname(__file__))
from core import build
from kbcore import chapter
from tv_bosung import EXTRA

def main(lops):
    tn_all, tl_all = [], []
    for lop in lops:
        m = importlib.import_module(f"tv{lop}")
        for stt, cd in enumerate(m.CHU_DE, 1):
            ten, mcs, tls = cd[:3]
            opt = cd[3] if len(cd) > 3 else {}
            if (lop, stt) in EXTRA:
                m2, t2 = chapter(EXTRA[(lop, stt)]); mcs = list(mcs) + m2
            opt = {**opt}; nm = opt.pop("n_mc", 30); nt = opt.pop("n_tl", 12)
            while True:
                try:
                    tn, tl = build(lop, stt, ten, mcs, tls, seed=lop * 1000 + stt + 500, mon="Tiếng Việt", pre="V", khoa_dap_an=True, n_mc=nm, n_tl=nt, **opt); break
                except RuntimeError as e:
                    if "trắc nghiệm" in str(e) and nm > 10: nm -= 1
                    elif "tự luận" in str(e) and nt > 6: nt -= 1
                    else: raise
            if nm < 30: print("CẢNH BÁO TV", lop, stt, ten, nm, nt)
            tn_all += tn; tl_all += tl
    return tn_all, tl_all

if __name__ == "__main__":
    lops = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [1, 2, 3, 4, 5]
    tn, tl = main(lops)
    out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/tv"
    os.makedirs(out, exist_ok=True)
    def ghi(ten, khoa, ds):
        with open(f"{out}/{ten}", "w", encoding="utf-8") as f:
            f.write('{"' + khoa + '": [\n' + ",\n".join(json.dumps(x, ensure_ascii=False) for x in ds) + "\n]}\n")
    ghi("cau_hoi_tieng_viet.json", "cau_hoi", tn)
    ghi("tu_luan_tieng_viet.json", "tu_luan", tl)
    print(len(tn), "trắc nghiệm,", len(tl), "tự luận")
