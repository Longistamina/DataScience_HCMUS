import math
a=math.sqrt(16) #--> a = 4
b=math.pow(2,3) #--> b = 2^3 = 8
math.pi #---> số pi
dir(math) #---> xem xem trong thư viện math có bao nhiêu function

#math.floor(x) =>Trả về  số nguyên lớn nhất nhỏ hơn nó floor(5.25) = 5

#math.modf(x) => Tách x thành phần nguyên và phần thập phân, modf(7.5) => (0.5,7.0)
le,nguyen = math.modf(3.5)
print(le)
print(nguyen)