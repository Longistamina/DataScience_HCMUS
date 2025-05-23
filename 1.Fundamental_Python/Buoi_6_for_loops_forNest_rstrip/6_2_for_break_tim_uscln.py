'''
Nhập hai số  a và b rồi tìm ước số chung lớn nhất
'''
a = int(input('\nNhập số  a: '))
b = int(input('Nhập số  b: '))
gtMin = min(a,b)
uscln = 0
for i in range(gtMin,0,-1):
    if a%i==0 and b%i==0:
        uscln = i
        break #thoát ngang khỏi vòng lặp trước khi kết thúc
print(f'USCLN của {a} và {b} là: {uscln}')

#Cho i chạy từ min(a,b) về  1, nếu bắt gặp được số  nào thoả điều kiện thì ngừng luôn.
#Nếu cho chạy từ 1 lên min(a,b) thì phải thêm thuật toán để  chọn ra uscln