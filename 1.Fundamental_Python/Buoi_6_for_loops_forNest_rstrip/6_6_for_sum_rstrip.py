'''
Nhập số  nguyên N >= 10, tính tổng từ 1 đến N
'''

while True:
    try:
        n = int(input('\nNhập số  nguyên n: '))
        assert n >= 10
    except Exception:
        print('>>>Lỗi, N phải là số  nguyên dương lớn hơn hoặc bằng 10.')
    else:
        s = 0
        daySo = ''
        for i in range (1,n+1,1):
            s += i
            daySo += f'{i} + '
        #print(f'Tổng từ 1 đến {n} là: {s}')
        daySo = daySo.rstrip(' + ')
        print(f'Tổng {daySo} = {s}')
    ttuc = input('Nếu muốn tiếp tục, nhấn [y], còn không ấn phím bất kỳ để thoát: ').strip().lower()
    if ttuc == 'y': continue
    else: break
print('\n--Kết thúc--')