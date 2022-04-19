#Q18. Ler uma temperatura em graus centígrados e 
# apresentá-la convertida em graus Fahrenheit. 
# A fórrmula de conversão é :
# F = (9 * C + 160) / 5
temperatura = int(input("Digite a temperatura em graus centígrados: "))
fahrenheit = (9 * temperatura + 160) / 5
print("Temperatura em Fahrenheit: " + str(fahrenheit))