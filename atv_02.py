# Inicío

deposito = float(input("Digite seu deposito "))
taxa = float(input("Digite o valor da taxa "))
mes = 1
saldo = deposito

while mes <= 24: 
    rendimento = saldo * (taxa / 100)
    saldo = saldo + rendimento
    print(f"Mes: {mes} Saldo: {saldo}", end=")
    mes = mes + 1

total_juros = saldo - deposito
print(f"total juros: {total_juros}")