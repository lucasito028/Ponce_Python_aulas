# Estrutura de Decisão
# Pegar 5 questões 
# https://wiki.python.org.br/EstruturaDeDecisao Base

# 1 - Faça um Programa que peça dois números e imprima o maior deles.
def excercise1():
    a = int(input('Coloque o primeiro numero ai: '))
    b = int(input('Coloque o Segundo numero ai: '))
    if a > b:
        print("A é maior que B")
    else:
        print("B é maior que A")
    
# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def excercise2():
    a = int(input('Coloque o numero ai: '))
    if a < 0:
        print('Numero {} é Negativo'.format(a))
    if a > 0:
        print('Numero {} é Positivo'.format(b))
    else:
        print('Numero é 0')
    
# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
def excercise3():
    s = input('Sexo -M ou -F ')
    if s == 'M':
        print('Sexo Masculino')
    if s == 'F':
        print('Sexo Feminino')
    else:
        print('Não sei que sexo é')
    
# 4 -Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def excercise4():
    s = input('Verifique a letra digitada: ')

    match s:
        case 'a':
            print('Vogal')
        case 'e':
            print('Vogal')
        case 'i':
            print('Vogal')
        case 'o':
            print('Vogal')
        case 'u':
            print('Vogal')
        case _:
            print('Consoante')
    
# 5 - Faça um Programa que converta metros para centímetros.
def excercise5():
    n1 = int(input('Coloque o primeiro nota ai:'))
    n2 = int(input('Coloque o Segundo nota ai:'))
    n3 = int(input('Coloque o Terceiro nota ai:'))
    n4 = int(input('Coloque o Quarta nota ai:'))
    
    n4 = (n3 + n2 + n1 + n4) / 4

    print("Das 4 deu{}".format(n4))

    if n4 > 7:
        print('Aprovado')
    else :
        print('Reprovado')

excercise5()