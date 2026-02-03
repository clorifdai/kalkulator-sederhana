import random

def kuis_penjumlahan():
    """
    Membuat kuis penjumlahan secara otomatis
    1 = 1 digit
    2 = 2 digit
    3 = 3 digit
    4 = 4 digit
    """
    
    level = input("Ketik 1-4 untuk menentukan jumlah digit. \nMasukkan jumlah digit: ")

    while True:
        if level == "1":
            bilangan_a = random.randint(0, 9)
            bilangan_b = random.randint(0, 9)
        elif level == "2":
            bilangan_a = random.randint(10, 99)
            bilangan_b = random.randint(10, 99)
        elif level == "3":
            bilangan_a = random.randint(100, 999)
            bilangan_b = random.randint(100, 999)
        elif level == "4":
            bilangan_a = random.randint(1000, 9999)
            bilangan_b = random.randint(1000, 9999)    
        else:
            print("Masukan anda salah!")
            return "Hanya masukkan angka 1-4"
            
        print("\nKetik huruf untuk keluar")
        print(bilangan_a, "+", bilangan_b, "= ?")
        hasil = bilangan_a + bilangan_b
        try:
            input_hasil = int(input("Masukkan angka: "))
        except ValueError:
            print("Anda Keluar")
            break
            
        if input_hasil == hasil:
            print("Jawaban anda benar")
            print(hasil)
        elif input_hasil != hasil:
            print(f"Hasil salah! Yang benar {hasil}")

    return ""
        
###########

if __name__ == "__main__":
    print(kuis_penjumlahan())
    # help(kuis_penjumlahan)