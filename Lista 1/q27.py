#Q27. Criar um algoritmo que leia o peso de uma pessoa, 
# só a parte inteira, calcular e imprimir:
# o peso da pessoa em gramas
# o novo peso em gramas se a pessoa engordar 12%
peso = int(input("Digite o peso: "))

pesoGramas = peso * 1000
print("Peso em gramas: " + str(pesoGramas))

pesoGramasEngordar = pesoGramas * 1.12
print("Peso em gramas após engordar 12%: " + str(pesoGramasEngordar))