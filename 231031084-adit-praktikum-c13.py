# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nilai = int(input('Masukkan sebuah bilangan: '))

# Program Utama
hasil = fibonacci(nilai)
print('Fibonacci(%d)=%d' % (nilai, hasil))