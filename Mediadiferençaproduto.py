# Obtém dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Exibe as opções para o usuário
print("Escolha a operação desejada:")
print("1. Média entre os números digitados")
print("2. Diferença do maior pelo menor")
print("3. Produto entre os números digitados")
print("4. Divisão do primeiro pelo segundo")

# Obtém a escolha do usuário
escolha = int(input("Digite o número da operação desejada: "))

# Realiza a operação escolhida e exibe o resultado
if escolha == 1:
    media = (numero1 + numero2) / 2
    print(f"A média entre {numero1} e {numero2} é {media:.2f}")
elif escolha == 2:
    diferenca = abs(numero1 - numero2)
    print(f"A diferença entre o maior e o menor número é {diferenca:.2f}")
elif escolha == 3:
    produto = numero1 * numero2
    print(f"O produto entre {numero1} e {numero2} é {produto:.2f}")
elif escolha == 4:
    if numero2 == 0:
        print("Não é possível dividir por zero.")
    else:
        divisao = numero1 / numero2
        print(f"A divisão de {numero1} pelo {numero2} é {divisao:.2f}")
else:
    print("Opção inválida. Escolha um número de 1 a 4 para a operação desejada.")
