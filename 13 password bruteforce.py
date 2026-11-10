# Topik 13 - Pencarian Password Sederhana (Brute Force)
from itertools import product

def tebak_password(target, karakter, maks_panjang):
    percobaan = 0
    for panjang in range(1, maks_panjang + 1):
        for kombo in product(karakter, repeat=panjang):   # semua kombinasi
            percobaan += 1
            tebakan = "".join(kombo)
            if tebakan == target:
                return tebakan, percobaan
    return None, percobaan

if __name__ == "__main__":
    karakter = "abc123"
    target = "ab1"
    hasil, percobaan = tebak_password(target, karakter, 4)
    print("Kumpulan karakter:", karakter)
    print("Password target  :", target)
    print("Password ditemukan:", hasil)
    print("Jumlah percobaan  :", percobaan)
    print("Total kemungkinan panjang 1-4:", sum(len(karakter)**k for k in range(1, 5)))