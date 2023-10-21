# -*- coding: utf-8 -*-
"""220411100158_Modul5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TKLVUbaVzNavvPa9ULnV4u_zFIijdIjG

#Nomor 1
a. Mengurutkan data secara Ascending dimulai dari index terakhir

b. Mengurutkan data secara Descending dimulai dari index awal
"""

def InsertionSortAscending(data):
    for indeks in range(len(data) - 1, -1, -1):
        nilai_sekarang = data[indeks]
        posisi = indeks
        print(f"Iterasi ke - {indeks}")
        while posisi < len(data) - 1 and data[posisi + 1] < nilai_sekarang:
            data[posisi] = data[posisi + 1]
            posisi += 1
        data[posisi] = nilai_sekarang
        print(data)
    return f"Data Urut = {data}"

import random
data = [random.randint(0, 100) for i in range(0, 5)]
print(f"Data Awal = {data}\n")
InsertionSortAscending(data)

def InsertionSortDescending(data):
    for indeks in range(0, len(data)):
        nilai_sekarang = data[indeks]
        posisi = indeks
        print(f"Iterasi ke - {indeks}")
        while posisi > 0 and data[posisi - 1] < nilai_sekarang:
            data[posisi] = data[posisi - 1]
            posisi -= 1
        data[posisi] = nilai_sekarang
        print(data)
    return f"Data Urut = {data}"

import random
data = [random.randint(0, 100) for i in range(0, 5)]
print(f"Data Awal = {data}\n")
InsertionSortDescending(data)

"""# Nomor 2
Memodifikasi tower of hanoi
"""

def tower(n, asal, tujuan, temp):
    if n > 0:
        tower(n-1, asal, temp, tujuan)

        print(f"Lempengan {n} dari {asal} ke {tujuan}")
        move(asal, tujuan)
        print_tower()

        tower(n-1, temp, tujuan, asal)
def move(asal, tujuan):
    item = towers[asal].pop()
    towers[tujuan].append(item)
def print_tower():
    print(asal, ": ", end="")
    [print(f"|{i}|", end="") for i in towers[asal]]
    print(f"\n{temp}", ": ", end="")
    [print(f"|{i}|", end="") for i in towers[temp]]
    print(f"\n{tujuan}", ": ", end="")
    [print(f"|{i}|", end="") for i in towers[tujuan]]
    print("")

n = 4
asal = "A"
tujuan = "C"
temp = "B"
towers = {
    asal: [i for i in range(n, 0, -1)],
    tujuan: [],
    temp: []
}
print("Pemindahan 4 lempengan dari A ke C dengan menggunakan bantuan B")
print_tower()
tower(n, asal, tujuan, temp)

def fungsi(n, asal, tujuan, bantuan):
  if n > 0:
    fungsi(n-1, asal, bantuan, tujuan)
    print(f"lempengan {n} dari {asal} ke {tujuan}")
    fungsi(n-1, bantuan, tujuan, asal)

fungsi(2, 'a', 'c', 'b')