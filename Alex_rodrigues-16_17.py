print('==='*8)
print("Para cada questão de acordo com o numero dela\nQuestão 1/2/3/4")
escolha = int(input('Digite de acordo com as opções acima '))
print('==='*8)


    # questao 1
if escolha == 1:
    valid = soma = cont =0
    num = []
    while True :
        x = int(input('Digite um número:'))
        if x != -1:
            num.append(x)
            cont += 1
            soma += x
        else:   
            break

        


        amedia =   (soma / cont)
        print(f'A- Mostre a quantidade de valores que foram lidos; {cont}')
        print(f'B- Exiba todos os valores na ordem em que foram informados, um ao lado do outro;{num}')
        num.reverse()
        print(f'C- Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro{num}')
        print(f'D- Exiba a soma dos valores;{soma}')
        print(f'E- média dos valores encontrados é {(soma / cont):.2f}')
        cont = 0
        for x in num:
            if x > amedia:
                cont += 1

        print(f"F- {cont} notas sao maiores que {amedia:.2f}" )
        print('G- Acabou')

# questao 02
elif escolha ==2 :
    lista = list()

    while True:
    
     if lista.__len__() >= 5:
         break

     string = input('Digite uma palavra ')

     lista.append(string)
    for value, string in enumerate(lista):
     if string[0] == 'a':
         print(f'{value} {string}')

        





# Questao 03
elif escolha ==3:

    lista3 = list()

    while True:
        entrada: str = input('Digite uma palavras, para sair apenas clique na tecla espaço: ')

        verificacao: bool = False
        for i in entrada:
            if i == ' ':
             verificacao = True
            break
            
        if verificacao:
                break
        lista3.append(entrada)


    listaPrintados = list()

    for entrada in lista3:
       if entrada not in listaPrintados:
         print(entrada)
         listaPrintados.append(entrada)



# questao 04

elif escolha ==4:
    naipe = ['S', 'H', 'D', 'C']
    valor = [i for i in range(2, 10)] + [i for i in 'TJQKA']
    deck = list()

    for i in naipe:
        for j in valor:
            deck.append(f'{i}{j}')

    print(f'Deck não em baralhado : {deck}')
    Ouros   =  ['AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']
    Paus    =  ['AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC']
    Copas   =  ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH']
    Espadas =  ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS']





    for i in range(0, 52, 4):
        for j in range(51, -1, -3):
            deck[i], deck[j] = deck[j], deck[i]


    print(f"espada{Espadas}")
    print(f"copas{Copas}")
    print(f"ouros{Ouros}")
    print(f"paus{Paus}")


    print(deck)
    print(deck.__len__())





else:
    print('Escolha Inválida')