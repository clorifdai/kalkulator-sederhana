import random

# Kuis_matematika.py berisi kode untuk membuat kuis matematika sederhana dari penjumlahan, perngurangan, perkalian dan pembagian


# Kuis penjumlahan
def kuis_penjumlahan():
    """
    Membuat kuis penjumlahan secara otomatis
    1 = 1 digit. 0 - 9
    2 = 2 digit. 10 - 99
    3 = 3 digit. 100 - 999
    4 = 4 digit. 1000 - 9999
    """
    
    level = input("Ketik 1-4 untuk menentukan jumlah digit. Ketik 'help' untuk bantuan. \nMasukkan jumlah digit: ")
    if level == "help":
        help(kuis_penjumlahan)
        pass

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

    return None

# Kuis pengurangan

def kuis_pengurangan():
    """
    Membuat kuis pengurangan secara otomatis
    1 = 1 digit. 0 - 9
    2 = 2 digit. 10 - 99
    3 = 3 digit. 100 - 999
    4 = 4 digit. 1000 - 9999
    """
    
    level = input("Ketik 1-4 untuk menentukan jumlah digit. Ketik 'help' untuk bantuan. \nMasukkan jumlah digit: ")
    if level == "help":
        help(kuis_pengurangan)
        pass

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
        print(bilangan_a, "-", bilangan_b, "= ?")
        hasil = bilangan_a - bilangan_b
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

    return None

# Kuis perkalian

def kuis_perkalian():
    """
    Membuat kuis perkalian secara otomatis
    1 = 1 digit. 0 - 9
    2 = 2 digit. 10 - 99
    3 = 3 digit. 100 - 999
    4 = 4 digit. 1000 - 9999
    """
    
    level = input("Ketik 1-4 untuk menentukan jumlah digit. Ketik 'help' untuk bantuan. \nMasukkan jumlah digit: ")
    if level == "help":
        help(kuis_perkalian)
        pass

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
        print(bilangan_a, "X", bilangan_b, "= ?")
        hasil = bilangan_a * bilangan_b
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

    return None

# Kuis pembagian

def kuis_pembagian():
    """
    Membuat kuis pembagian secara otomatis. 
    Hasil maksimal pembagian  2 angka dibelakang nol
    1 = 1 digit. 0 - 9
    2 = 2 digit. 10 - 99
    3 = 3 digit. 100 - 999
    4 = 4 digit. 1000 - 9999
    """
    
    level = input("Ketik 1-4 untuk menentukan jumlah digit. Ketik 'help' untuk bantuan. \nMasukkan jumlah digit: ")
    if level == "help":
        help(kuis_pembagian)
        pass

    while True:
        if level == "1":
            bilangan_a = random.randint(1, 9)
            bilangan_b = random.randint(1, 9)
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
        print(bilangan_a, ":", bilangan_b, "= ?")
        hasil = bilangan_a / bilangan_b
        hasil_2digit = round(hasil, 2)
        try:
            input_hasil = float(input("Masukkan angka: "))
        except ValueError:
            print("Anda Keluar")
            break
            
        if input_hasil == hasil_2digit:
            print("Jawaban anda benar")
            print(hasil_2digit)
        elif input_hasil != hasil_2digit:
            print(f"Hasil salah! Yang benar {hasil_2digit}")

    return None

###########

if __name__ == "__main__":
    # print(kuis_penjumlahan())
    print(kuis_pembagian())
    # help(kuis_penjumlahan)