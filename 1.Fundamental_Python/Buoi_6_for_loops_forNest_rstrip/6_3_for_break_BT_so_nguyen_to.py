'''
Nhập số  nguyên K >= 10, print ra các số  nguyên tố  nhỏ hơn K
'''
k = int(input('\nNhập số  nguyên K: '))
print(f'Các số nguyên tố nhỏ hơn {k} là:',end = ' ')
kq =''
for i in range (2,k):
    for j in range (2,i):
        if i%j == 0: break
    else: kq +=str(i)+' '
print(kq)

