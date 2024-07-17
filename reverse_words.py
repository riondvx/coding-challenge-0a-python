"""
REVERSE WORDS

Deskripsi :
Bantu Bibi membuat program yang menerima tiga kata sebagai masukan dan kemudian menampilkan kembali kata-kata tersebut dalam urutan terbalik.

Format Input :
Input terdiri dari satu baris yang mengandung tepat tiga kata yang dipisahkan oleh spasi.

Format Output :
Output juga terdiri dari satu baris yang mengandung tepat tiga kata yang dipisahkan oleh spasi. Print enter di akhir output.

Batasan :
1 ≤ jumlah karakter dalam setiap kata ≤ 20
Setiap kata hanya mengandung huruf kecil dari ‘a’ hingga ‘z’.

Contoh Input/Output
----------
Contoh 1
Input :
langit berwarna biru

Output :
biru berwarna langit

----------
Contoh 2
Input :
merah putih biru

Output :
biru putih merah

----------
Contoh 3
Input :
algoritma dan logika

Output :
logika dan algoritma

----------
Contoh 4
Input :
satu dua tiga

Output :
tiga dua satu

"""

teks = input("-> ")
daftar_kata = teks.split(" ")
daftar_kata_dibalik = daftar_kata[::-1]
teks_dibalik = " ".join(daftar_kata_dibalik)
print(teks_dibalik)

# Cara singkat dalam satu baris
# print(" ".join(input("-> ").split(" ")[::-1]))
