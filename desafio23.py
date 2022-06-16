'''n = str(input('Digite um número com 4 dígitos '))
print('No número digitado a unidade é {}, a dezena {} a centena {} e o milhar {}. '.format(n[3],n[2],n[1],n[0]))'''

n = int(input("Digite um número qualquer até 9999 \n"))
u = n%10
d = (n//10)%10
c = (n//100)%10
m = (n//1000)%10
print('No número digitado a unidade é {}, a dezena é {}, a centena é {} e o milhar é {}.'.format(u , d , c , m))