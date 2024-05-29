# Estrutura Listas
# Pegar 5 questões 
# https://wiki.python.org.br/EstruturaDeRepeticao
""" 
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
def exce01():
    vetor = [1, 2, 3, 4, 5]
    i = 0
    
    for i in range(len(vetor)):
        print('Numero do Vetor {}: {}'.format(i+1, vetor[i]))
""" 
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
def exce02():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    i = 0
    p = 9

    for i in range(len(vetor)):
        print('Numero do Vetor {}: {}'.format(i+1, vetor[i]))

    print('\n')

    for i in range(len(vetor)):
        print('Numero do Vetor invertido {}: {}'.format(p, vetor[p]))
        p-=1
"""           
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
def exce03():
    vetorNotas = [10, 6, 7, 8]
    media = 0

    for i in range(len(vetorNotas)):
        print('Numero do Vetor {}: {}'.format(i+1, vetorNotas[i]))
        media += (vetorNotas[i] / 4)

    print('Media é: {}'. format(media))
""" 
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas 
consoantes foram lidas. Imprima as consoantes.
"""
def exce04():
    word = 'Bananananap'
    count = 0
    dontBe = ['a', 'i', 'u', 'e', 'o']
    i = 0

    for i in range(len(word)):
        if word[i] not in dontBe:
            count+=1

    print('Na palavra {} tem {} de consoantes'. format(word, count))
""" 
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""

def exce05():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    par = []
    impar = []
    i = 0
    for i in range(len(vetor)):
        if vetor[i] % 2 == 0:
            par.append(vetor[i])
        else:
            impar.append(vetor[i])

    print('{}\n{}\n{}\n'.format(vetor, par, impar))

exce05()