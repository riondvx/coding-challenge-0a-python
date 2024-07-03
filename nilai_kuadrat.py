"""
NILAI KUADRAT

Deskripsi :
Diberikan sebuah nilai (X) berupa bilangan bulat postif. Buatkan sebuah program yang dapat menampilkan nilai kuadrat bilangan dari 1 sampai X.

Contoh Input :
Input Bilangan (X) : 5

Contoh Output :
X         X^2
====================
1         1
2         4
3         9
4         16
5         25

"""

bilangan_x = int(input("Input Bilangan (X) : "))

print("X         X^2")
print("====================")

for n in range(1, bilangan_x + 1):
  n_kuadrat = n * n
  print(f"{n:<10}{n_kuadrat}")
