#---------Bảng cửu chương------------#
while True:
    try:
        n = int(input('\nMời nhập số  cửu chương: '))
        assert n > 0
    except Exception:
        print('>>>Lỗi: số  cửu chương phải là số  nguyên dương.')
    else:    
        i = 1
        while i <= 10:
            print(f'{n} x {i} = {n*i}')
            i += 1
    kt = str(input('Nếu muốn tiếp tục, ấn [y], ngược lại ấn phím bất kỳ để thoát: ')).strip().lower()
    if kt == 'y': continue
    else: break
print('\n--Kết thúc--')

#--------------------Cách ghi kết quả khác-----------------------#
while True:
    try:
        n = int(input('\nMời nhập số  cửu chương: '))
        assert n > 0
    except Exception:
        print('>>>Lỗi: số  cửu chương phải là số  nguyên dương.')
    else:    
        i = 1
        bcc=''
        while i <= 10:
            bcc += f'{n} x {i} = {n*i}\n'
            i += 1
    print(bcc)
    kt = str(input('Nếu muốn tiếp tục, ấn [y], ngược lại ấn phím bất kỳ để thoát: ')).strip().lower()
    if kt == 'y': continue
    else: break
print('\n--Kết thúc--')