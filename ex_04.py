primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))

resultado = 0
x = 1
while x <= segundo:
    resultado = resultado + primeiro
    x = x + 1

print(f"{primeiro} x {segundo} = {resultado}")