import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_bp"
)

cursor = db.cursor()
sql = """CREATE TABLE tb_hobi (
  no_id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(50),
  hobi Varchar(50)
)
"""
cursor.execute(sql)

print("Tabel berhasil dibuat")