print("==== Tugas Pertemuan 3 ====\n")

print("Nama \t: Imam Mulyana")
print("NIM \t: 20210801234 \n")

print("==== Operator Aritmatika ====\n")
a = 40
b = 20

hasil = a + b
hasil1 = a - b
hasil2 = a / b
hasil3 = a * b
print("Hasil dari", a, "+", b, "=", hasil)
print("Hasil dari", a, "-", b, "=", hasil1)
print("Hasil dari", a, "/", b, "=", hasil2)
print("Hasil dari", a, "*", b, "=", hasil3)

print("==== Matriks 2*2 ====\n")

matriks1 = [
    [2, 2],
    [4, 7],
]

matriks2 = [
    [2, 2],
    [4, 7],
]
for x in range(0, len(matriks1)):
    for y in range(0, len(matriks1[0])):
        print(matriks1[x][y] + matriks2[x][y], end=' ')
