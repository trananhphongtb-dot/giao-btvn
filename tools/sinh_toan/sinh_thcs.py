"""Sinh ngân hàng Toán lớp 6–12 (KNTT). Dùng: python3 sinh_thcs.py 6,7 <outdir>"""
import json, sys, importlib, os
sys.path.insert(0, os.path.dirname(__file__))
from core import build

def main(lops):
    tn_all, tl_all = [], []
    for lop in lops:
        m = importlib.import_module(f"lop{lop}")
        for stt, (ten, mcs, tls) in enumerate(m.CHU_DE, 1):
            tn, tl = build(lop, stt, ten, mcs, tls, seed=lop * 1000 + stt, n_mc=30, n_tl=12)
            tn_all += tn; tl_all += tl
    return tn_all, tl_all

if __name__ == "__main__":
    lops = [int(x) for x in sys.argv[1].split(",")]
    tn, tl = main(lops)
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    def ghi(ten, khoa, ds):
        with open(f"{out}/{ten}", "w", encoding="utf-8") as f:
            f.write('{"' + khoa + '": [\n' + ",\n".join(json.dumps(x, ensure_ascii=False) for x in ds) + "\n]}\n")
    ghi("cau_hoi_toan_thcs_thpt.json", "cau_hoi", tn)
    ghi("tu_luan_toan_thcs_thpt.json", "tu_luan", tl)
    print(len(tn), "trắc nghiệm,", len(tl), "tự luận")
