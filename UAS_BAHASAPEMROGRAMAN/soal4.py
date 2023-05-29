import mysql.connector

test_koneksi = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "",
)
if test_koneksi.is_connected():
    print("Berhasil terhubung")