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

    while True: 
        try:
                angka = int(input("Ketik -0 untuk keluar.\nMasukkan angka: "))
                if angka == -0:
                    print("Anda keluar dari kalkulator")
                    break
                print("Angka masuk", angka)
                list_angka *= angka
        except ValueError:
            print("Masukkan angka bukan huruf maupun simbol!!")
    return list_angka            

if __name__ == "__main__":
    # plus = tambah(12, 16.9)
    # print(plus)

    # kur = kurang(11, 100)
    # print(kur)
    print(kali())