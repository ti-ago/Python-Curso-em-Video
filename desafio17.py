import math
catop = float(input('Qual o valor do cateto oposto do triângulo ?\n'))
catad = float(input('Qual o valor do cateto adjacente do triângulo ?\n'))
a = math.pow(catop, 2)
b = math.pow(catad, 2)
hyp = math.sqrt(a+b)
print('A hipotenusa do triângulo é de {}'.format(hyp))