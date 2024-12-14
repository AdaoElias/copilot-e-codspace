# Solicita a operação desejada
# operacao = input("Digite a operação desejada (+, -, *, /): ")

# Solicita o número para a tabuada 
numero = float(input("Digite um número para a tabuada: ")) 

for fator in range(1,11):
    print(f"{numero} x {fator} = {numero*fator}".replace(".0", ""))

    #Usei o replace para excluir os zeros após o ponto.