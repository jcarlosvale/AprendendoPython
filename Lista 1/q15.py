#Q15. Entrar com um número no formato CDU 
# e imprimir invertido: UDC. (Exemplo:123, sairá 321.) 
# O número deverá ser armazenado em outra variável 
# antes de ser impresso.
num = int(input("Digite um número: "))
centenas = num // 100;
dezenas = (num % 100) // 10;
unidades = num % 10;
numInvertido = unidades * 100 + dezenas * 10 + centenas;
print("Número invertido: " + str(numInvertido))
