# Lê dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifica qual é o menor número
if numero1 < numero2:
    menor_numero = numero1
else:
    menor_numero = numero2

# Exibe o menor número
print("O menor número é:", menor_numero)
