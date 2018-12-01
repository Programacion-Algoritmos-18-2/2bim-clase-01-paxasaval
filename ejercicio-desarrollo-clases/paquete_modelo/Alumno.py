"""
Creamos un objeto del tipo Alumno
"""
class Alumno(object):
	"""
	Inicializamos el objeto con los atributos nombre, nota1, nota2 y nota3
	"""
	def __init__(self, n, n1, n2, n3):
		self.nombre=n
		self.nota1=int(n1)
		self.nota2=int(n2)
		self.nota3=int(n3)
	"""
	Set y Get para Nombre
	"""
	def setNombre(self, n):#Agregar Nombre
		self.nombre = n
	def getNombre(self):#Devolver Nombre
		return self.nombre
	"""
	Set y Get para Nota1
	"""
	def setNota1(self,n1):#Agregar nota 1
		self.nota1=int(n1)
	def getNota1(self):# Devolver nota 1
		return self.nota1
	"""
	Set y Get para Nota2
	"""
	def setNota2(self, n2):# Agregar nota 2
		self.nota2=int(n2)
	def getNota2(self,):# Devolver nota 2
		return self.nota2
	"""
	Set y Get para Nota3
	"""
	def setNota3(self, n3):#Agregaar nota 3
		self.nota3=int(n3)
	def getNota3(self,):#Devolver nota 3
		return self.nota3
	"""
	MEtodo para calcular el promedio en base al get de las 3 notas
	"""
	def obtener_promedio(self):# Calcular el promedio usando los obtener notas
		return (self.getNota1()+self.getNota2()+self.getNota3())/3#Devolvemos el promedio alculado
	
	def __str__(self):#metodo para presentar lso datos de un objetos similar al toString de JAVA
		return "%20s\t%15d "%(self.nombre, self.obtener_promedio())
		
		