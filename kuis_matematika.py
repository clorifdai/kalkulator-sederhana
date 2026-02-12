import random

# Kuis_matematika.py berisi kode untuk membuat kuis matematika sederhana dari penjumlahan, perngurangan, perkalian dan pembagian


# Kuis penjumlahan
from datetime import datetime

waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M")
waktu_tanggal_sekarang = datetime.now().strftime("%Y-%m-%d_%H%M%S")


def kuis_penjumlahan():
    """
    Membuat kuis penjumlahan secara otomatis
    1 = 1 digit. 0 - 9
    2 = 2 digit. 10 - 99
    3 = 3 digit. 100 - 999
    4 = 4 digit. 1000 - 9999
    """
    list_hasil = []
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
            list_hasil.append(f"{bilangan_a} + {bilangan_b} = {hasil} BENAR")
        elif input_hasil != hasil:
            print(f"Hasil salah! Yang benar {hasil}")
            list_hasil.append(f"{bilangan_a} + {bilangan_b} = {input_hasil} SALAH")
    # Print daftar soal yang berhasil dijawab
    # print(list_hasil)
    return list_hasil

# Kuis pengurangan

def kuis_pengurangan():
    """
    Membuat kuis pengurangan secara otomatis
    1 = 1 digit. 0 - 9
    2 = 2 digit. 10 - 99
    3 = 3 digit. 100 - 999
    4 = 4 digit. 1000 - 9999
    """
    list_hasil = []
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
            list_hasil.append(f"{bilangan_a} - {bilangan_b} = {hasil} BENAR")
        elif input_hasil != hasil:
            print(f"Hasil salah! Yang benar {hasil}")
            list_hasil.append(f"{bilangan_a} - {bilangan_b} = {input_hasil} SALAH")
    # Print daftar soal yang berhasil dijawab
    # print(list_hasil)
    return list_hasil
# Kuis perkalian

def kuis_perkalian():
    """
    Membuat kuis perkalian secara otomatis
    1 = 1 digit. 0 - 9
    2 = 2 digit. 10 - 99
    3 = 3 digit. 100 - 999
    4 = 4 digit. 1000 - 9999
    """
    list_hasil = []
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
        print(bilangan_a, "x", bilangan_b, "= ?")
        hasil = bilangan_a * bilangan_b
        try:
            input_hasil = int(input("Masukkan angka: "))
        except ValueError:
            print("Anda Keluar")
            break
            
        if input_hasil == hasil:
            print("Jawaban anda benar")
            print(hasil)
            list_hasil.append(f"{bilangan_a} x {bilangan_b} = {hasil} BENAR")
        elif input_hasil != hasil:
            print(f"Hasil salah! Yang benar {hasil}")
            list_hasil.append(f"{bilangan_a} x {bilangan_b} = {input_hasil} SALAH")
    # Print daftar soal yang berhasil dijawab
    # print(list_hasil)
    return list_hasil

# def tampilkan_hasil():
#     print(list_hasil)

def simpan_hasil(a):
    "Menggunakan hasil return fungsi kuis lain lalu disimpan ke file txt"
    nama_file_jawaban =  f"jawaban_ {waktu_tanggal_sekarang}.txt"
    
    with open(nama_file_jawaban, "w") as file_jawaban:
        file_jawaban.write(f"{waktu_sekarang}\n")
    
    for i in a:
        with open(nama_file_jawaban, "a") as file_jawaban:
            file_jawaban.write(f"{i}\n")

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
    list_hasil = []
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
            list_hasil.append(f"{bilangan_a} : {bilangan_b} = {hasil_2digit} BENAR")
        elif input_hasil != hasil_2digit:
            print(f"Hasil salah! Yang benar {hasil_2digit}")
            list_hasil.append(f"{bilangan_a} : {bilangan_b} = {input_hasil} SALAH")
    # Print daftar soal yang berhasil dijawab
    # print(list_hasil)
    return list_hasil

# Menyimpan jawaban
def simpan_hasil(daftar_jawaban: list):  # noqa: F811
    "Menggunakan hasil return fungsi kuis lain lalu disimpan ke file txt"
    nama_file_jawaban =  f"jawaban_ {waktu_tanggal_sekarang}.txt"
    
    with open(nama_file_jawaban, "w") as file_jawaban:
        file_jawaban.write(f"{waktu_sekarang}\n")
    
    for jawaban in daftar_jawaban:
        with open(nama_file_jawaban, "a") as file_jawaban:
            file_jawaban.write(f"{jawaban}\n")

#######

if __name__ == "__main__":
    x = kuis_pembagian()
    simpan_hasil(x)

