import math
a = float(input('Informe um ângulo qualquer\n'))
b = math.radians(a)
sen = (math.sin(b))
cos = (math.cos(b))
tan = (math.tan(b))
print('O seno de {} graus é {:.3f}\no cosseno é {:.3f}\ne a tangente é {:.3f}'.format(a, sen, cos, tan))