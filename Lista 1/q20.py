#Q20. Efetuar o cálculo da quantidade de litros de combustível 
# gastos em uma viagem, sabendo-se que o carro faz 12 km 
# com um litro. Deverão ser fornecidos o tempo gasto na viagem 
# e a velocidade média.
#Utilizar as seguintes fórmulas:	
# distância = tempo x velocidade.
# litros usados = distância / 12
tempoGastoViagem = int(input("Digite o tempo gasto na viagem: "))
velocidadeMedia = int(input("Digite a velocidade média: "))
distancia = tempoGastoViagem * velocidadeMedia
litrosCombustivel = distancia / 12
print("Litros de combustível gastos: " + str(litrosCombustivel))