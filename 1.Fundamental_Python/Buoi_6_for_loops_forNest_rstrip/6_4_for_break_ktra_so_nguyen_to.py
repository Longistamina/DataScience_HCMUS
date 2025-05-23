n = int(input('\nMời nhập số  N: '))
if n <= 1:
    ketLuan = f'{n} không phải số  nguyên tố.'
else:
    ketLuan = f'{n} là số  nguyên tố.'
    for i in range (2,n): #Đi từ 2 đến n-1
        if n%i == 0:
            ketLuan = f'{n} không phải số  nguyên tố.'
            break
print(ketLuan)
