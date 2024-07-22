"""
SUM & AVERAGE

Deskripsi :
Diberikan kumpulan bilangan bulat dalam bentuk array:

Array A1 = [ 7, 10, 5, 3, 5, 12, 1, 9, 18, 12 ]

Tulislah sebuah program yang dapat menghitung total (SUM) dan rata-rata (AVERAGE) dari nilai-nilai dalam array tersebut. Total adalah hasil penjumlahan semua nilai, sementara rata-rata adalah nilai rata-rata dari keseluruhan elemen array, dihitung dengan membagi total dengan jumlah elemen.

Contoh Array :
*-- Array 1 --*
A1 = [7, 10, 5, 3, 5, 12, 1, 9, 18, 12]

*- Output -*
Total: 82
Rata-rata: 8.2

*-- Array 2 --*
A2 = [4, 8, 15, 16, 23, 42]

*- Output -*
Total: 108
Rata-rata: 18.0

*-- Array 3 --*
A3 = [3, 20, 9, 12, 6, 18, 21, 24]

*- Output -*
Total: 113
Rata-rata: 14.125
"""

def calculate_sum_and_average(arr):
  total = sum(arr)
  avg = total / len(arr)
  return total, avg


arr = [7, 10, 5, 3, 5, 12, 1, 9, 18, 12]
total, avg = calculate_sum_and_average(arr)
print(f"Array: {arr}")
print(f"Total: {total}")
print(f"Rata-rata: {avg}")
