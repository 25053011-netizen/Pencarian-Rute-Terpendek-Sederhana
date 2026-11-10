# Topik 1 - Pencarian Substring Terpanjang (Brute Force)
def substring_terpanjang(a, b):
    terbaik, dicek = "", 0
    for i in range(len(a)):                   # titik awal substring di a
        for j in range(i + 1, len(a) + 1):    # titik akhir substring di a
            sub = a[i:j]
            dicek += 1
            if sub in b and len(sub) > len(terbaik):
                terbaik = sub                 # simpan yang terpanjang
    return terbaik, dicek

if __name__ == "__main__":
    s1, s2 = "algoritma", "logaritma"
    hasil, dicek = substring_terpanjang(s1, s2)
    print("String 1             :", s1)
    print("String 2             :", s2)
    print("Substring terpanjang :", hasil)
    print("Panjang              :", len(hasil))
    print("Jumlah substring dicek:", dicek)