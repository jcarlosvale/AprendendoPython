#Q14. Fazer um algoritmo que possa entrar com 
# o saldo de uma aplicação e imprima o novo saldo, 
# considerando o reajuste de 1%.
num = int(input("Digite o valor do saldo: "))
reajuste = num * 0.01
valorFinal = num + reajuste
print("Valor final: " + str(valorFinal))