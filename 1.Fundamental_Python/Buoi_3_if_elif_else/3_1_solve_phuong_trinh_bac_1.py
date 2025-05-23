'''
Giải phương trình bậc 1: ax+b=0
'''
print()
print("GIẢI PHƯƠNG TRÌNH BẬC NHẤT AX + B = 0")
print("-"*60)
a = float(input('Nhập hệ số  A: '))
b = float(input('Nhập hệ số  B: '))

if a != 0:
    print(f'Nghiệm của phương trình là X = -B/A = {-(b/a)}')
elif a == 0 and b == 0:
    print('Phương trình này có vô số  nghiệm.')
else:
    print('Phương trình này vô nghiệm.')
print()