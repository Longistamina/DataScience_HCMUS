import math
print('\nGIẢI PHƯƠNG TRÌNH BẬC 2')
print('-'*80)

#--------------------bắt lỗi A ----------------#
try:
    a = float(input('Nhập hệ số  A: '))
    assert a != 0
except ValueError:
    k = True
    while k == True:
        try:
            a = float(input('>>>LỖI: Hệ số  A phải là số, yêu cầu nhập lại: '))
            assert a != 0
        except ValueError:
            k = True
        except AssertionError:
            l = True
            while l == True:
                try:
                    a = float(input('>>>LỖI: Hệ số  A phải khác 0, yêu cầu nhập lại: '))            
                    assert a != 0
                except AssertionError:
                    l = True
                except ValueError:
                    l = False
                    k = True
                else:
                    l = False
                    k = False
        else:
            k = False
print()
#--------------------bắt lỗi B ----------------#

try:
    b = float(input('Nhập hệ số  B: '))
except ValueError:
    k = True
    while k == True:
        try:
                b = float(input('>>>LỖI: Hệ số  B phải là một số, yêu cầu nhập lại: '))
        except ValueError:
            k = True
        else: 
            k = False
print()

#--------------------bắt lỗi B ----------------#

try:
    c = float(input('Nhập hệ số  C: '))
except ValueError:
    k = True
    while k == True:
        try:
                c = float(input('>>>LỖI: Hệ số  C phải là một số, yêu cầu nhập lại: '))
        except ValueError:
            k = True
        else: 
            k = False
print()

#-----------------Xử lý tính toán--------------#
if b > 0 and c > 0:
    pt = f'{a}x{chr(178)} + {b}x + {c} = 0'
elif b < 0 and c > 0:
    pt = f'{a}x{chr(178)} - {-1*b}x + {c} = 0'
elif c < 0 and b > 0:
    pt = f'{a}x{chr(178)} + {b}x - {-1*c} = 0'
else:
    pt = f'{a}x{chr(178)} - {-1*b}x - {-1*c} = 0'

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    kq = f'Vì Delta > 0 nên phương trình {pt} có hai nghiệm là {round(x1,2)} và {round(x2,2)}'
elif delta == 0:
    x = (-b)/(2*a)
    kq = f'Vì Delta = 0 nên phương trình {pt} có nghiệm kép là {round(x,2)}'
else:
    kq = f'Vì Delta < 0 nên phương trình {pt} vô nghiệm'

#---------------------Kết quả----------------------#
print(f'Biệt thức delta = {delta} \n')
print(kq)
print()