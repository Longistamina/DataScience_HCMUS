'''
Bài này tìm hiểu về  local variable (biến địa phương) và global variable (biến toàn cục)
'''
print()
tenHocsinh = 'An' #Global variable, luôn tồn tại miễn là chương trình còn chạy, không phụ thuộc hàm hay for while loop
def Inthongtin1():
    print(f'1 - Tên HS (global variable): {tenHocsinh}')

def Inthongtin2():
    hoHS = 'Lê'
    tenHS = 'Bình' #Local variable, chỉ tồn tại khi hàm được thực thi, sau khi xong thì biến sẽ bị xoá
    print(f'2 - Tên HS (local variable): {hoHS} {tenHS}')

def Inthongtin3():
    global hoHocsinh2 #khai báo biến hoHocsinh2 là global, dù là ở trong hàm python vẫn xem nó là global, không phải local nữa
    hoHocsinh2 = 'Đỗ ' #nên khi hàm được thực hiện xong  thì biến này vẫn còn, không biến mất
    
    global tenHocsinh2
    tenHocsinh2 = 'Phủ'

if __name__ == '__main__':
    #%%
    Inthongtin1()

    #%%
    Inthongtin2()
    print(f'Tên HS (global): {tenHocsinh}') #biến global vẫn tồn tại

    #%%
    Inthongtin3()
    print(f'3 - Tên HS (Global): {hoHocsinh2} {tenHocsinh2}')