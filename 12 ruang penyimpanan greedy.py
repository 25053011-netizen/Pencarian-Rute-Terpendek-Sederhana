# Topik 12 - Pengelolaan Ruang Penyimpanan (Greedy)
def pilih_file(files, kapasitas):
    # prioritas tertinggi dulu; jika sama, ukuran terkecil dulu
    urut = sorted(files, key=lambda f: (-f[2], f[1]))
    dipilih, terpakai = [], 0
    for nama, ukuran, prioritas in urut:
        if terpakai + ukuran <= kapasitas:
            dipilih.append((nama, ukuran, prioritas))
            terpakai += ukuran
    return dipilih, terpakai

if __name__ == "__main__":
    files = [("skripsi.docx", 50, 10), ("video.mp4", 300, 4),
             ("foto.zip", 120, 6), ("data.xlsx", 40, 9),
             ("musik.mp3", 80, 3), ("tugas.pdf", 30, 8)]
    kapasitas = 250
    dipilih, terpakai = pilih_file(files, kapasitas)
    print("Kapasitas:", kapasitas, "MB")
    for nama, ukuran, p in dipilih:
        print(f"  {nama:<14}{ukuran:>4} MB  prioritas {p}")
    print("Terpakai:", terpakai, "MB | Sisa:", kapasitas - terpakai, "MB")