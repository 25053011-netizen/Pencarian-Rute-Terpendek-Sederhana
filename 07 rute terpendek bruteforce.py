# Topik 7 - Pencarian Rute Terpendek Sederhana (Brute Force)
from itertools import permutations

kota = ["A", "B", "C", "D", "E"]
jarak = [[0, 10, 15, 20, 25],
         [10, 0, 35, 25, 30],
         [15, 35, 0, 30, 20],
         [20, 25, 30, 0, 15],
         [25, 30, 20, 15, 0]]

def panjang_rute(rute):
    total = 0
    for k in range(len(rute) - 1):
        total += jarak[rute[k]][rute[k + 1]]
    return total

if __name__ == "__main__":
    terbaik, minimum, jumlah = None, float("inf"), 0
    for perm in permutations(range(1, len(kota))):   # A (0) sebagai awal
        rute = (0,) + perm + (0,)                    # kembali ke A
        d = panjang_rute(rute)
        jumlah += 1
        if d < minimum:
            terbaik, minimum = rute, d
    print("Jumlah rute dicoba:", jumlah)
    print("Rute terpendek    :", " -> ".join(kota[i] for i in terbaik))
    print("Jarak total       :", minimum)