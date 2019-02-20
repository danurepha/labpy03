# **#labpy03**

## **(latihan1) Program Menampilkan N Bilangan Acak Yang Lebih Kecil Dari 0.5**
- ### Algoritma
1. import random memanggil file random.
2. n = int(input("Masukan nilai N : ")) input variabel n, tipe data integer.
3. for x in range(n) : looping for index x dengan jumlah perulangan sebanyak n.
4. b = random.uniform(.0,.5) variabel a berisikan random angka dari 0.0 sampai 0.5.
5. print ("Data ke : ",a,"==>",b) print data ke : a = index looping b = angka random sesuai syarat nomor 4.
6. print("Selesai") print Selesai di luar looping.
7. while jawab == 'yes' : looping for index yes untuk mengulang program kembali ke syarat nomor 2.
8. if jawab == 'yes' : kembali ke syarat nomor 2.
9. elif jawab == 'no' break : menghentikan program.
10. Tampilkan hasil kelayar.

- ### Syntax
```
def perulangan():
    print(' ')
    print('====== Bilangan Acak Yang Lebih Kecil Dari 0.5 ======')
    print(' ')
    import random
    n = int(input("Masukan nilai N : "))
    a = 0
    for x in range(n):
        a += 1
        b = random.uniform(.0,.5)
        print('Data ke:',a,'==>',b)
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
    print('Total perulangan : ' + str (hitung))
    
perulangan()
```

- ### Flowchart
![flowchart latihan1](https://user-images.githubusercontent.com/46738960/53030254-0cc11100-349d-11e9-9dd8-debc1c0af3f0.png)

- ### Screenshot
![screenshot program latihan1](https://user-images.githubusercontent.com/46738960/53069351-3f572200-350e-11e9-9254-ec90c1b166ba.png)


## **(latihan2) Program Menentukan Bilangan Terbesar**
- ### Algoritma
1. max=0 variable max diisi 0.
2. while True: looping while dengan syarat True.
3. if max < a: max = a proses if untuk mencari nilai terbesar.
4. a = int(input('Masukan bilangan = ')) input nilai a dengan tipe data integer.
5. if a==0 : break jika inputan a diisi angka 0 maka break alias berhenti looping.
6. print('Bilangan terbesarnya adalah = ',max) print nilai terbesar, variabel max.
7. Tampilkan hasil kelayar.

- ### Syntax
```
print('====== Menentukan Bilangan Terbesar ======')
max=0
while True:
	a=int(input('Masukkan bilangan = '))
	if max < a:
		max = a
	if a==0:
		break
print('Bilangan terbesarnya adalah = ',max)
```

- ### Flowchart
![flowchart latihan2](https://user-images.githubusercontent.com/46738960/53031646-d46f0200-349f-11e9-8a89-9c56ed21d935.png)

- ### Screenshot
![screenshot program latihan2](https://user-images.githubusercontent.com/46738960/53032449-72af9780-34a1-11e9-90f2-f4e91855f9aa.png)

## **(program1) Program Sederhana Pengulangan Dengan Menghitung Laba Pengusaha**
- ### Algoritma
1. a=100000000 modal 100.000.000, variable a.
2. sum=0 variable untuk menjumlah total laba.
3. b=0 variable untuk masa bulan.
4. lb = [int(0), int(0), int(a) * .1, int(a) * .1, int(a) * .5, int(a) * .5, int(a) * .5, int(a) * .2] variable untuk jumlah laba perbulan, dipisahkan dengan koma dan tipe data integer.
5. for c in lb : looping for index c dengan mengambil data dari lb.
6. sum=sum+c rumus untuk menghitung total laba perbulan.
7. b+=1 masa bulan, tiap looping menambah 1.
8. print('Laba bulan ke-',b,'sebesar :',c) print : b = ambil masa bulan, c = ambil dari data yg ada di dalam lb.
9. print('Total laba adalah :',sum) print total laba.
10. Tampilkan hasil kelayar.


- ### Syntax
```
print('====== Program Sederhana Pengulangan ======')
a=100000000
sum=0
b=0
lb = [int(0), int(0), int(a) * .1, int(a) * .1, int(a) * .5, int(a) * .5, int(a) * .5, int(a) * .2]
print('Investasi Modal Awal : ',a)
for c in lb :
    sum=sum+c
    b+=1
    print('Laba bulan ke-',b,'sebesar :',c)
print('Total laba adalah : ',sum)
```

- ### Flowchart
![flowchart program1](https://user-images.githubusercontent.com/46738960/53034202-49910600-34a5-11e9-9a29-769ccf230f92.png)

- ### Screenshot
![screenshot program program1](https://user-images.githubusercontent.com/46738960/53034279-6b8a8880-34a5-11e9-9128-c349595bc397.png)


# Sekian dan Terima Kasih
## Danu Braditya Repha
## 311810241
## TI.18.B.1