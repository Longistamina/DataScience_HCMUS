print()
#------------HÀM TỰ ĐỊNH NGHĨA-----------------
def tinh_tong(a,b):
    kq = a+b
    return kq

def tong_tich(a,b):
    tong = a+b
    tich = a*b
    return tong,tich #Trả về nhiều kết quả

#-----HÀM CÓ THAM SỐ  CÓ GIÁ TRỊ MẶC ĐỊNH---------
def tinh_tien_ban_hang (soluong,dongia,tygia=1.3):
    kq = soluong*dongia*tygia #tygia sẽ có giá trị không đổi = 1.3
    return kq

#------ *ARG: THAM SỐ  LÀ TẬP HỢP CÓ NHIỀU PHẦN TỬ  (TRỪ DICTIONARY)
def tinh_tich_dayso(*dayso): # *arg giúp python hiểu tham số truyền vào ở dạng tập hợp
    kq=1
    for i in dayso: kq *=i
    return kq
#---------CODE CỦA MAIN--------------

if __name__ == '__main__':
    s1 = tinh_tong(7,6) #Phải truyền giá trị cho tham số đúng thứ tự, đủ số  lượng tham số 
    s2 = tinh_tong(b=9,a=12) #Hoặc truyền theo định danh
    print('Sum1 =',s1)
    print('Sum2 =',s2)

    kqtong,kqtich = tong_tich(a=15,b=20) #Nhận hai kết quả được trả về  từ hàm tong_tich()

    tien1 = tinh_tien_ban_hang(3,50000) #Nếu không truyền tham số cho tygia, nó sẽ nhận giá trị mặc định = 1.3
    tien2 = tinh_tien_ban_hang(5,35000,tygia=1.5) #Hoặc cũng có thể truyền giá trị mới cho tygia
    
    kqtichDayso1 = tinh_tich_dayso(2,3,5,7) #Tập hợp 2,3,5,7 này là các phần tử  của *dayso, dayso lúc này là tuple
    lstSN = [1,6,9,12]
    kqtichDayso2 = tinh_tich_dayso(*lstSN) #nếu tham số ở dạng tập hợp sẵn thì phải có dấu * đằng trước
    print()