#SOLICITO AL USUARIO QUE INGRESE PESO Y ALTURA

altura= float(input("Ingrese su Altura en metros: "))
peso = float(input("Ingrese su Peso en kgs: "))

# Realizo el calculo utilizando la formula de IMC --> kg/m2

imc = (peso/(altura**2))

print(f'Su IMC es {imc:.2f}')