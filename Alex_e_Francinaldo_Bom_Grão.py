# ---DECLARAÇÃO DE CLASSES, VAIRAVEIS E LISTAS

# ___ Dicionario numa nova area pra mostrar pTrabalhoreços,  e no historico de compras clientes e gerente

compradores = []
gestao_gerente = []
senha = "adm123"
# valor_arroz = 2.10
# valor_feijao = 1.25
# valor_acucar = 1.10
# valor_milho = 1.30
valor_graos = {'arroz' : 2.10, 'feijao': 1.25, 'açucar':1.10, 'milho':1.30}
class Gestao_Cliente:
	def __init__(self, nome, data, pagamento, kilos_arroz, kilos_feijao, kilos_acucar, kilos_milho, gasto_cliente):
		self.nome = nome
		self.data = data
		self.pagamento = pagamento
		self.kilos_arroz = kilos_arroz
		self.kilos_feijao = kilos_feijao
		self.kilos_acucar = kilos_acucar
		self.kilos_milho = kilos_milho
		self.gasto_cliente = gasto_cliente

class Gestao_Graos:
	def __init__(self, quantidade_arroz, quantidade_feijao, quantidade_acucar, quantidade_milho, caixa, total_renda, valor_total):
		self._quantidade_arroz = quantidade_arroz
		self._quantidade_feijao = quantidade_feijao
		self._quantidade_acucar = quantidade_acucar
		self._quantidade_milho =  quantidade_milho
		self._caixa = caixa
		self._total_renda = total_renda
		self._valor_total = valor_total

	# get quantidade_arroz
	@property
	def quantidade_arroz(self):
		return self._quantidade_arroz	
	# set quantidade_arroz
	@quantidade_arroz.setter
	def quantidade_arroz(self,quantidade_arroz):
		self._quantidade_arroz = quantidade_arroz
	# ------------------------------------------------------------------------------
	# get quantidade_feijao
	@property
	def quantidade_feijao(self):
		return self._quantidade_feijao
	# set quantidade_feijao
	@quantidade_feijao.setter
	def quantidade_feijao(self,quantidade_feijao):
		self._quantidade_feijao = quantidade_feijao
	# ------------------------------------------------------------------------------
	# get quantidade_acucar
	@property
	def quantidade_acucar(self):
		return self._quantidade_acucar	
	# set quantidade_acucar
	@quantidade_acucar.setter
	def quantidade_acucar(self,quantidade_acucar):
		self._quantidade_acucar = quantidade_acucar
	# ------------------------------------------------------------------------------
	# get quantidade_milho
	@property
	def quantidade_milho(self):
		return self._quantidade_milho	
	# set quantidade_milho
	@quantidade_milho.setter
	def quantidade_milho(self,quantidade_milho):
		self._quantidade_milho = quantidade_milho
	# ------------------------------------------------------------------------------
	# get caixa
	@property
	def caixa(self):
		return self._caixa	
	# set caixa
	@caixa.setter
	def caixa(self,caixa):
		self._caixa = caixa
	# ------------------------------------------------------------------------------
	# get total_renda
	@property
	def total_renda(self):
		return self._total_renda	
	# set total_renda
	@total_renda.setter
	def total_renda(self,total_renda):
		self._total_renda = total_renda
	# ------------------------------------------------------------------------------
	# get valor_total
	@property
	def valor_total(self):
		return self._valor_total	
	# set valor_total
	@valor_total.setter
	def valor_total(self,valor_total):
		self._valor_total = valor_total


