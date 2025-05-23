#Kiểm tra số nguyên tố
def kTra_soNgTo (n):
    if n <= 1: return False #Nếu điều kiện này thoả thì nó sẽ return False và thoát hàm, không thực hiện nữa
    for i in range(2,n):
        if n%i == 0: return False
    return True

if __name__ == '__main__':
    lstN = [5,7,2,8,9,12,24,5,9,2,11,12]
    lstNgTo = list(filter(kTra_soNgTo,lstN))
    print(lstN)
    print(lstNgTo)