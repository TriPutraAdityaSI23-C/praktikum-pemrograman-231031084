import os
os.system('clear')

a = True
limit = 5
i = 0


while a:
    i += 1
    print(f'Menjankan Program {limit + 1 - i} ')
    if i == limit:
        a = False
        print('Program berhenti di sini')
    else:
        a =True