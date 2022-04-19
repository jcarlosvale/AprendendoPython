#Q12. Entrar com dois numeros inteiros 
# e imprimir a seguinte saída, da divisão entre eles:
# dividendo
# divisor
# quociente
# resto
num1 = int(input("Digite um número: "))	
num2 = int(input("Digite outro número: "))
dividendo = num1;
divisor = num2;
quociente = num1 // num2
resto = num1 % num2

print("Dividendo: " + str(dividendo))
print("Divisor: " + str(divisor))
print("Quociente: " + str(quociente))
print("Resto: " + str(resto))