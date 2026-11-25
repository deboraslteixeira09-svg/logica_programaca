# Início

divida_inicial = float(input ("Qual o valor da divida?"))
taxa = float(input ("Qual o valor da taxa?"))
pagamento_mensal = float(input ("Qual o valor da mensalidade?"))

print(f"O valor da divida inicial é: {divida_inicial}")

juros_primeiro_mes = divida_inicial * (taxa/100)

while pagamento_mensal <= juros_primeiro_mes:
    mes = 0
    divida = divida_inicial
    total_pago = 0.0

    if divida > 0:
        juros = divida*(taxa/100)
        divida = divida + juros
        mes = mes + 1

        if 