def tambah(depan: float, belakang: float):
    """Operasi penambahan"""
    hasil = depan + belakang
    return hasil


if __name__ == "__main__":
    plus = tambah(12, 16.9)
    print(plus)