# ---Usuário digitando quantidade de quilos e caixa inicial 
quantidade_arroz = float(input("Digite a Quantidade de Arroz no Estoque (Em KG): "))
quantidade_feijao = float(input("Digite a Quantidade de Feijão no Estoque (Em KG): "))
quantidade_acucar = float(input("Digite a Quantidade de Açucar no Estoque (Em KG): "))
quantidade_milho = float(input("Digite a Quantidade de Milho no Estoque (Em KG): "))
caixa = float(input("Digite A renda Inicial do Comercio (Em R$): "))
# ---Adicionando na lista
gestao_gerente.append(Gestao_Graos(quantidade_arroz, quantidade_feijao, quantidade_acucar, quantidade_milho, caixa, 0, 0)) #Graos e Renda do Comercio.
# ---FUNÇÃO PARA GERENTE OU DONO REFAZER O ESTOQUE
def Restoque():
	print("-+-+-+-+-+-+"*20)
	total_arroz = float(input("Informe a quantidade de Kilos Arroz comprados: "))
	total_feijao = float(input("Informe a quantidade de Kilos de Feijão comprados: "))
	total_acucar = float(input("Informe a quantidade de Kilos de Açucar comprados: "))
	total_milho = float(input("Informe a quantidade de Kilos de milho comprados: "))
	total_renda = float(input("Informe a Quantia gasta em Arroz, Feijão, Açucar e Milho em R$:"))
	print("-+-+-+-+-+-+"*20)
	for x in gestao_gerente:
		# x.caixa = round( )
		print("-+-+-+-+-+-+"*20)
		x.quantidade_arroz = total_arroz + x.quantidade_arroz
		print(f"A Quantidade de Arroz agora é {x.quantidade_arroz}Kg")
		x.quantidade_feijao = total_feijao + x.quantidade_feijao
		print(f"A Quantidade de Feijão agora é {x.quantidade_feijao}Kg")
		x.quantidade_acucar = total_acucar + x.quantidade_acucar
		print(f"A Quantidade de Açucar agora é {x.quantidade_acucar}Kg")
		x.quantidade_milho = total_milho + x.quantidade_milho
		print(f"A Quantidade de milho agora é {x.quantidade_milho}Kg")
		print("-+-+-+-+-+-+"*20)
		x.caixa = x.caixa - total_renda
		x.total_renda = total_renda
		print(f"O dinheiro Gasto em Arroz, Feijão, Açucar e Milho foi R${total_renda}")
		print(f"A renda agora é de R${round(x.caixa,2)}")
		print("-+-+-+-+-+-+"*20)
# ---VERIFICANDO QUANTIDADE DE GRÂOS
def Verificar_graos():
	print(valor_graos.items())
	print('_+_+_+_+_+'*10)
	for x in gestao_gerente:
				print(f"Arroz {x.quantidade_arroz}Kg")
				print(f"Feijão {x.quantidade_feijao}Kg")
				print(f"Açucar {x.quantidade_acucar}Kg")
				print(f"Milho {x.quantidade_milho} Kg")
# ---FUNÇÃO DO CLIENTE COMPRAR ARROZ:
def Comprar_Arroz():
	print("-+-+-+-+-+-+"*14)
	nome = str(input("Informe seu Nome: "))
	data = str(input("Informe a Data da compra: "))
	pagamento = str(input("Informe a forma de pagamento: [Pix ou Espécie] "))
	kilos_arroz = float(input("Informe a quantidade de Kilos Arroz comprados: "))
	print("-+-+-+-+-+-+"*20)
	gasto_cliente = kilos_arroz * valor_graos.get('arroz')
	for x in gestao_gerente:
		if kilos_arroz <= x.quantidade_arroz:
			x.quantidade_arroz = x.quantidade_arroz - kilos_arroz 
			x.caixa = x.caixa + gasto_cliente
			print("-+-+-+-+-+-+"*20)
			print(f"O total a ser Pago é: R${gasto_cliente}")
			print(f"A Quantidade de Arroz requirida foi: {kilos_arroz}Kg")
			print("-+-+-+-+-+-+"*20)   
			compradores.append(Gestao_Cliente(nome, data, pagamento, kilos_arroz, "", "", "", gasto_cliente))
		else:
			print(f"Sem quantidade de Estoque Suficiente para essa Quantidade \nTemos Apenas {x.quantidade_arroz}Kg em estoque")
			break
