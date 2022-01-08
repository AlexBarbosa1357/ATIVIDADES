#  ---DECLARAÇÃO DE CLASSES, VAIRAVEIS E LISTAS 
compradores = []
gestao_gerente = []
senha = "adm123"
valor_arroz = 2.10
valor_feijao = 1.25
valor_acucar = 1.10
valor_milho = 1.30
class gestao_cliente:
	def __init__(self, nome, data, pagamento, kilos_arroz, kilos_feijao, kilos_acucar, kilos_milho, gasto_cliente):
		self.nome = nome
		self.data = data
		self.pagamento = pagamento
		self.kilos_arroz = kilos_arroz
		self.kilos_feijao = kilos_feijao
		self.kilos_acucar = kilos_acucar
		self.kilos_milho = kilos_milho
		self.gasto_cliente = gasto_cliente
class gestao_graos:
	def __init__(self, quantidade_arroz, quantidade_feijao, quantidade_acucar, quantidade_milho, rendas, total_renda, valor_total):
		self.quantidade_arroz = quantidade_arroz
		self.quantidade_feijao = quantidade_feijao
		self.quantidade_acucar = quantidade_acucar
		self.quantidade_milho =  quantidade_milho
		self.rendas = rendas
		self.total_renda = total_renda
		self.valor_total = valor_total
# U---suário digitando quantos quilos tem de cada grão
quantidade_arroz = float(input("Digite a Quantidade de Arroz no Estoque: "))
quantidade_feijao = float(input("Digite a Quantidade de Feijão no Estoque: "))
quantidade_acucar = float(input("Digite a Quantidade de Açucar no Estoque: "))
quantidade_milho = float(input("Digite a Quantidade de Milho no Estoque: "))
rendas = float(input("Digite A renda Inicial do Comercio: "))
# A---dicionando na lista
gestao_gerente.append(gestao_graos(quantidade_arroz, quantidade_feijao, quantidade_acucar, quantidade_milho, rendas, 0, 0)) #Graos e Renda do Comercio.
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
		x.rendas = x.rendas - total_renda
		x.total_renda = total_renda
		print(f"O dinheiro Gasto em Arroz, Feijão, Açucar e Milho foi R${total_renda}")
		print(f"A renda agora é de R${x.rendas}")
		print("-+-+-+-+-+-+"*20)
#V---ERIFICANDO QUANTIDADE DE GRÂOS
def Verificar_graos():
	for x in gestao_gerente:
				print(f"Arroz {x.quantidade_arroz}Kg")
				print(f"Feijão {x.quantidade_feijao}Kg")
				print(f"Açucar {x.quantidade_acucar}Kg")
				print(f"Milho {x.quantidade_milho} Kg")
#F---UNÇÃO DO CLIENTE COMPRAR ARROZ:
def Comprar_Arroz():
	print("-+-+-+-+-+-+"*20)
	nome = str(input("Informe seu Nome: "))
	data = str(input("Informe a Data da compra: "))
	pagamento = str(input("Informe a forma de pagamento: [Pix ou Espécie] "))
	kilos_arroz = float(input("Informe a quantidade de Kilos Arroz comprados: "))
	print("-+-+-+-+-+-+"*20)
	gasto_cliente = kilos_arroz * valor_arroz
	for x in gestao_gerente:
		if kilos_arroz <= x.quantidade_arroz:
			x.quantidade_arroz = x.quantidade_arroz - kilos_arroz 
			x.rendas = x.rendas + gasto_cliente
			print("-+-+-+-+-+-+"*20)
			print(f"O total a ser Pago é: R${gasto_cliente}")
			print(f"A Quantidade de Arroz requirida foi: {kilos_arroz}Kg")
			print("-+-+-+-+-+-+"*20)   
			compradores.append(gestao_cliente(nome, data, pagamento, kilos_arroz, "", "", "", gasto_cliente))
		else:
			print(f"Sem quantidade de Estoque Suficiente para essa Quantidade \nTemos Apenas {x.quantidade_arroz}Kg em estoque")
			break
