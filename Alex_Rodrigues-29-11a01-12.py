carros = []

class Veiculos:
    def __init__(self, cor, ano, modelo):
        self.cor = str(cor)
        self.ano =  int(ano)
        self.modelo = str(modelo)


obj1 = Veiculos('verde', 2010, 'Hilux')
obj2 = Veiculos('preto', 2018 , 'Fiesta')
obj3 = Veiculos('vermelho', 2021, 'Supra')
carros.append(obj1)
carros.append(obj2)
carros.append(obj3)
    

    
while True:
    print('====='*5)
    print("0-Sair do programa")
    print("1-Consultar lista de carros")
    print("2-Adicionar carro")
    print("3-Excluir carro da lista")
    print("4-Alterar carro")
    print('====='*5)


    escolha = int(input('Digite a opção de acordo com as citadas acima: '))

    if escolha == 0:
        print('====='*5)
        print('FIM')
        print('====='*5)

        break

# Consulta de objetos na lista
    elif escolha ==1 :
        print('====='*5)
        for carro in carros:
            print(f'Cor: {carro.cor} Ano: {carro.ano}  Modelo: {carro.modelo}')
        
        
# Adicionar objeto 
    elif escolha ==2:
        if len(carros)<5:
            print('Adicione abaixo de acordo com os requerimentos. ')
            cor = input("Digite a cor do carro:")
            ano = int(input('Digite o ano do carro: '))
            modelo = input('Digite o modelo do carro: ')
            carros.append(Veiculos(cor, ano, modelo))
        else:
            print('Erro, primeiro exclua um carro da lista')
           

# Remoção de elementos/objetos
    elif escolha ==3: 
        indice = int(input('Digite o numero do carro na lista que queira excluir: '))  
        for i in range(len(carros)):
            if i == indice:
                carros.pop(i)
                break
        else:
            print('Não existe carro com esse indice')

# Alteração de atributos
        
    elif escolha ==4:
        indice = int(input('Digite o numero do carro na lista que queira exclui: '))  
        for i in range(len(carros)):
            if i == indice:
                carros.pop(i)
                break
            cor = input("Digite a cor do carro:")
            ano = int(input('Digite o ano do carro: '))
            modelo = input('Digite o modelo do carro: ')
            carros.append(Veiculos(cor, ano, modelo))
            
        else:
            print('Escolha invalida.')


    else: 
        print('Escolha inválida!')            