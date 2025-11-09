rno = int(input('Enter Rno : '))
name = input('Enter Name : ')
ph = int(input('Enter Phy marks : '))
ch = int(input('Enter Che marks : '))
ma = int(input('Enter Maths marks : '))
bio = int(input('Enter Biology marks : '))
mar = int(input('Enter Marathi marks : '))

gt = ph + ch + ma + bio + mar
per = gt / 5.0
print(f'Rno {rno} Nmae = {name} Gt = {gt} Per = {per}')
