# Topik 14 - Pemilihan Rute Terdekat / Nearest Neighbor (Greedy)
kota = ["A", "B", "C", "D", "E"]
jarak = [[0, 10, 15, 20, 25],
         [10, 0, 35, 25, 30],
         [15, 35, 0, 30, 20],
         [20, 25, 30, 0, 15],
         [25, 30, 20, 15, 0]]

def rute_terdekat(awal=0):
    rute, total = [awal], 0
    belum = set(range(len(kota))) - {awal}
    sekarang = awal
    while belum:
        tujuan = min(belum, key=lambda k: jarak[sekarang][k])  # terdekat
        total += jarak[sekarang][tujuan]
        rute.append(tujuan)
        belum.remove(tujuan)
        sekarang = tujuan
    total += jarak[sekarang][awal]                # kembali ke kota awal
    rute.append(awal)
    return rute, total

if __name__ == "__main__":
    rute, total = rute_terdekat(0)
    print("Rute  :", " -> ".join(kota[i] for i in rute))
    print("Jarak total:", total)