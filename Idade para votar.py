# Obtém o ano de nascimento da pessoa
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade
ano_atual = 2023  # Ano atual (pode ser ajustado conforme necessário)
idade = ano_atual - ano_nascimento

# Verifica se a pessoa pode votar e obter a carteira de habilitação
pode_votar = idade >= 16
pode_dirigir = idade >= 18

# Exibe a idade e as verificações
print(f"A idade da pessoa é {idade} anos.")
if pode_votar:
    print("A pessoa pode votar, pois tem 16 anos ou mais.")
else:
    print("A pessoa não pode votar, pois tem menos de 16 anos.")
if pode_dirigir:
    print("A pessoa pode obter a Carteira de Habilitação, pois tem 18 anos ou mais.")
else:
    print("A pessoa não pode obter a Carteira de Habilitação, pois tem menos de 18 anos.")
