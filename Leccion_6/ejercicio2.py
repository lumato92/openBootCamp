#Creo clase que recibe 2 atributos
class Alumno:

	"""docstring for Alumno"""
	def __init__(self,nombre,nota ):
		self.nombre = nombre
		self.nota = nota 
	#Creo metodo que dice si esta aprobado o no
	def aprobado(self):
		return "Aprobado" if self.nota >= 7 else "Reprobado"
	def __str__(self):
		return f'Nombre: {self.nombre} Nota:{self.nota} Condicion: {"Aprobado" if self.nota >= 7 else "Reprobado"}'
	

al1=Alumno("Lucas",6)

print(al1.aprobado())