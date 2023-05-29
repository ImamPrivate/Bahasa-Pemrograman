# 20210801234 Imam Mulyana
import array as arr
print("Deklarasi array dengan library\n")

angka = arr.array('i', [1, 2, 3])

print("Mengakses array")
for i in range(0, 3):
    print(angka[i])

print("menambahkan array ")
angka.insert(2, 4)
for i in range(0, 3):
    print(angka[i])

print("menghapus data di aray ")
angka.remove(2)
for i in range(0, 3):
    print(angka[i])
print("\n=========================================\n")

print("Deklarasi array menggunakan list\n")
no_id = [1, 5, 3, 6]

print("Mengakses array")
print(no_id)

print("Mengakses array berdasarkan index")
index_arr = no_id[2]
print(index_arr, "\n")

print("Mengakses array menggunakan for")
for i in no_id:
    print(i)

print("Menghitung panjang array")
panjang_array2 = len(no_id)
print(panjang_array2)

print("menambahkan data array")
tambah = no_id.append(11)
print(no_id)

print("menambahkan data array berdasarkan index")
index = no_id.insert(1, 12)
print(no_id)

print("mengurutkan data array")
urut = no_id.sort()
print(no_id)

print("menghapus array")
hapus = no_id.remove(5)
print(no_id)
