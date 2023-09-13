# Obtém a idade da pessoa
idade = int(input("Digite a idade da pessoa: "))

# Define as faixas etárias para classificação
limite_jovem = 25
limite_velho = 60

# Verifica a faixa etária da pessoa
if idade < limite_jovem:
    classificacao = "Jovem"
elif idade < limite_velho:
    classificacao = "Adulto"
else:
    classificacao = "Velho"

# Exibe a classificação
print(f"A pessoa é classificada como '{classificacao}'.")
