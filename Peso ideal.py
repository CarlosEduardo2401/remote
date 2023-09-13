# Solicita a altura e o sexo da pessoa
altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

# Calcula o peso ideal com base no sexo
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    genero = "masculino"
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    genero = "feminino"
else:
    print("Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")
    exit()

# Exibe o resultado
print(f"O peso ideal para uma pessoa de altura {altura:.2f} metros e sexo {genero} é aproximadamente {peso_ideal:.2f} quilogramas.")
