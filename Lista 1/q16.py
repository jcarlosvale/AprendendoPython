#Q16. Entrar com a base e a altura de um retângulo 
# e imprimir a seguinte saída: perímetro e área
base = int(input("Digite a base do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
perimetro = 2 * (base + altura)
area = base * altura
print("Perímetro: " + str(perimetro))
print("Área: " + str(area))