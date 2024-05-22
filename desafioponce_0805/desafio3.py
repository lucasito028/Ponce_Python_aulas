# Estrutura Repeticao
# Pegar 5 questões 
# https://wiki.python.org.br/EstruturaDeRepeticao Base
""" Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem 
caso o valor seja inválido e continue pedindo até que o usuário informe um valor 
válido. """
def exce01():
    a = 1
    while a == 1:
        nota = int(input('Coloque uma nota de um a 10: '))
        notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if nota in notas:
            print('A nota que informou na qual {} é valida'.format(nota))
            a = 2
        else:
            print('A nota que informou na qual {} é invalida'.format(nota))

""" Faça um programa que leia um nome de usuário e a sua senha e não aceite a 
senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a 
pedir as informações. """
def exce02():
    a = 1
    while a == 1:
        usuario = input('Seu apelido de usuario: ')
        senha = input('Sua senha: ')
        if senha == usuario:
            print('Senha não permitida: '.format(senha))
            
        else:
            print('Senha permitida: '.format(senha))
            a = 2
"""           
Faça um programa que leia e valide as seguintes informações:
- Nome: maior que 3 caracteres;
- Idade: entre 0 e 150;
- Salário: maior que zero;
- Sexo: 'f' ou 'm';
- Estado Civil: 's', 'c', 'v', 'd';
"""
def exce03():
    a = 1

    agePossible = range(0, 150)
    sexPossible =['f', 'm']
    statusPossible = ['s', 'c', 'v', 'd']

    a = 1
    while a == 1:
        name = input('Seu nome: ')
        age = int(input('Sua Idade: '))
        salary = float(input('Seu Salario: '))
        sex = input('Seu Sexo: ')
        status = input('Seu estatus: ')
        
        if (len(name) > 3 and age in agePossible 
        and salary > 0 and sex in sexPossible and status in statusPossible):
            print('Validado')
            a = 2
        else:
            print('Não Validado')


""" Supondo que a população de um país A seja da ordem de 80000 habitantes com 
uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva 
o número de anos necessários para que a população do país A ultrapasse ou 
iguale a população do país B, mantidas as taxas de crescimento.
"""

""" Altere o programa anterior permitindo ao usuário informar as populações e as 
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. """


exce03()