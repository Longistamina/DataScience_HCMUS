'''
Nhập điểm trung bình, nếu >= 5 thì báo đậu.
Nếu bé hơn thì báo rớt
'''

Ten = str(input("Vui lòng nhập họ và tên: "))
Diem = float(input('Vui lòng nhập điểm: '))

if Diem>=5:
    print(f'Chúc mừng {Ten} đã đậu!')
else:
    print(f'Xin chia buồn {Ten} không đậu.')

print()