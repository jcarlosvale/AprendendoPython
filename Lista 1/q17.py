#Q17. Em épocas de pouco dinheiro, 
# os comerciantes estão procurando aumentar suas vendas 
# oferecendo desconto. 
# Faça um algoritmo que possa entrar com o valor de um produto 
# e imprima o novo valor tendo em vista que o desconto foi de 9%.
num = int(input("Digite o valor do produto: "))
desconto = num * 0.09
valorFinal = num - desconto
print("Valor final: " + str(valorFinal))