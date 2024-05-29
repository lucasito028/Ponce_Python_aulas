# Estrutura sequancial
# Pegar 5 questões 
# https://wiki.python.org.br/EstruturaSequencial 

# 1 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def excercise1():
    print('Alo Mundo')
    
# 2 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def excercise2():
    a = input('Coloque o numero ai:')
    print("O número informado foi: {}".format(a))
    
# 3 - Faça um Programa que peça dois números e imprima a soma.
def excercise3():
    a = int(input('Coloque o primeiro numero ai:'))
    b = int(input('Coloque o Segundo numero ai:'))
    b += a
    print("Soma dos 2 deu: {} ".format(b))
    
# 4 -Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def excercise4():
    n = [0, 0, 0, 0, 0]

    n[0] = float(input('Coloque o primeiro nota ai: '))
    n[1] = float(input('Coloque o Segundo nota ai: '))
    n[2] = float(input('Coloque o Terceiro nota ai: '))
    n[3] = float(input('Coloque o Quarta nota ai: '))
    
    n[4] = (n[0] + n[1] + n[2] + n[3]) / 4

    print("Das 4 deu: {}".format(n[4]))
    
# 5 - Faça um Programa que converta metros para centímetros.
def excercise5():
    m = float(input('Coloque a medida em metros:'))
    cm = m * 100
    print("O de m foi para {}cm".format(cm))

excercise2()
