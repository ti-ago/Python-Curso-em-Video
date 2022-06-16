from math import degrees,acos
a = float(input('Qual o comprimento do lado 1 do triângulo ? '))
b = float(input('Qual o comprimento do lado 2 do triângulo ? '))
c = float(input('Qual o comprimento do lado 3 do triângulo ? '))
retas = [a,b,c]
if a+b<=c or a+c<=b or b+c<=a:
    print('\33[1;41m Não é possível formar um triângulo com essas medidas. \33[m')
else:
    cosalfa=(a**2-(b**2+c**2))/(-2*b*c)
    cosbeta=(b**2-(a**2+c**2))/(-2*a*c)
    cosgama=(c**2-(a**2+b**2))/(-2*a*b)
    alfa = degrees(acos(cosalfa))
    beta = degrees(acos(cosbeta))
    gama = degrees(acos(cosgama))
    print('\33[1;42m É possível formar um triângulo com essas medidas cujos ângulos serão\33[m \n {:.2f},{:.2f} e {:.2f}.'.format(alfa,beta,gama))

