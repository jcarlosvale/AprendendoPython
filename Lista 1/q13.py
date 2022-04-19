#Q13. Entrar com quatro números e imprimir a média ponderada, 
# sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))
num4 = int(input("Digite outro número: "))
mediaPonderada = (num1 * 1 + num2 * 2 + num3 * 3 + num4 * 4) / 10
print("Média Ponderada: " + str(mediaPonderada))