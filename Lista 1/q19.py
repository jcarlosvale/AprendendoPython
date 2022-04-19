#Q19. Calcular e apresentar o valor do volume de uma lata de óleo,
# utilizando a fórmula:
# volume = 3.14159 * R * R * altura.
# Você deve fornecer como entrada o raio R e a altura da lata.
R = float(input("Digite o raio da lata: "))
altura = float(input("Digite a altura da lata: "))
volume = 3.14159 * R * R * altura
print("Volume da lata: " + str(volume))