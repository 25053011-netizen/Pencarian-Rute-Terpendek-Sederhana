# Topik 6 - Knapsack Sederhana berdasarkan Rasio Nilai/Berat (Greedy)
def knapsack_greedy(items, kapasitas):
    # urut berdasarkan rasio nilai/berat terbesar
    urut = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    total, dipilih = 0.0, []
    for nama, berat, nilai in urut:
        if kapasitas <= 0:
            break
        ambil = min(berat, kapasitas)             # ambil penuh / sebagian
        total += nilai * ambil / berat
        dipilih.append((nama, ambil, berat, nilai / berat))
        kapasitas -= ambil
    return dipilih, total

if __name__ == "__main__":
    items = [("A", 10, 60), ("B", 20, 100), ("C", 30, 120)]
    dipilih, total = knapsack_greedy(items, 50)
    for nama, ambil, berat, rasio in dipilih:
        print(f"Item {nama}: ambil {ambil} dari {berat} kg (rasio {rasio:.1f})")
    print("Total nilai:", total)