#Q25. Criar um algoritmo que leia o valor de um depósito e 
# o valor da taxa de juros. Calcular e imprimir o valor do 
# rendimento e o valor total depois do rendimento.
valor = float(input("Digite o valor do depósito: "))
taxa = float(input("Digite a taxa de juros: "))
rendimento = valor * (taxa / 100)
valorFinal = valor + rendimento
print("Valor do rendimento: " + str(rendimento))
print("Valor total depois do rendimento: " + str(valorFinal))