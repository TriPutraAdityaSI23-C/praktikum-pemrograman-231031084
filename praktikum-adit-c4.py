import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','8','4']
print()

print(nim)

print()
print('item index o (pertama)',nim[0])
print('item index 1 (kedua)',nim[1])

print()
print(f'item index o (pertama) {nim[0]}')
print(f'item index 1 (kedua) {nim[1]}')
print(f'item index terakhir {nim[len(nim)-1]}')
print(f'item index terakhir {nim[-1]}')
print(f'item index (pertama) {nim[-len(nim)]}')

print()
data = ['Tri Putra Aditya',2023,'Aktif']
nilai= [90,89,93,97]

print()
print('Nama     : '+ data[0])
print('Angkatan :', data[1])
print('Status   : '+ data[2])

print()
print(f'{data[0]} status kuliah : {data[2]}')
print(f'Data terbesar nilai adalah     : {max(nilai)}' )
print(f'Data terkecil nilai adalah     : {min(nilai)}' )
x = sum(nilai) / len(nilai)
print(f'Rata-rata nilai adalah         :',x)

# >> Von Neumann status Kuliah: Aktif
print(f'{data[0]} status kuliah : {data[2]}')
print()
# >> Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah     : {max(nilai)}' )
print()
# >> Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah     : {min(nilai)}' )
print()
# >> Rata-rata nilai adalah: 92.25
x = sum(nilai) / len(nilai)
print(f'Rata-rata nilai adalah         :',x)

print()
data = [('Tri Putra Aditya',2023,'Aktif'),

(90,89,93,97),
(20,22),
('S1-Reguler','Ganjil')]

print(data[0][0])
print(data[-1][0])
print(data[2][0:])

print()
# Nama Mahasiswa : Tri Putra Aditya
print(f'Nama Mahasisiwa : {data[0][0]}')
# Inisial Tri Putra Aditya : T P A
print(f'Inisial Tri Putra Aditya : {data[0][0][0]} {data[0][0][4]} {data[0][0][10]}')
# NIM Tri Putra Aditya : 231031084

# Program Tri Putra Aditya : S1-Reguler Sistem Informasi C
print(f'Program Tri Putra Aditya : {data[-1][0]}')
# Angkatan Tri Putra Aditya : Ganjil-2023
print(f'Angkatan Tri Putra Aditya : {data[-1][1]}-{data[0][1]}')
# Total sks Tri Putra Aditya adalah : 11
# Jumlah nilai Tri Putra Aditya : 5
# Nilai tertinggi Tri Putra Aditya : 99
# Nilai terendah Tri Putra Aditya : 76
# Rata-rata nilai Tri Putra Aditya : 92.25


# >> Tugas: Nama Mahasiswa Thomas dengan NIM: 600201014
# >> Program pendidikan Thomas: S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[-1][0]}')
# >> Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]}-{data[-1][1]}')
# >> Jumlah nilai Thomas adalah: 4
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
# >> Data terbesar Thomas adalah: 97
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
# >> Data terkecil Thomas adalah: 89
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
# >> Rata-rata nilai Thomas adalah: 92.25
x_bar = sum(data[1])/len(data[1])
print(f'Rata-rata nilai {data[0][0]} adalah: {x_bar}')

