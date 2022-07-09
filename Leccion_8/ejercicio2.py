import pickle


#Creo la clase vehiculo tiene como parametros color, ruedas, puertas
class Vehiculo ():
	def __init__(self,color,ruedas,puertas):
		self.color=color
		self.ruedas=ruedas
		self.puertas=puertas

	def __str__(self) -> str:
		return f' Color {self.color} , Cantidad de Ruedas: {self.ruedas} , Cantidad de puertas: {self.puertas}'



#Genero archivo nuevo binario 

with open("./Leccion_8/archivo2.bin","wb"):
    pass

#Instancio la clase vehiculo
auto=Vehiculo("Azul",4,5)


#Abro el archivo que generamos y le guardo el objeto 
with open("./Leccion_8/archivo2.bin","wb") as file:
    pickle.dump(auto,file)

#Cargo el archivo y extraigo el objeto guardado en el archivo
with open("./Leccion_8/archivo2.bin","rb") as file:
    auto2 = pickle.load(file)


print(auto2)