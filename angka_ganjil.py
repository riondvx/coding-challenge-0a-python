"""
ANGKA GANJIL

Deksripsi :
Buat program yang menerima inputan bilangan bulat positif (N). Program harus menghasilkan deretan angka dari 1 sampai (N), dan mengganti semua angka ganjil dalam deretan tersebut dengan kata "ganjil".

Batasan :
- Nilai (N) harus merupakan bilangan bulat positif.

Format Input:
- Satu baris berisi angka (N). Dimana (N) merupakan bilangan bulat positif.

Format Output:
- Deretan angka dari 1 sampai (N). Semua angka ganjil diubah menjadi kata "ganjil".
- Tampilkan tulisan "Nilai maksimal yang diinputkan adalah 50" jika nilai (N) melebihi 50.

#-- Contoh 1 --#
Input :
5

Output :
ganjil 2 ganjil 4 ganjil 

#-- Contoh 2 --#
Input :
10

Output :
ganjil 2 ganjil 4 ganjil 6 ganjil 8 ganjil 10 

#-- Contoh 3 --#
Input :
7

Output :
ganjil 2 ganjil 4 ganjil 6 ganjil 

#-- Contoh 4 --#
Input :
51

Output :
Nilai maksimal yang diinputkan adalah 50
"""

def cari_angka_ganjil(bilangan_n):
  if bilangan_n > 50:
    print("Nilai maksimal yang diinputkan adalah 50")
    return

  for angka in range(1, bilangan_n + 1):
    if angka % 2 == 1:
      print("ganjil", end=" ")
    else:
      print(angka, end=" ")

  print("")


n = int(input(">> "))
cari_angka_ganjil(n)
