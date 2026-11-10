# Topik 11 - Pencarian Jadwal Kegiatan (Brute Force)
from itertools import combinations

def bentrok(a, b):
    return a[1] < b[2] and b[1] < a[2]            # waktu saling tumpang tindih

def jadwal_terbanyak(kegiatan):
    terbaik, dicek = [], 0
    for r in range(1, len(kegiatan) + 1):
        for kombo in combinations(kegiatan, r):   # semua himpunan kegiatan
            dicek += 1
            aman = all(not bentrok(x, y) for x, y in combinations(kombo, 2))
            if aman and len(kombo) > len(terbaik):
                terbaik = list(kombo)
    return terbaik, dicek

if __name__ == "__main__":
    data = [("A", 1, 4), ("B", 3, 5), ("C", 0, 6), ("D", 5, 7),
            ("E", 3, 9), ("F", 5, 9), ("G", 6, 10), ("H", 8, 11)]
    hasil, dicek = jadwal_terbanyak(data)
    print("Kombinasi dicek:", dicek)
    for nama, mulai, selesai in hasil:
        print(f"  {nama}: {mulai} - {selesai}")
    print("Jumlah kegiatan terbanyak:", len(hasil))