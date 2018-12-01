from paquete_archivos.Archivos import ReadFichero, WriteFichero#importamos las clases para leer y escribir iicheros
from paquete_modelo.Alumno import Alumno#importar la clase alumno

f = ReadFichero()#iniciamos el lector del fichero con nombre f
f2= WriteFichero()#iniciamos la escritura del fichero con nnombre f2

lista = f.obtener_informacion()#agregamos al informacion del fichero al arreglo lista
lista = [l.split("|") for l in lista]# por cada posicion del arreglo lista realizamos un split con el carater especial "|"
lista=lista[1:]#Eliminamos la primera linea ya que corresponde al emcabezado

print("\n%15s\t\t%18s\n"%("ALUMNO","PROMEDIO"))#Imprimimos un emcabezado para el reporte

for o in lista:#recorremos cada posicion de la lista bajo el nombre de o (recuerde que o es el arreglo del split "|")
    a=Alumno(o[0], o[1], o[2], o[3])#tTomamos la informacion de cada posicion del arreglo o y la ingresamos en el constructor de ALUMNO
    print(a)#Imprimimos la informaicond el objeto(metodo STR)
    f2.agregar_informacion(a)#Agregamos la informacion al segundo fichero
f.cerrar_archivo()# cerramso el fichero  de lectura
f2.cerrar_archivo()# cerramos el fichero de escritura	