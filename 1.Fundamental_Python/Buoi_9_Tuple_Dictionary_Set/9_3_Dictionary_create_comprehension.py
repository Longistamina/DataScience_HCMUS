print()
lstMaSo = ['H01','H02','H03','H04'] 
lstDonGia = [100,200,300,400]

#dict comprehension
dictHH1 = {ms:dg for ms,dg in zip(lstMaSo,lstDonGia)}
print(dictHH1) #{'H01': 100, 'H02': 200, 'H03': 300, 'H04': 400}

print()
dictHH2 = {ms:dg for ms,dg in zip(lstMaSo,lstDonGia) if dg > 100}
print(dictHH2) #{'H02': 200, 'H03': 300, 'H04': 400}