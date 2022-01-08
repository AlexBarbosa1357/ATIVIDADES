
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



if __name__ == '__main__':

	estoque = list()

	def searchCar(marca: str):
		for car in estoque:
			car: Veiculo
			if car.marca == marca:
				print(f'Placa: {car.placa}, marca: {car.marca}, cor: {car.cor}, chassis: {car.chassis}, ano: {car.ano}, modelo: {car.modelo}')

	def outputCars():
		for car in estoque:
			car: Veiculo

			print(f'Placa: {car.placa}, marca: {car.marca}, cor: {car.cor}, chassis: {car.chassis}, ano: {car.ano}, modelo: {car.modelo}')


	while True:
		escolha = input('Continuar produzindo?[ s/n ]\n=> ')
		
		if 'n' == escolha:
			break

		elif 's' == escolha:
			estoque.append(Veiculo(
				placa=input('Digite a placa do carro: '),
				marca=input('Digite a marca do carro: '),
				cor=input('Digite a cor do carro: '),
				chassis=input('Digite o chassis do carro: '),
				ano=int(input('Digite o ano do carro: ')),
				modelo=input('Digite o modelo do carro: '),
			))

	searchCar(
		input('Digite a marca do carro: ')
	)

	print('\n\n')

	outputCars()

	estoque[0].changeColor('Vermelho')
	


