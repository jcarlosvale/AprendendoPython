#Q26. Para vários tributos, a base de cálculo é o salário mínimo. 
# Fazer um algoritmo que leia o valor do salário mínimo e 
# o valor do salário de uma pessoa. 
# Calcular e imprimir quantos salários mínimos ela ganha.
salarioMinimo = float(input("Digite o valor do salário mínimo: "))
salario = float(input("Digite o valor do salário: "))
salarios = salario / salarioMinimo
print("Salários ganhos: " + str(salarios))