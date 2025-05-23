'''
Giải phương trình bậc 1: ax+b=0
'''
print()
print("GIẢI PHƯƠNG TRÌNH BẬC NHẤT AX + B = 0")
print("-"*60)
a = float(input('Nhập hệ số  A: '))
b = float(input('Nhập hệ số  B: '))

if b>= 0:
    pt=f'{a}x + {b} = 0'
else:
    pt=f'{a}x - {-1*b} = 0'

if a != 0 and b == 0:
    print(f'Phương trình {pt} có nghiệm bằng 0')
else:
    if a != 0 and b != 0:
        print(f'Phương trình {pt} có nghiệm bằng {-b/a}')
    if a ==0 and b == 0:
        print(f'Phương trình {pt} có vô số nghiệm.')
    else:
        print('Phương trình vô nghiệm')
print()