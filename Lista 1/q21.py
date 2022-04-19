#Q21. Efetuar o cálculo do valor de uma prestação em atraso, 
# utilizando a fórmula:
# prestação = valor + (valor*(taxa/100)*tempo)
valor = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros: "))
tempo = int(input("Digite o tempo de atraso: "))
prestacao = valor + (valor * (taxa / 100) * tempo)
print("Valor da prestação em atraso: " + str(prestacao))