# Topik 9 - Pencarian Kombinasi Uang (Brute Force)
from itertools import product

def kombinasi_uang(nominal, pecahan):
    batas = [range(nominal // p + 1) for p in pecahan]   # jumlah tiap pecahan
    hasil = []
    for jumlah in product(*batas):                       # coba semua kombinasi
        if sum(j * p for j, p in zip(jumlah, pecahan)) == nominal:
            hasil.append(jumlah)
    return hasil

if __name__ == "__main__":
    pecahan = [5000, 2000, 1000]
    nominal = 10000
    hasil = kombinasi_uang(nominal, pecahan)
    print(f"Nominal: Rp {nominal}, pecahan: {pecahan}")
    for n, k in enumerate(hasil, 1):
        teks = " + ".join(f"{j}x{p}" for j, p in zip(k, pecahan) if j)
        print(f"{n:>2}. {teks}   ({sum(k)} lembar)")
    print("Jumlah kombinasi:", len(hasil))
    print("Paling sedikit lembar:", min(sum(k) for k in hasil))