# Vamos solicitar uma palavra e um número e depois fazer com que a palavra apareça de acordo com o numero indicado.

#Solicitaçãoo da string
palavra = input("Digite uma palavra:")

#Solicitação do número
numero = int(input("Digite um número:"))

#Exibir a palavra n vezes de acordo com o número indicado
resultado = (palavra + '\n') * numero

print("Resultado: \n" , resultado)
