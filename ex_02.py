qtd = 0
soma = 0

while True:
    n = int(input("Número (0 sai): "))
    if n == 0:
        break
    soma = soma + n
    qtd = qtd + 1

if qtd > 0:
    media = soma / qtd
    print(f"Qtd: {qtd} | Soma: {soma}")
    print(f"Média: {media:.2f}")