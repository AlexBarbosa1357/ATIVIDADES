# ---Declarando Lista e Classe
carros = []
class Veiculos:
    def __init__(self, cor, ano, modelo):
        self.cor = str(cor)
        self.ano =  int(ano)
        self.modelo = str(modelo)
# ---Criando 3 objetos iniciais
obj1 = Veiculos('Verde', 2010, 'Hilux')
obj2 = Veiculos('Preto', 2018 , 'Fiesta')
obj3 = Veiculos('Vermelho', 2021, 'Supra')
# ---Adicionando na Lista criada para armazenar
carros.append(obj1)
carros.append(obj2)
carros.append(obj3)
# ---Menu do Software
while True:
    print('_+_+_+_+_+_+_+'*5)
    print("0-Sair do programa")
    print("1-Consultar lista de carros")
    print("2-Adicionar carro")
    print("3-Excluir carro da lista")
    print("4-Alterar carro")
    print('_+_+_+_+_+_+_+'*5)
# ---Váriavel de entrada de dados do usuário
    escolha = int(input('Digite a opção de acordo com as citadas acima: '))
# ---Saindo do programa
    if escolha == 0:
        print('_+_+_+_+_+_+_+'*5)
        print('FIM')
        print('_+_+_+_+_+_+_+'*5)
        break

# ---Consulta de objetos na lista
    elif escolha ==1 :
        print('_+_+_+_+_+_+_+'*5)
        for carro in carros:
            print(f'Cor: {carro.cor} Ano: {carro.ano}  Modelo: {carro.modelo}')
        
        
# ---Adicionar objeto 
    elif escolha ==2:
        if len(carros)<5:
            print('Adicione abaixo de acordo com os requerimentos. ')
            cor = str(input("Digite a cor do carro: ")).capitalize()
            ano = int(input('Digite o ano do carro: '))
            modelo = str(input('Digite o modelo do carro: ')).capitalize()
            carros.append(Veiculos(cor, ano, modelo))
        else:
            print('Erro, primeiro exclua um carro da lista')
           

# ---Remoção de elementos/objetos
    elif escolha ==3: 
        indice = int(input('Digite o numero do carro na lista que queira excluir: '))  
        for i in range(len(carros)):
            if i == indice:
                carros.pop(i)
                break
        else:
            print('Não existe carro com esse indice')

# ---Alteração de atributos      
    elif escolha ==4:
        indice = int(input('Digite o numero do carro na lista escolhido para alteração: '))  
        for i in range(len(carros)):
            if i == indice:
                carros.pop(i)
                break
            cor = str(input("Digite a cor do carro: ")).capitalize()
            ano = int(input('Digite o ano do carro: '))
            modelo = str(input('Digite o modelo do carro: ')).capitalize()
            carros.append(Veiculos(cor, ano, modelo))
            
        else:
            print('Escolha invalida.')

# ---Escolha Inválida
    else: 
        print('Opção não existente no menu!')            