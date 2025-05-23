'''
Có thể  import global variable từ một module khác vào để sử dụng
'''
import ex03_local_global_variable as ex03
import math
print()

tenHS = ex03.tenHocsinh
print(tenHS)

soPi = math.pi
print(soPi)