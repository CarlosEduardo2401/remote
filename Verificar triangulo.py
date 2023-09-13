# Obtém os três valores X, Y e Z do usuário
x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))

# Verifica se os valores podem formar um triângulo
if x + y > z and x + z > y and y + z > x:
    # Verifica o tipo de triângulo
    if x == y == z:
        tipo_triangulo = "equilátero"
    elif x == y or x == z or y == z:
        tipo_triangulo = "isósceles"
    else:
        tipo_triangulo = "escaleno"

    # Exibe o tipo de triângulo
    print(f"Os valores {x}, {y} e {z} formam um triângulo {tipo_triangulo}.")
else:
    print("Os valores não podem formar um triângulo.")
