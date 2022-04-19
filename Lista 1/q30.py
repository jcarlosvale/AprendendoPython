#Q30. Criar um algoritmo que leia a quantidade de fitas que uma 
# locadora de vídeo possui e o valor que ela cobra por 
# cada aluguel, mostrando as informações pedidas a seguir:
#   Sabendo que um terço das fitas são alugadas por mês, 
#   exiba o faturamento anual da locadora;
#   Quando o cliente atrasa a entrega, 
#   é cobrada uma multa de 10% sobre o valor do aluguel. Sabendo 
#   que um décimo das fitas alugadas no mês são devolvidas 
#   com atraso, calcule o valor ganho com multas por mês;
#   Sabendo ainda que 2% de fitas se estragam ao longo do ano, 
#   e um décimo do total é comprado para reposição, 
#   exiba a quantidade de fitas que a locadora terá 
#   no final do ano
quantidadeDeFitas = int(input("Digite a quantidade de fitas: "))
valor = float(input("Digite o valor do aluguel: "))

faturamentoAnual = (quantidadeDeFitas // 3) * valor * 12
print("Faturamento anual: " + str(faturamentoAnual))

multas = (quantidadeDeFitas // 10) * valor * 1.1
print("Valor das multas: " + str(multas))

fitasQueEstragam = quantidadeDeFitas * 0.02
fitasCompradas = quantidadeDeFitas * 0.1
quantidadeDeFitasFinal = quantidadeDeFitas - fitasQueEstragam + fitasCompradas
print("Quantidade de fitas que a locadora terá no final do ano: " + str(quantidadeDeFitasFinal))