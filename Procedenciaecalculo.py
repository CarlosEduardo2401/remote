# Obtém o preço líquido e o código de origem do produto
preco_liquido = float(input("Digite o preço líquido do produto: "))
codigo_origem = int(input("Digite o código de origem (1 a 5): "))

# Determina a procedência e a taxa de imposto com base no código de origem
if codigo_origem == 1:
    procedencia = "Sul"
    taxa_imposto = 0.11
elif codigo_origem == 2:
    procedencia = "Norte"
    taxa_imposto = 0.13
elif codigo_origem == 3:
    procedencia = "Nordeste"
    taxa_imposto = 0.09
elif codigo_origem == 4:
    procedencia = "Centro-Oeste"
    taxa_imposto = 0.12
elif codigo_origem == 5:
    procedencia = "Sudeste"
    taxa_imposto = 0.18
else:
    print("Código de origem inválido. Use um código de 1 a 5.")
    exit()

# Calcula o preço final com base no imposto
imposto = preco_liquido * taxa_imposto
preco_final = preco_liquido + imposto

# Exibe a procedência, o imposto e o preço final
print(f"Procedência: {procedencia}")
print(f"Imposto ({taxa_imposto*100}%): R$ {imposto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
