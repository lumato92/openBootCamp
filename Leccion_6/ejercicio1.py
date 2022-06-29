
#Creo la clase vehiculo tiene como parametros color, ruedas, puertas
class Vehiculo ():
	def __init__(self,color,ruedas,puertas):
		self.color=color
		self.ruedas=ruedas
		self.puertas=puertas

	def __str__(self) -> str:
		return f'Color {self.color} , Cantidad de Ruedas: {self.ruedas} , Cantidad de puertas: {self.puertas}'

# creo la clase coche que hereda de vehiculo y le agrego los parametros velocidad y cilidrada
class Coche(Vehiculo):
	def __init__(self,color,ruedas,puertas,velocidad, cilindrada):
		self.color=color
		self.ruedas=ruedas
		self.puertas=puertas
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def __str__(self) -> str:
		return f'Color {self.color} , Cantidad de Ruedas: {self.ruedas} , Cantidad de puertas: {self.puertas} Velocidad: {self.velocidad}, Cilindrada: {self.cilindrada}'

c1=Coche('Azul',4,5,120,1200)		

print(c1)