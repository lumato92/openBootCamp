class Vehiculo ():
	def __init__(self,color,ruedas,puertas):
		self.color=color
		self.ruedas=ruedas
		self.puertas=puertas


class Coche(Vehiculo):
	def __init__(self, arg):
		super(Vehiculo, self).__init__()
		self.arg = arg
		