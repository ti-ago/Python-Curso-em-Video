nota1=float(input('Qual a primeira nota do aluno ? '))
nota2=float(input('Qual a segunda nota do aluno ? '))
media=((nota1+nota2)/2)

if nota1<0 or nota1>10 or nota2 <0 or nota2>10:
    print('Notas inválidas, preencha novamente')
elif media<5:
    print('O aluno foi reprovado, sua média foi {:.1f} .'.format(media))
elif media>=5 and media<7:
    print('O aluno está de recuperação, sua média foi {:.1f} .'.format(media))
elif media>=7 and media<=10:
    print('O aluno está aprovado, sua média foi {:.1f} .'.format(media))

