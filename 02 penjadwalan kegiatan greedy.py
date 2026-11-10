# Topik 2 - Penjadwalan Kegiatan Optimal / Activity Selection (Greedy)
def pilih_kegiatan(kegiatan):
    urut = sorted(kegiatan, key=lambda k: k[2])   # urut waktu selesai
    terpilih = [urut[0]]
    waktu_akhir = urut[0][2]
    for k in urut[1:]:
        if k[1] >= waktu_akhir:                   # tidak bentrok
            terpilih.append(k)
            waktu_akhir = k[2]
    return terpilih

if __name__ == "__main__":
    data = [("A", 1, 4), ("B", 3, 5), ("C", 0, 6), ("D", 5, 7),
            ("E", 3, 9), ("F", 5, 9), ("G", 6, 10), ("H", 8, 11),
            ("I", 8, 12), ("J", 2, 14), ("K", 12, 16)]
    hasil = pilih_kegiatan(data)
    print("Jumlah kegiatan tersedia:", len(data))
    print("Kegiatan terpilih:")
    for nama, mulai, selesai in hasil:
        print(f"  {nama}: {mulai} - {selesai}")
    print("Total kegiatan terpilih :", len(hasil))