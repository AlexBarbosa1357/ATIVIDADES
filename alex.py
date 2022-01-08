print("escolha de acordo com as seguintes opções.")

escolha = int(input('1-area e volume do cilindro, 2-perímetro e a superfície de um retângulo, 3-salario bruto e liquido: '))

#  questao-01 

if escolha == 1:
    raio = float(input('digite o valor equivalente ao raio do cilindro:'))
    altura = float(input('digite o valor equivalente a altura do cilindro:'))
    area = 2*3.14*(raio*raio)
    volume = 3.14*(raio*raio)*altura
    print(f'De acordo com os dados inseridos o valor da area é {area}, ja o valor do volume é {volume}')

# questao-02
elif escolha == 2:
    base = float(input("Digite o valor da base do retangulo: "))
    altura = float(input("Digite o valor da altura do retangulo: "))
    perimetro = 2*(base + altura)
    superfice = base*altura
    print(f"Com os valores inseridos temos que a superficie é {superfice} e perimetro é {perimetro}")

# questao-03
elif escolha == 3:
    horasmes = float(input('Digite o total de horas trabalhadas no mês '))
    ganhora = float(input("valor em R$ por hora trabalhada "))
    bruto = horasmes * ganhora

# condicionais para subtrair o valor adequado do INSS


    if bruto < 1.039:

        
        inss = bruto * (7.5/100)
        sLiq = bruto  - inss

        print(f"Salário bruto: {bruto}")
        print(f"Salário líquido: R${sLiq}")

    elif (bruto >= 1.039  <= 2.089,60):

        
        inss = bruto * (9/100)
        sLiq = bruto  - inss

        print(f"Salário bruto: {bruto}")
        print(f"Salário líquido: R${sLiq}")

    elif (bruto >= 2.089,61     <= 3.134,40 ) :
        
        inss = bruto * (9/100)
        sLiq = bruto  - inss

        print(f"Salário bruto: {bruto}")
        print(f"Salário líquido: R${sLiq}")


    else:          
        inss = bruto * (14/100)
        sLiq = bruto  - inss

        print(f"Salário bruto: {bruto}")
        print(f"Salário líquido: R${sLiq}")

    
    