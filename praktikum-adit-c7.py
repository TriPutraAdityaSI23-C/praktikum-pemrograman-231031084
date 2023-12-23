import os
os.system('clear')

pwd_benar = 'si23c'
a = True
i = 0
limit = 3

while a:
    i += 1
    pwd = input('Masukkan password: ')
    if pwd == pwd_benar:
        print('Selamat anda berhasil login!')
        a = False
    else:
        if i < limit:
            print('Passwor salah! coba lagi.')
            print(f'Kesempatan anda tersisa {limit-i} kali')
            a = True
        else:
            print('Kesempatan anda habis!')
            a = False