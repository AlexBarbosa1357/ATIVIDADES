# ---Declação de classe e seus métodos apartir da linha 11
class Veiculo:
	def __init__(self, chassis, marca, modelo, ano, cor, placa) -> None:
		self.chassis = chassis
		self.marca = marca
		self.modelo = modelo
		self.ano = ano
		self.cor = cor 
		self.placa = placa
    
	def changeColor(self, newColor: str) -> None:
		"""Esse metodo troca a cor do carro """
		self.cor = newColor

	def Ligar(self):
		print('Seu carro Ligou ')

	def acelerar(self):
		print('Você está acelerando o veiculo ')

	def frear(self):
		print('Você está freando o veiculo ')

	def esquerda(self):
		print('Você está virando a esquerda ')

	def direita(self):
		print('Você virou a direita ')

	def desligar(self):
		print('Você está parando o veiculo e desligando o mesmo ')
		print('Fim, você parou o carro e deligou o mesmo')
# ---Declarando lista
estoque = list()


# ---Função de pesquisa de carro
def searchCar(marca: str):
	for car in estoque:
		car: Veiculo
		if car.marca == marca:
			print(f'Placa: {car.placa}, marca: {car.marca}, cor: {car.cor}, chassis: {car.chassis}, ano: {car.ano}, modelo: {car.modelo}')
# ---Função para ver as caracteristicas do carro
def outputCars():
	for index, car in enumerate(estoque):
		car: Veiculo
		print(f'Index{index}, placa: {car.placa}, marca: {car.marca}, cor: {car.cor}, chassis: {car.chassis}, ano: {car.ano}, modelo: {car.modelo}')

# ---Menu inicial
while True:
	
	escolha = int(input('Digite de acordo com a escolha\n1-Fabricar mais carros  2-Pesquisar por um carro especifico  3-Consultar Caractereisticas dos carros \n  4-Trocar cor de um carro   5-Sair:'))
	if escolha == 1:
	    	while True:	
				escolha = input('Digite S-Para continuar fabricando  e  N-Para parar de fabricar')

				if 'n' == escolha.lower():
					break
				
				elif 's' == escolha.lower():
					estoque.append(Veiculo(
						placa=input('Digite a placa do carro: '),
						marca=input('Digite a marca do carro: ').capitalize(),
						cor=input('Digite a cor do carro: ').capitalize(),
						chassis=input('Digite o chassis do carro: '),
						ano=int(input('Digite o ano do carro: ')),
						modelo=input('Digite o modelo do carro: ').capitalize(),
					))
					print('\n ==================================================='*5)

				else:
					print('Escolha inválida!')
					break
	elif escolha==2:
		# ---Puxando função para pesquisar o carro
		searchCar(input('Digite a marca do carro: '))
	elif escolha==3:
		# ---Puxando função para consultar as caracteristicas do carro
		outputCars()
	elif escolha ==4:
		# ---Trocando a cor do carro
		num=int(input('Digite o index do carro'))
		estoque[num].changeColor(str(input("Digite a nova cor do veículo: ")))
	elif escolha==5:
		print('Fim!')
		break
	else:
		print('Escolha de operação inválida!')