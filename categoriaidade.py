# Obtém a idade do nadador
idade = int(input("Digite a idade do nadador: "))

# Determina a categoria com base na idade
if 5 <= idade <= 7:
    categoria = "Infantil"
elif 8 <= idade <= 10:
    categoria = "Juvenil"
elif 11 <= idade <= 15:
    categoria = "Adolescente"
elif 16 <= idade <= 30:
    categoria = "Adulto"
else:
    categoria = "Sênior"

# Exibe a categoria do nadador
print(f"O nadador de {idade} anos pertence à categoria {categoria}.")
