s = float(input('Qual o salário atual do funcionário ? '))
if s<=1250:
    a =  s*1.15
    print('O novo salário do funcionário será de \33[1;33m R${:.2f}\33[m'.format(a))
else:
    a =  s*1.1
    print('O novo salário do funcionário será de \33[1;32m R${:.2f}\33[m'.format(a))


