# Topik 10 - Pemilihan Barang Berdasarkan Prioritas (Greedy)
def pilih_barang(barang, kapasitas):
    urut = sorted(barang, key=lambda b: b[2], reverse=True)  # prioritas tinggi
    dipilih, terpakai = [], 0
    for nama, berat, prioritas in urut:
        if terpakai + berat <= kapasitas:         # muat -> ambil
            dipilih.append((nama, berat, prioritas))
            terpakai += berat
    return dipilih, terpakai

if __name__ == "__main__":
    barang = [("Obat", 2, 10), ("Air minum", 4, 9), ("Makanan", 5, 8),
              ("Senter", 1, 7), ("Pakaian", 6, 5), ("Buku", 3, 3)]
    kapasitas = 12
    dipilih, terpakai = pilih_barang(barang, kapasitas)
    print("Kapasitas:", kapasitas, "kg")
    for nama, berat, p in dipilih:
        print(f"  {nama:<10} berat {berat} kg, prioritas {p}")
    print("Total berat terpakai:", terpakai, "kg")