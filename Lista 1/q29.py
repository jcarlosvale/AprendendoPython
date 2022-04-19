#Q29. Uma pessoa resolveu fazer uma aplicação em uma 
# poupança programada. 
# Para calcular seu rendimento, 
# ela deverá fornecer o valor constante da aplicação mensal, 
# a taxa e o número de meses. 
# Sabendo-se que a fórmula usada para este cálculo é:
# rendimento = P * ((1 + taxa)**tempo - 1)/taxa
#   P = aplicação mensal;
#   i = taxa;
#   n = número de meses.
valorMensal = float(input("Digite o valor mensal da aplicação: "))
taxa = float(input("Digite a taxa de juros: "))
meses = int(input("Digite o número de meses: "))
rendimento = valorMensal * ((1 + taxa)**meses - 1)/taxa
print("Rendimento: " + str(rendimento))