def capucino():
    print("memilih capucino")
    a = int(input("masukkan harga : "))
    b = 10 / 100 * a
    c = a + b
    print("Jumlah yang harus di bayarkan ", c)


def teh():
    print("memilih teh")
    a = int(input("masukkan harga : "))
    b = 10 / 100 * a
    c = a + b
    print("Jumlah yang harus di bayarkan ", c)


def identitas():
    NIM = int(input("NIM : "))
    print(NIM)
    Nama = input("Nama : ")
    print(Nama)


def pilihan():

    print("1. capucino")
    print("2. teh")
    print("3. exit")


while True:
    identitas()
    pilihan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    else:
        break
