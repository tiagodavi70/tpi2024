
#CDU - UDC
# 456
cdu = input("Entre com um numero de tres digitos: ")
cdu = int(cdu)

c = cdu // 100
d = (cdu - c*100) // 10 
u = cdu % 10

udc = (u * 100) + (d * 10) + c

print(udc)