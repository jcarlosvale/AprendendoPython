#Q22. Ler dois valores para as variáveis A e B, 
# efetuar a troca dos valores de forma que 
# a variável A passe a ter o valor da variável B 
# e que a variável B passe a ter o valor da variável A. 
# Apresentar os valores trocados.
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
aux = a
a = b
b = aux
print("Valor de A: " + str(a))
print("Valor de B: " + str(b))