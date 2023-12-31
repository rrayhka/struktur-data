# -*- coding: utf-8 -*-
"""220411100158_Modul 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UuvORXiGcytmDlGZnPVQ1c9ulkZBf3qW
"""

# fungsi dibawah ini untuk membuat sparse matrix sekaligus untuk menjawab nomor ke-1 pada modul praktiikum

def createMatrix():
    global matrice1
    global matrice2
    matrice1 = []
    matrice2 = []
    for matriks in range(2):
        matrix = []
        print()
        print(f"matrik -{matriks + 1}")
        jumlah_baris = int(input("jumlah baris = "))
        jumlah_kolom = int(input("jumlah kolom = "))
        jumlah_data = int(input("jumlah data = "))

        for row in range(jumlah_baris):
            row = []
            for col in range(jumlah_kolom):
                row.append(0)
            matrix.append(row)

        for data in range(jumlah_data):
            baris_ke = int(input("baris ke = "))
            kolom_ke = int(input("kolom ke = "))
            input_user = int(input(f"matrik {[baris_ke, kolom_ke]} = "))

            for change in range(jumlah_data):
                for baris in matrix:
                    for kolom in baris:
                        matrix[baris_ke][kolom_ke] = input_user

        if matriks == 0:
            matrice1 = matrix
        else:
            matrice2 = matrix
createMatrix()

# fungsi dibawah ini untuk menampilkan list dalam bentuk matriks yang sudah dibuat pada fungsi sebelumnya

def displayMatrices(matrice):
    for i in range(len(matrice)):
        result = ''
        for j in range(len(matrice[i])):
            result = result+str(matrice[i][j])+' '
        print('|', result,'|')
    print()

# kode dibawah ini untuk memanggil fungsi displayMatrice()
# kode ini untuk menjawab soal nomor ke-2 pada modul praktikum

print("Matriks 1 =")
displayMatrices(matrice1)

print("Matriks 2 = ")
displayMatrices(matrice2)

# kode dibawah ini untuk mengalikan kedua matrix

def matrixMultiplication(matrice1, matrice2):
    rows = len(matrice1)
    columns = len(matrice2[0])
    matrice = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            temp = 0
            for k in range(len(matrice2)):
                temp = temp + matrice1[i][k] * matrice2[k][j]
                matrice[i][j] = temp
    return matrice
matrixMultiplication(matrice1, matrice2)

# kode dibawah ini untuk menampilkan hasil perkalian matrix
# kode dibawah ini untuk menjawab pertanyaan pada soal ke-3 pada modul praktikum

print("Matriks 1 =")
displayMatrices(matrice1)

print("Matriks 2 = ")
displayMatrices(matrice2)

print("Hasil =")
displayMatrices(matrixMultiplication(matrice1, matrice2))