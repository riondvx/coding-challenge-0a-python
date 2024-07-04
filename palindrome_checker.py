"""
PALINDROME CHECKER

Deskripsi :
Diberikan sebuah string `s`, tulis sebuah fungsi untuk memeriksa apakah string tersebut adalah palindrome. String yang disebut palindrome jika string tersebut dapat dibaca sama dari kiri ke kanan maupun kanan ke kiri setelah mengabaikan spasi, tanda baca, simbol, dan mengabaikan perbedaan antara huruf kecil dan besar.

Format Input :
- Satu baris input berupa string `s`.

Format Output :
- Cetak "palindrome" jika string tersebut adalah palindrome dan jika bukan palindrome maka cetak "bukan palindrome".

Contoh Test Case :
#-- Contoh 1 -- #
input : Kasur ini rusak
output : palindrome

#-- Contoh 2 -- #
input : Saya suka makan nasi
output : bukan palindrome

#-- Contoh 3 -- #
input : katak
output : palindrome

#-- Contoh 4 -- #
input : 2021-12-02
output : palindrome

#-- Contoh 5 -- #
input : 08123456789
output : bukan palindrome

"""

def cek_palindrome(text_str):
  text_str = text_str.lower()  # lowercase
  text_alnum = ""

  for char in text_str:
    if char.isalnum():
      text_alnum += char

  if text_alnum == text_alnum[::-1]:
    print("palindrome")
  else:
    print("bukan palindrome")


text_str = input(">> ")
cek_palindrome(text_str)
