print('==='*8)
print("Para cada questão de acordo com o numero dela\nQuestão 1/2/3/4/5/6")
questoes = int(input('Digite de acordo com as opções acima '))
print('==='*8)

# ---questao 01   { Um banco só empresta dinheiro para quem tem o salário maior que R$ 2000 e a idade maior que 18 anos.}
if questoes == 1:
    print('==='*8)
    idade = int(input('Digite sua idade para o cadastro: '))
    salario = float(input('Digite o valor do seu salario: '))

    if idade >= 18 and salario >2000:
        print('Parabéns! você foi aprovado para o empréstimo')
        print('==='*8)
    else:
        print('Infelizmente você não foi aprovado para o empréstimo.') 
       
        print('==='*8)


# ---questao 02 {Leia dois números e que pergunte qual operação o usuário deseja realizar: 
# ---soma, subtração, divisão e multiplicação. Exiba o resultado da operação solicitada.}
elif questoes ==2:
    while True:
        print('==='*8)
        operacao = int(input('Digite e questoes o numero para a operação 1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão, 5-Sair '))
        if operacao ==1:
            print('==='*8)
            nume1 = float(input('Digite o primero numero '))
            nume2 = float(input('Digite o segundo numero '))
    
            print('==='*8)
            print(f"A soma dos números é:{nume1+nume2}")
    
        elif operacao ==2:
            print('==='*8)
            nume1 = float(input('Digite o primero numero '))
            nume2 = float(input('Digite o segundo numero '))
    
            print('==='*8)
            print(f"A subtração dos números é:{nume1-nume2}")
    
        elif operacao ==3:
            print('==='*8)
            nume1 = float(input('Digite o primero numero '))
            nume2 = float(input('Digite o segundo numero '))
    
            print('==='*8)
            print(f"A multiplicação dos números é:{nume1*nume2}")
    
        elif operacao ==4:
            print('==='*8)
            nume1 = float(input('Digite o primero numero '))
            nume2 = float(input('Digite o segundo numero '))
    
            print('==='*8)
            print(f"A divisão dos números é:{nume1/nume2}")    
        
        elif operacao ==5:
            print('Fim!')
            break    


 # ---questao 03   { Escreva um programa para analisar o financiamento bancário para compra de uma casa. 
 # ---O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior
 # ---a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar. De acordo com as informações inseridas, o programa deve dizer se o financiamento será aprovado ou não.}
elif questoes ==3:
    print('==='*8)
    print("Seja muito bem-vindo ao seu programa de consultoria de imovel, a seguir siga as instruções")
    valorimovel = float(input("Digite o valor do imovel desejado a ser adiquirido (Sem pontuação exemplo: 250000)"))
    salario = float(input('Digite o valor do seu salario mensal '))
    anos = int(input('Digite a quantidade de anos a serem pagos em prestações '))
    meses = anos * 12
    parcelas = valorimovel / meses
    porcentagem = (salario / 100) * 30

    if parcelas < porcentagem:
        print('Seu emprestimo foi aprovado.')
    else:
        print('Seu emprestimo não foi aprovado')


# ---questao 04 Escreva um programa que calcule o preço a pagar pela energia elétrica de um imóvel. Pergunte a quantidade de kwh consumida e o tipo do imóvel: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com as informações a seguir:
#    ---Residencial - Até 500 kWh (R$ 0,4 por 1 kWH); Acima de 500 kWh (R$ 0,65 por 1 kWH).
#    ---Comercial - Até 1000 kWh (R$ 0,55 por 1 kWH); Acima de 1000 kWh (R$ 0,6 por 1 kWH).
#    ---Industrial - Até 5000 kWh (R$ 0,55 por 1 kWH); Acima de 5000 kWh (R$ 0,62 por 1 kWH).
elif questoes ==4:

    print('==='*8)
    imovel = str(input('Digite o tipo do imovel   R-Residencial/ C-Comercial/ I-Industrial ').upper())
    kwhgastos = int(input('Digite quantos kWh foram gastos no mês: '))
    
    def residencial():
        print('====='*5)
        print("Imovel residencial")
        if kwhgastos <= 500:
         print(f"O total a pagar no mês é: {kwhgastos*0.40:.2f}")
        else :
         print(f"O total a pagar no mês é: {kwhgastos*0.65:.2f}")

    def comercial():
        print('====='*5)
        print("Imovel comercial")
        if kwhgastos <= 1000:
         print(f"O total a pagar no mês é: {kwhgastos*0.55:.2f}")
        else :
         print(f"O total a pagar no mês é: {kwhgastos*0.60:.2f}")


    def industrial():
        print('====='*5)
        print("Imovel industrial")
        if kwhgastos <= 5000:
         print(f"O total a pagar no mês é: {kwhgastos*0.55:.2f}")
        else :
         print(f"O total a pagar no mês é: {kwhgastos*0.62:.2f}")

    def switch(case):
        if case == "R":
            return residencial
        elif case == "C":
            return comercial
        elif case == "I":
            return industrial
    if __name__ == "__main__":
     function = switch(case=imovel)
    function()


# ---5. Crie um programa em que o usuário digite o seu email e o programa informe apenas o seu nome de usuário. 
elif questoes == 5:
    print('==='*8)
    email = input("Digite seu endereço de email: ")
    if '@' and '.' in email :
         print(f"Seu nome de usuário é: {email.split('@')[0]}")
    else:
        print("E-mail inválido.")


#questao 06   Crie um programa em que o usuário digite o seu email e o programa informe o seu provedor de email. 
elif questoes == 6:
        print('==='*8)
        email = input("Digite seu endereço de email: ")
        if '@' and '.' in email :
            print(f"Seu e-mail é provido por: {email.split('@')[1].split('.')[0]}") 
        else:
            print("E-mail inválido!")


# ---Escolha de questao inválida 
else: 
    print('Escolha Inválida.')