#F---UNÇÃO DO CLIENTE COMPRAR FEIJÂO
def Comprar_Feijao():
	print("-+-+-+-+-+-+"*20)
	nome = str(input("Informe seu Nome: "))
	data = str(input("Informe a Data da compra: "))
	pagamento = str(input("Informe a forma de pagamento: [Pix ou Espécie] "))
	kilos_feijao = int(input("Informe a quantidade de Kilos de Feijão comprados: "))
	print("-+-+-+-+-+-+"*20)
	gasto_cliente = kilos_feijao * valor_feijao 
	for x in gestao_gerente:
		if kilos_feijao <= x.quantidade_feijao:
			x.quantidade_feijao = x.quantidade_feijao - kilos_feijao 
			x.rendas = x.rendas + gasto_cliente
			print("-+-+-+-+-+-+"*20)
			print(f"O total a ser Pago é: R${gasto_cliente}")
			print(f"A Quantidade de Feijão requirida foi: {kilos_feijao}Kg")
			print("-+-+-+-+-+-+"*20)
			compradores.append(gestao_cliente(nome, data, pagamento, "", kilos_feijao, "", "", gasto_cliente))
		else:
			print(f"Sem quantidade de Estoque Suficiente para essa Quantidade \nTemos Apenas {x.quantidade_feijao}Kg em estoque")
			break
#F---UNÇÃO DO CLIENTE COMPRAR AÇUCAR
def Comprar_Acucar():
	print("-+-+-+-+-+-+"*20)
	nome = str(input("Informe seu Nome: "))
	data = str(input("Informe a Data da compra: "))
	pagamento = str(input("Informe a forma de pagamento: [Pix ou Espécie] "))
	kilos_acucar = int(input("Informe a quantidade de Kilos de Açucar comprados: "))
	print("-+-+-+-+-+-+"*20)
	gasto_cliente = kilos_acucar * valor_acucar
	for x in gestao_gerente:
		if kilos_acucar <= x.quantidade_acucar:
			x.quantidade_acucar = x.quantidade_acucar - kilos_acucar 
			x.rendas = x.rendas + gasto_cliente
			compradores.append(gestao_cliente(nome, data, pagamento, "", "", kilos_acucar, "", gasto_cliente))
			print("-+-+-+-+-+-+"*20)
			print(f"O total a ser Pago é: R${gasto_cliente}")
			print(f"A Quantidade de Açucar requirida foi: {kilos_acucar}Kg")
			print("-+-+-+-+-+-+"*20)
		else:
			print(f"Sem quantidade de Estoque Suficiente para essa Quantidade \nTemos Apenas {x.quantidade_acucar}Kg em estoque")
			break
#F---UNÇÃO DO CLIENTE COMPRAR MILHO
def Comprar_Milho():
	print("-+-+-+-+-+-+"*20)
	nome = str(input("Informe seu Nome: "))
	data = str(input("Informe a Data da compra: "))
	pagamento = str(input("Informe a forma de pagamento: [Pix ou Espécie] "))
	kilos_milho = int(input("Informe a quantidade de Kilos de Milho comprados: "))
	print("-+-+-+-+-+-+"*20)
	gasto_cliente = kilos_milho * valor_milho
	for x in gestao_gerente:
		if kilos_milho <= x.quantidade_milho:
			x.quantidade_milho = x.quantidade_milho - kilos_milho 
			x.rendas = x.rendas + gasto_cliente
			print("-+-+-+-+-+-+"*20)
			print(f"O total a ser Pago é: R${gasto_cliente}")
			print(f"A Quantidade de Milho requirida foi: {kilos_milho}Kg")
			print("-+-+-+-+-+-+"*20)
			compradores.append(gestao_cliente(nome, data, pagamento, "", "", "", kilos_milho, gasto_cliente))
		else:
			print(f"Sem quantidade de Estoque Suficiente para essa Quantidade \nTemos Apenas {x.quantidade_feijao}Kg em estoque")
			break
# ---FUNÇÃO PARa VERIFICAR HISTORICO DE VENDAS DOS CLIENTES
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
def Gestao_Cliente():
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
		print(f'Na semana houve lucro de R${lucro} ')
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
				print(f"O Saldo do Comercio e: R${x.rendas}")
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
			Gestao_Cliente()
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
# S---OLI DEO GLORIA ---#