# Topik 8 - Penjadwalan Tugas Berdasarkan Deadline (Greedy)
def jadwal_tugas(tugas):
    urut = sorted(tugas, key=lambda t: t[2], reverse=True)   # untung terbesar
    maks = max(t[1] for t in tugas)
    slot = [None] * (maks + 1)                    # slot waktu 1..maks
    for nama, deadline, untung in urut:
        for s in range(deadline, 0, -1):          # cari slot kosong terakhir
            if slot[s] is None:
                slot[s] = (nama, untung)
                break
    return slot

if __name__ == "__main__":
    tugas = [("T1", 2, 100), ("T2", 1, 19), ("T3", 2, 27),
             ("T4", 1, 25), ("T5", 3, 15)]
    slot = jadwal_tugas(tugas)
    total = 0
    for s in range(1, len(slot)):
        if slot[s]:
            print(f"Slot {s}: {slot[s][0]} (untung {slot[s][1]})")
            total += slot[s][1]
    print("Total keuntungan:", total)