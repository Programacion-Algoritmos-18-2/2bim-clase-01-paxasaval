"""
	Importacion de la libreria codecs para evitaar conflicto con caracteres especiales
"""
import codecs

"""
Creamos una clase para la lectura de una fichero
"""
class ReadFichero:
	"""
	Inicialisamos la clase abriendo el archivo en la ubicacion establecidad
	"""
	def __init__(self):
		self.archivo=codecs.open("data\informacion.csv", "r")#Usamos open para abrir el fichero(ruta, y r para leer (read)

	"""
	Obtenemos la informacion del fichero y cada linea sera una posicion de un arreglo
	"""
	def obtener_informacion(self):
		return self.archivo.readlines()
	"""
	Cerrramos y Guardamos el Archivo
	"""	
	def cerrar_archivo(self):
		self.archivo.close()
"""
	Creamos una clases para escribir al final de un fichero en caso de no existir se lo crea
"""
class WriteFichero:
	"""
	Inicializamos la clase abriendo el archivo en la ruta deseada, en caso de no existir lo creamos
	"""
	def __init__(self):
		self.archivo = codecs.open("data/info_resumida.csv", "a")#Usamos open para abrir el fichero(ruta, y a para agregar al final del fichero (add)
		self.archivo.write("%s|%s\n"%("ALUMNO","PROMEDIO"))
	
	"""
	Tomamos un objeto del tipo alumno y exribimos el nombre y el promedio al final del nuevo fichero
	"""
	def agregar_informacion(self, a):
		self.archivo.write("%s|%2.f\n" % (a.nombre, a.obtener_promedio()))
	"""
	Cerramos y Guardadmo el nuevo fichero 
	"""
	def cerrar_archivo(self):
		self.archivo.close()
		print("\n\t***Fichero 2 Actualizado****\n")#mensaje que indica que se guardo el fichero