numero_inicial=int(input("Ingrese Numero inicial: "))
numero_final=int(input("Ingrese Numero final: "))
resultado=[]

while (numero_inicial > numero_final):
	numero_final=int(input(f"El numero debe ser mayor a {numero_inicial}: "))

for numero in range(numero_inicial,numero_final):
	if numero%2 != 0:
		resultado.append(numero)

print(resultado)