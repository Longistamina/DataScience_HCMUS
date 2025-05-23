'''
Cho người dùng nhập các số  vào list rồi tính tổng các số
'''
print()
print('Chương trình nhập và tính tổng các số '.center(80))
print('-'*80)

giaTriNhap = input('Mời bạn nhập một dãy số , các số ngăn cách nhau bởi dấu phẩy: ')
lstN = giaTriNhap.split(',')

tong = None
sum = 0

for i in range(len(lstN)):
    lstN[i] = lstN[i].strip()
    while True:
        try:
            lstN[i] = float(lstN[i])
        except ValueError:
                try:
                    lstN[i] = float(input(f'>>>Lỗi: dữ liệu thứ {i+1} không hợp lệ, mời nhập lại ở dạng số, nếu muốn loại bỏ dữ liệu này hãy ấn bất kỳ phím nào không phải số: '))
                except ValueError: break
        else: 
            sum += lstN[i]
            break

print('\nDãy bạn đã nhập là:',lstN)

for item in lstN:
    try: float(item)
    except ValueError: continue
    else: tong = sum

if tong == None:
     print('Không tính được tổng')
else:
     print('Tổng các số có trong dãy =',tong)




