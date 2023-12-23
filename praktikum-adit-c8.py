import os
import random as rd

warna = ['merah','putih','hitam']
com = rd.choice(warna)
a = True
while a:
    pilih = input('Masukkan Pilihan [merah,putih,hitam]: ')
    if pilih == com:
        print(f'Pilihan anda benar yaitu {pilih} \n')
        a = False
    else:
        print('Tebakan anda salah! coba lagi.')


#Tugas: Buat program tebak angka 1 sampai 10 dengan batas kesempatan 3 kali. berikan pesan 'kesempatan anda tersisa x kali'