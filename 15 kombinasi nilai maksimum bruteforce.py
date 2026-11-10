# Topik 15 - Pemilihan Kombinasi Nilai Maksimum (Brute Force)
from itertools import combinations

def nilai_maksimum(angka, batas):
    terbaik, maks, dicek = (), 0, 0
    for r in range(len(angka) + 1):
        for kombo in combinations(angka, r):      # periksa semua subset
            dicek += 1
            total = sum(kombo)
            if total <= batas and total > maks:
                terbaik, maks = kombo, total
    return terbaik, maks, dicek

if __name__ == "__main__":
    angka = [8, 5, 12, 7, 3, 9]
    batas = 25
    kombo, maks, dicek = nilai_maksimum(angka, batas)
    print("Daftar angka:", angka)
    print("Batas       :", batas)
    print("Kombinasi terbaik:", list(kombo))
    print("Total terbesar   :", maks)
    print("Subset diperiksa :", dicek)