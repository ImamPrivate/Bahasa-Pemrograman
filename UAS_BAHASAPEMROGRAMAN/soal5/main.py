import mysql.connector
import os


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_bp"
)


def insert_data(db):
  nama = input("Masukan nama: ")
  hobi = input("Masukan hobi: ")
  val = (nama, hobi)
  cursor = db.cursor()
  sql = "INSERT INTO tb_hobi (nama, hobi) VALUES (%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} Data tersimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM tb_hobi"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Data tidak ditemukan")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  no_id = input("pilih id orang> ")
  nama = input("Nama baru: ")
  hobi = input("Hobi baru: ")

  sql = "UPDATE tb_hobi SET nama=%s, hobi=%s WHERE no_id=%s"
  val = (nama, hobi, no_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data telah diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  no_id = input("pilih id orang> ")
  sql = "DELETE FROM tb_hobi WHERE no_id=%s"
  val = (no_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def show_menu(db):
  print("=== Database Hobi Orang ===")
  print("1. Insert")
  print("2. Show")
  print("3. Update")
  print("4. Delete")
  print("0. Exit")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)