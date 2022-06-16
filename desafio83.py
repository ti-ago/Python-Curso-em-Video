controlador=[]
expressao=str(input('Digite a expressão: '))
for digito in expressao:
    if digito == '(':
        controlador.append('(')
    elif digito == ')':
        if len(controlador)==0:
            controlador.append(')')
            break
        else:
            controlador.pop()

if len(controlador)!=0:
    print('Expressão inválida')
else:
    print('Expressão válida')