# ---FUNÇÃO DO CLIENTE COMPRAR FEIJÂO
def Comprar_Feijao():
	print("-+-+-+-+-+-+"*20)
	nome = str(input("Informe seu Nome: "))
	data = str(input("Informe a Data da compra: "))
	pagamento = str(input("Informe a forma de pagamento: [Pix ou Espécie] "))
	kilos_feijao = int(input("Informe a quantidade de Kilos de Feijão comprados: "))
	print("-+-+-+-+-+-+"*20)
	gasto_cliente = kilos_feijao * valor_graos.get('feijao') 
	for x in gestao_gerente:
		if kilos_feijao <= x.quantidade_feijao:
			x.quantidade_feijao = x.quantidade_feijao - kilos_feijao 
			x.caixa = x.caixa + gasto_cliente
			print("-+-+-+-+-+-+"*20)
			print(f"O total a ser Pago é: R${gasto_cliente}")
			print(f"A Quantidade de Feijão requirida foi: {kilos_feijao}Kg")
			print("-+-+-+-+-+-+"*20)
			compradores.append(Gestao_Cliente(nome, data, pagamento, "", kilos_feijao, "", "", gasto_cliente))
		else:
			print(f"Sem quantidade de Estoque Suficiente para essa Quantidade \nTemos Apenas {x.quantidade_feijao}Kg em estoque")
			break
# ---FUNÇÃO DO CLIENTE COMPRAR AÇUCAR
def Comprar_Acucar():
	print("-+-+-+-+-+-+"*20)
	nome = str(input("Informe seu Nome: "))
	data = str(input("Informe a Data da compra: "))
	pagamento = str(input("Informe a forma de pagamento: [Pix ou Espécie] "))
	kilos_acucar = int(input("Informe a quantidade de Kilos de Açucar comprados: "))
	print("-+-+-+-+-+-+"*20)
	gasto_cliente = kilos_acucar * valor_graos.get('açucar')
	for x in gestao_gerente:
		if kilos_acucar <= x.quantidade_acucar:
			x.quantidade_acucar = x.quantidade_acucar - kilos_acucar 
			x.caixa = x.caixa + gasto_cliente
			compradores.append(Gestao_Cliente(nome, data, pagamento, "", "", kilos_acucar, "", gasto_cliente))
			print("-+-+-+-+-+-+"*20)
			print(f"O total a ser Pago é: R${gasto_cliente}")
			print(f"A Quantidade de Açucar requirida foi: {kilos_acucar}Kg")
			print("-+-+-+-+-+-+"*20)
		else:
			print(f"Sem quantidade de Estoque Suficiente para essa Quantidade \nTemos Apenas {x.quantidade_acucar}Kg em estoque")
			break
# ---FUNÇÃO DO CLIENTE COMPRAR MILHO
def Comprar_Milho():
	print("-+-+-+-+-+-+"*20)
	nome = str(input("Informe seu Nome: "))
	data = str(input("Informe a Data da compra: "))
	pagamento = str(input("Informe a forma de pagamento: [Pix ou Espécie] "))
	kilos_milho = int(input("Informe a quantidade de Kilos de Milho comprados: "))
	print("-+-+-+-+-+-+"*20)
	gasto_cliente = kilos_milho * valor_graos.get('milho')
	for x in gestao_gerente:
		if kilos_milho <= x.quantidade_milho:
			x.quantidade_milho = x.quantidade_milho - kilos_milho 
			x.caixa = x.caixa + gasto_cliente
			print("-+-+-+-+-+-+"*20)
			print(f"O total a ser Pago é: R${gasto_cliente}")
			print(f"A Quantidade de Milho requirida foi: {kilos_milho}Kg")
			print("-+-+-+-+-+-+"*20)
			compradores.append(Gestao_Cliente(nome, data, pagamento, "", "", "", kilos_milho, gasto_cliente))
		else:
			print(f"Sem quantidade de Estoque Suficiente para essa Quantidade \nTemos Apenas {x.quantidade_feijao}Kg em estoque")
			break
