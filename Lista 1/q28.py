#Q28. Criar um algoritmo que leia um número entre ZERO e 60 
# e imprimir o seu sucessor, sabendo que o sucessor de 60 é ZERO.
# Não pode ser utilizado nenhum comando de seleção e 
# nem de repetição
num = int(input("Digite um número entre 0 e 60: "))
sucessor = (num + 1) % 61
print("Sucessor: " + str(sucessor))