# Solicita a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Solicita o número para a tabuada
numero = int(input("Digite um número para a tabuada: "))

# Gera a tabuada de 0 até 10
print(f"Tabuada do {numero} ({operacao}):")
for i in range(11):
    if operacao == '+':
        resultado = numero + i
    elif operacao == '-':
        resultado = numero - i
    elif operacao == '*':
        resultado = numero * i
    elif operacao == '/':
        # Adiciona uma verificação para evitar divisão por zero
        if i != 0:
            resultado = numero / i
        else:
            resultado = "Indefinido"
    else:
        resultado = "Operação inválida!"
        break
    print(f"{numero} {operacao} {i} = {resultado}")
