# Estrutura Textos
# Pegar 5 questões 
# https://wiki.python.org.br/EstruturaDeRepeticao
""" 
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe 
também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
"""
def exce01():
    strings = ['', '']
    strings[0] = input('Informe o primeiro texto: ')
    strings[1] = input('Informe o primeiro texto: ')

    i = 0
    print('\n')
    for i in range(len(strings)):
        print('Palavra {}: {}'.format(i, strings[i]))

    if strings[0] == strings[1]:
        print("As duas são iguais")
    else :
        print("As duas diferentes")
        if len(strings[0]) == len(strings[1]):
            print('As duas palavras tem o mesmo comprimento')
        else:
            print('As duas palavras Tem comprimento diferentes')
""" 
Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do 
usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode 
digitar letras maiúsculas ou minúsculas.
"""
def exce02():
    string = input('Digite qualquer nome do usuario\nPode ser maiusculas e Minusculas: ')
    string = string.upper()

    print('{}'.format(string))

    p = len(string) - 1
    i = 0

    for i in range(len(string)):
        print('{}'.format(string[p]))
        p -= 1
"""           
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
"""
def exce03():
    string = input('Digite qualquer nome do usuario: ')
    string = string.upper()

    i = 0

    for i in range(len(string)):
        print('{}'.format(string[i]))
""" 
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
"""
def exce04():
    string = input('Digite qualquer nome do usuario: ')
    string = string.upper()

    space = ''
    i = 0

    for i in range(len(string)):
        print('{}{}'.format(space, string[i]))
        space += ' '
""" 
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
"""
def exce05():
    string = input('Digite qualquer nome do usuario: ')
    string = string.upper()

    space = ''
    i = 0

    for i in range(len(string)):
        space += ' '

    for i in range(len(string)):
        print('{}{}'.format(space, string[i]))
        space = space[:-1]

exce05()