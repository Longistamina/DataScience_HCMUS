n = int(input('\nMời nhập số  N: '))
if n <= 1:
    ketLuan = f'{n} không phải số  nguyên tố.'
else:
    for i in range (2,n): #Đi từ 2 đến n-1
        if n%i == 0:
            ketLuan = f'{n} không phải số  nguyên tố.'
            break
    else: #của for
        ketLuan = f'{n} là số  nguyên tố.'
print(ketLuan)

#else của for sẽ được thực thi khi vòng lặp for kết thúc một cách tự nhiên. 
#Nếu dùng break để  thoát for thì else của for sẽ không được thực thi