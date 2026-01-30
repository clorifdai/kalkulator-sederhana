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

if __name__ == "__main__":
    # plus = tambah(12, 16.9)
    # print(plus)

    # kur = kurang(11, 100)
    # print(kur)
    # print(kali())
    print(bagi(12, 9))