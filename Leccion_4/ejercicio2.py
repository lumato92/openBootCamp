numero_inicial=int(input("Ingrese Numero inicial: "))
numero_final=int(input("Ingrese Numero final: "))

for numero in range(numero_inicial,numero_final):
	if numero%2 != 0:
		print(numero)
	