# ---FUNÇÃO PARA VERIFICAR HISTORICO DE VENDAS DOS CLIENTES
def Verificando_ultimas_vendas():
	for x in compradores:
		print("-+-+-+-+-+-+"*20)
		print(f"Nome:{x.nome}")
		print(f"Data:{x.data}")
		print(f"Forma Pagamento:{x.pagamento}")
		print(f"Arroz:{x.kilos_arroz}Kg | Feijão:{x.kilos_feijao}Kg | Açucar:{x.kilos_acucar}Kg | Milho:{x.kilos_milho}Kg")
		print(f"Valor da Venda:R${x.gasto_cliente}")
		print("-+-+-+-+-+-+"*20)
# ---COMPRANDO GRÂOS
def Comprar_Graos():	
	while True: #-----MENU GRÂOS
		print("-+-+-+-+-+-+"*20)
		print("1- Comprar Arroz \n2- Comprar Feijão \n3- Comprar Açucar \n4- Comprar Milho \n0- Sair")
		print("-+-+-+-+-+-+"*20)
		opcao = str(input("Informe a Opção: "))
		if opcao == "1": # ---Comprando arroz
			Comprar_Arroz()
		elif opcao == "2": # ---Comprando Feijão
			Comprar_Feijao()
		elif opcao == "3": # ---Comprando Açucar
			Comprar_Acucar()
		elif opcao == "4": # ---Comprando Milho
			Comprar_Milho()         
		elif opcao == "0":
			break
		else:
			print("Opção Invalida.")
	pass  
# ---FUNÇÃO MENU DO CLIENTE
def Gestao_cliente():
	while True:
		print("-+-+-+-+-+-+"*20)
		print("1- Comprar Grãos \n2- verificar Grãos \n0- Sair")
		print("-+-+-+-+-+-+"*20)
		opcao = str(input("Informe a Opção: "))
		if opcao == "1":
			Comprar_Graos()
		elif opcao == "2":
			Verificar_graos()
		elif opcao == "0":
			break
		else:
			print("Opção Invalida.")
# ---FUNÇÃO PARA VERIFICAR LUCRO
def Verificando_Lucros():
	valor_total = 0
	for x in compradores:
		valor_total = x.gasto_cliente + valor_total
	lucro = 0
	contador = 0
	for x in gestao_gerente:
		lucro =  valor_total - x.total_renda
		contador += 1
		print(f"O Restoque {contador} Tem Lucro de:{lucro}") 
	if lucro > 0:
		print(f'Na semana houve lucro de R${round(lucro, 2)} ')
	else:
		print(f'Na semana não houve lucro') 	
# ---FUNÇÃO MENU DO GERENTE OU DONO
def Gestao_Gerente():
	while True:
		print("-+-+-+-+-+-+"*20)
		print("1- Verificar Ultimas Vendas \n2- Verificar Saldo \n3- Verificar Estoque \n4- Restoque \n5- Verificar Lucros\n0- Sair")
		print("-+-+-+-+-+-+"*20)
		opcao = str(input("Informe a Opção: "))
		if opcao == "1":
			Verificando_ultimas_vendas()
		elif opcao == "2":
			for x in gestao_gerente:
				print(f"O Saldo do Comercio e: R${round(x.caixa, 2)}")
		elif opcao == "3":
			Verificar_graos()
		elif opcao == "4":
			Restoque()
		elif opcao == "5":
			Verificando_Lucros()
		elif opcao == "0":
			break
		else:
			print("Opção Invalida.")
#  ---MENU INICIAL DO PROGRAMA
while True:
	print("-+-+-+-+-+-+"*20)
	print("1- Gestão Clientes \n2- Gestão Gerente\n3- Trocar senha \n0- Sair")
	print("-+-+-+-+-+-+"*20)
	opcao = str(input("Informe a Opção: "))
	if opcao == "1":
			Gestao_cliente()
	elif opcao == "2":
		opc = str(input("Digite Sua Senha: "))
		if opc == senha:
			Gestao_Gerente()
		else:
			print("Senha Invalida.")
	elif opcao == "3":
		opc = str(input("Digite Sua Senha: "))
		if opc == senha:  
			senha = str(input("digite a nova senha: "))
	elif opcao == "0":
		break
	else:
		print("Opção Invalida.")
# ---SOLI DEO GLORIA---#