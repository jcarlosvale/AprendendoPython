#Q23. Todo restaurante embora por lei não possa obrigar o cliente
# a pagar, cobra 10% para o garçom. 
# Fazer um algoritmo que leia o valor gasto 
# com despesas realizadas em um restaurante e 
# imprima o valor total com a gorjeta.
num = int(input("Digite o valor gasto: "))
gorjeta = num * 0.1
valorFinal = num + gorjeta
print("Valor final: " + str(valorFinal))