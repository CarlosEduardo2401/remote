# Solicita que o usuário insira as três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média aritmética das notas
media = (nota1 + nota2 + nota3) / 3

# Verifica a situação do aluno e determina a mensagem apropriada
if media >= 7.0:
    mensagem = "Aprovado"
elif media < 3.0:
    mensagem = "Reprovado"
else:
    # O aluno está em situação de exame
    nota_exame = 6.0 - media  # Calcula a nota necessária no exame para aprovação
    media_exame = (media + nota_exame) / 2  # Calcula a nova média após o exame
    if media_exame >= 5.0:
        mensagem = "Aprovado em exame"
    else:
        mensagem = "Reprovado em exame"

# Exibe a média e a mensagem
print(f"Média: {media:.2f}")
print(f"Situação: {mensagem}")


