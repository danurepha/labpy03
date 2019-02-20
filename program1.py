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
print('\nDanu Braditya Repha')
print('311810241')
print('TI.18.B.1')