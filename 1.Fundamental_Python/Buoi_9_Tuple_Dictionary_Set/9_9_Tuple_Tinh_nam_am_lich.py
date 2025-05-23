'''
Mời người dùng nhập năm dương lịch, trả về  năm âm lịch
'''
print()
print('TÍNH NĂM ÂM LỊCH'.center(60))
print('-'*60)

tupCan = 'Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ'
tupChi = 'Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi'

while True:
    try:
        namDL = int(input('Mời bạn nhập năm dương lịch: '))
    except ValueError:
        print('>>>Lỗi: năm dương lịch phải là số nguyên dương từ 1 đến 9999.')
    else:
        can = namDL%10 #Lấy năm dương lịch chia cho 10 lấy phần dư, rồi dùng làm index để trích xuất can
        chi = namDL%12 #Lấy năm dương lịch chia cho 12 lấy phần dư, rồi dùng làm index để trích xuất chi
        print(f'Năm âm lịch tương ứng là {tupCan[can]} {tupChi[chi]}')
    
    ttuc = input('Nếu muốn tiếp tục nhập [y], ngược lại ấn bất kỳ để  thoát: ')
    if ttuc == 'y':
        print() 
        continue
    else: break
print('\n--Kết thúc--')
