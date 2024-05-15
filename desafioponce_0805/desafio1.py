# Estrutura sequancial
# Pegar 5 questões 
# https://wiki.python.org.br/EstruturaSequencial Base

# 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def excercise1():
    print('Alo Mundo')
    
# 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def excercise2():
    a = int(input('Coloque o numero ai:'))
    print("O número informado foi [{}]".format(a))
    
# 3 - Faça um Programa que peça dois números e imprima a soma.
def excercise3():
    a = int(input('Coloque o primeiro numero ai:'))
    b = int(input('Coloque o Segundo numero ai:'))
    b += a
    print("Soma dos 2 deu:{}".format(b))
    
# 4 -Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def excercise4():
    n1 = int(input('Coloque o primeiro nota ai:'))
    n2 = int(input('Coloque o Segundo nota ai:'))
    n3 = int(input('Coloque o Terceiro nota ai:'))
    n4 = int(input('Coloque o Quarta nota ai:'))
    n4 = (n3 + n2 + n1 + n4) / 4
    print("Das 4 deu{}".format(n4))
    
# 5 - Faça um Programa que converta metros para centímetros.
def excercise5():
    m = float(input('Coloque o primeiro nota ai:'))
    cm = m * 100
    print("O de m foi para {}cm".format(cm))

excercise5()
