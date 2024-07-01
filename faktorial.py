"""
FAKTORIAL

Deskripsi:
Diberikan sebuah bilangan bulat "N", tentukan nilai dari "N!" (faktorial dari "N"). Faktorial dari "N", dilambangkan sebagai "N!", didefinisikan sebagai hasil perkalian dari semua bilangan bulat positif dari 1 hingga "N".

Batasan :
0 <= N <= 20

Format Input :
- Satu baris berisi sebuah bilangan bulat "N".

Format Output :
- Satu baris berisi nilai dari "N!".

#-- Contoh 1 --#
Input :
5

Output :
120

Penjelasan :
5! = 5 x 4 x 3 x 2 x 1 = 120

#-- Contoh 2 --#
Input:
0

Output:
1

Penjelasan:
0! didefinisikan sebagai 1

#-- Contoh 3 --#
Input :
10

Output :
3628800

#-- Contoh 4  --#
Input :
20

Output :
2432902008176640000
"""

def faktorial(bilangan_n):
  hasil = 1

  for i in range(1, bilangan_n + 1):
    hasil *= i

  print(hasil)


bilangan_n = int(input(">> "))
faktorial(bilangan_n)

