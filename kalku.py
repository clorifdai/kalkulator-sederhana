def tambah(bilangan_a: float, bilangan_b: float):
    """Operasi penambahan"""
    hasil = bilangan_a + bilangan_b
    return hasil

def kurang (bilangan_a: float, bilangan_b: float):
    """Operasi pengurangan"""
    hasil = bilangan_a - bilangan_b
    return hasil

def kali (bilangan_a: float, bilangan_b: float):
    """Operasi perkalian"""
    hasil = bilangan_a * bilangan_b
    return hasil

def kali_input ():
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

def bagi(bilangan_a: float, bilangan_b: float):
    """Operasi pembagian"""
    hasil = bilangan_a / bilangan_b
    return hasil

if __name__ == "__main__":
    bagi(12, 2)
