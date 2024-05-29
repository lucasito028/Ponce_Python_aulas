# Estrutura de Decisão
# Pegar 5 questões 
# https://wiki.python.org.br/EstruturaDeDecisao

# 1 - Faça um Programa que peça dois números e imprima o maior deles.
def excercise1():
    a = int(input('Coloque o primeiro numero ai: '))
    b = int(input('Coloque o Segundo numero ai: '))
    if a > b:
        print("A: {} é maior que B: {}". format(a, b))
    else:
        print("B: {} é maior que A: {}". format(b, a))
    
# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
def excercise2():
    a = int(input('Coloque o numero ai: '))
    if a < 0:
        print('Numero {} é Negativo'.format(a))
    if a > 0:
        print('Numero {} é Positivo'.format(a))
    if a == 0:
        print('Numero é 0')
    
# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
def excercise3():
    s = input('Sexo -M ou -F ')
    if s == 'M':
        print('Sexo Masculino')
    if s == 'F':
        print('Sexo Feminino')
    if s != 'F' and s != 'M':
        print('Não sei que sexo é')
    
# 4 -Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
def excercise4():
    s = input('Verifique a letra digitada: ')

    s = s.upper()

    match s:
        case 'A':
            print('Vogal')
        case 'E':
            print('Vogal')
        case 'I':
            print('Vogal')
        case 'O':
            print('Vogal')
        case 'U':
            print('Vogal')
        case _:
            print('Consoante')
    
""" 
5- Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
def excercise5():
    n1 = float(input('Coloque o primeiro nota ai:'))
    n2 = float(input('Coloque o Segundo nota ai:'))
    n3 = float(input('Coloque o Terceiro nota ai:'))
    n4 = float(input('Coloque o Quarta nota ai:'))
    
    n4 = (n3 + n2 + n1 + n4) / 4

    print("Das 4 deu: {}".format(n4))

    if n4 > 7 and n4 < 10:
        print('Aprovado')
    if n4 == 10:
        print('Aprovado com Distincao')
    else :
        print('Reprovado')

excercise5()