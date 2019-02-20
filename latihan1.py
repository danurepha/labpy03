def perulangan():
    print(' ')
    print('====== Bilangan Acak Yang Lebih Kecil Dari 0.5 ======')
    print(' ')
    import random
    n = int(input("Masukan nilai N : "))
    a = 0
    for x in range(n):
        a += 1
        b = random.uniform(.0, .5)
        print('Data ke:', a, '==>', b)
    print('Selesai')
    print('')
    jawab = 'yes'
    hitung = 0
    while jawab == 'yes':
        hitung += 1
        jawab = input('Ingin Mengulang Program Ini? (yes/no) : ')
        if jawab == 'yes':
            return perulangan()
        elif jawab == 'no':
            break
    print('Total perulangan : ' + str(hitung))

perulangan()