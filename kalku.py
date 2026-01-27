def tambah(depan: float, belakang: float):
    """Operasi penambahan"""
    hasil = depan + belakang
    return hasil

def kurang(depan: float, belakang: float):
    """Pengurangan"""
    hasil = depan - belakang
    return hasil

if __name__ == "__main__":
    plus = tambah(12, 16.9)
    print(plus)

    kur = kurang(11, 100)
    print(kur)