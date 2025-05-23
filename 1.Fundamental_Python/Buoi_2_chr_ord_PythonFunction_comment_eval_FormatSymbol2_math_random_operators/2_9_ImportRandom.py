import random

n1 = random.random() #Phát sinh một số  thực ngẫu nhiên [0,1)
print(n1)

n2 = random.uniform(10,20) #Phát sinh một số  thực ngẫu nhiên >10 <20
print(n2)

n3 = random.randrange(10,20,1) #Phát sinh một số  nguyên ngẫu nhiên [10,19], step là 1
print(n3)

n4 = random.randint(10,20) #Phát sinh một số  nguyene ngẫu nhiên [10,20]
print(n4)