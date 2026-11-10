# Topik 3 - Pencarian Kombinasi Item Terbaik (Brute Force)
from itertools import combinations

def kombinasi_terbaik(items, kapasitas):
    terbaik, nilai_max, dicek = (), 0, 0
    for r in range(len(items) + 1):
        for kombo in combinations(items, r):      # semua kombinasi
            dicek += 1
            berat = sum(i[1] for i in kombo)
            nilai = sum(i[2] for i in kombo)
            if berat <= kapasitas and nilai > nilai_max:
                terbaik, nilai_max = kombo, nilai
    return terbaik, nilai_max, dicek

if __name__ == "__main__":
    items = [("A", 2, 12), ("B", 1, 10), ("C", 3, 20), ("D", 2, 15)]
    kapasitas = 5
    kombo, nilai, dicek = kombinasi_terbaik(items, kapasitas)
    print("Kapasitas:", kapasitas)
    print("Item terbaik:", [i[0] for i in kombo])
    print("Total berat :", sum(i[1] for i in kombo))
    print("Total nilai :", nilai)
    print("Kombinasi dicek:", dicek)