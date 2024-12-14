
# Informe os numeros desejados para efetar a operação
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

# Solicita a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2
else:
    resultado = "Indefinido"
        
print("Resultado:" ,resultado)
