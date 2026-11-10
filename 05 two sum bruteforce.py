# Topik 5 - Pencarian Pasangan Angka / Two Sum (Brute Force)
def two_sum(angka, target):
    pasangan = []
    for i in range(len(angka)):
        for j in range(i + 1, len(angka)):        # setiap pasangan (i, j)
            if angka[i] + angka[j] == target:
                pasangan.append((i, j))
    return pasangan

if __name__ == "__main__":
    angka = [2, 7, 11, 15, 3, 6]
    target = 9
    hasil = two_sum(angka, target)
    print("Daftar angka:", angka)
    print("Target      :", target)
    for i, j in hasil:
        print(f"Ditemukan: {angka[i]} + {angka[j]} = {target}  (indeks {i} dan {j})")
    if not hasil:
        print("Tidak ada pasangan yang cocok")