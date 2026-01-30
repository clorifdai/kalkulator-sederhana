def tambah(depan: float, belakang: float):
    """Operasi penambahan"""
    hasil = depan + belakang
    return hasil

def kurang(depan: float, belakang: float):
    """Pengurangan"""
    hasil = depan - belakang
    return hasil

def kali ():
    """Perkalian dengan input """
    list_angka = 1
# Perlu menambah alat pendeteksi int dan str. 
    while True:         
        angka = input("Ketik q untuk keluar.\nMasukkan angka: ")
        if angka == "q":
            print("Anda keluar dari kalkulator")
            break  
        elif angka.isdigit():
            print(angka, "sudah masuk")
            list_angka *= int(angka)
        else:
            print("***")
            print("Anda memasukkan bukan Angka")
            print("***")

    return list_angka

def bagi(depan: float, belakang:float):
    "Membagi secara sederhana"
    hasil = depan / belakang
    return hasil

# Membuat tebakan nomer random
def kuis_penjumlahan(level):
    import random
    "Level 1, Level 2, Level 3, level 4"
    l1_depan = random.randint(0, 9)
    l1_belakang = random.randint(0, 9)
    # l2 = random.randint(10, 99)
    # l3 = random.randint(100, 999)
    # l4 = random.randint(1000, 9999)
    while True:
        if level == "l1":
            print("Ketik huruf untuk keluar")
            print(l1_depan, "+", l1_belakang, "= ?")
            hasil = l1_depan + l1_belakang
            try:
                input_hasil = int(input("Masukkan angka: "))
            except ValueError:
                print("Anda keluar")
                break
            if input_hasil == hasil:
                return hasil
            elif input_hasil != hasil:
                return f"Hasil salah, yang benar {hasil}"
    return ""
        



if __name__ == "__main__":
    print(kuis_penjumlahan("l1"))
    # plus = tambah(12, 16.9)
    # print(plus)

    # kur = kurang(11, 100)
    # print(kur)
    # print(kali())
    # print(bagi(12, 9))
