"""
HURUF VOKAL

Deskripsi :
Buatlah sebuah fungsi yang menerima sebuah string dan mencari huruf vokal di dalam string tersebut. Huruf vokal yang dianggap adalah 'a', 'i', 'u', 'e', 'o' dalam huruf kecil maupun besar.

Batasan :
- Panjang string 1 <= |S| <= 10^5
- String dapat berisi huruf kecil, huruf besar, spasi, dan karakter non-huruf.

Format Input :
- Satu baris berisi string (S).

Format Output :
- Baris pertama berisi huruf vokal yang ditemukan dalam string.
- Baris kedua berisi jumlah huruf vokal didalam string.

Contoh Input dan Output :
#-- Contoh 1 --#
Input :
Halo Dunia

Output :
aouia
5

#-- Contoh 2 --#
Input :
Ini adalah contoh string

Output :
Iiaaaooi
8


#-- Contoh 3 --#
Input :
Komputer

Output :
oue
3

#-- Contoh 4 --#
Input :
Python dan JavaScript

Output :
oaaai
5
"""

def cari_huruf_vokal(teks):
  vokal = "aiueoAIUEO"
  vokal_ditemukan = ""

  for huruf in teks:
    if huruf in vokal:
      vokal_ditemukan += huruf

  print(vokal_ditemukan)
  print(len(vokal_ditemukan))


teks = input(">> ")
cari_huruf_vokal(teks)
