nama_karyawan = input('Masukkan nama :')
pendapatan = int(input('Masukkan besaran pendapatan:'))

print(f"""\nNama : {nama_karyawan}
pendapatan : {pendapatan} """)

if pendapatan >= 1000:
    print('Status berhak')
else:
    print('Status: Tidak Berhak')