import numpy as np
import re, random
import math

"""
Vino   (4): Tinto, Blanco, Rosado, Espumoso
Reserva(5): Joven, Reserva, Gran Reserva, Roble, Sin Reserva
Cosecha(2): < 2000s, > 2000s
Precio (3): < $20,000-$10,000, $10,000-$4,000, $4,000 >
Uva    (7): Pinot Noir, Cabernet Sauvignon, Moscatel, Gewürztraminer, Glera,  Syrah, Merlot
Pais   (4): Francia, Italia, España, Alemania
"""

def leerBase():
	'''
	Funcion que leer una base de conocimiento y la transforma en un arreglo de filas
	'''
	datos = []
	archivo = open('BaseConocimiento.txt', 'r')  # Reemplaza 'nombre_archivo.txt' con la ruta y nombre de tu archivo
	try:
		next(archivo)
		for linea in archivo:
			aux = linea.rstrip('\n')
			newLinea = aux.split(',')
			newLinea = [s.lower() for s in newLinea]
			datos.append(newLinea)
	finally:
		archivo.close()
	return datos

def cabeceras():
	'''
	Funcion que regresa la primera columna de un archivo de conocimiento.
	'''
	archivo = open('BaseConocimiento.txt', 'r')  # Reemplaza 'nombre_archivo.txt' con la ruta y nombre de tu archivo
	try:
		aux = archivo.readline().rstrip('\n').split(',')
		aux = aux[1:]
	finally:
		archivo.close()
	#print(aux)
	return aux	

def totalAtributos(datos):
	'''
	Total de atributos del producto por cada producto. TA (Suma Fila).
	Conteo de cuantos atributos en total estamos tomando en cuenta para hacer nuestra recomendación.
	Columna de Total Atributos (Suma de las columnas de cada producto).
	'''
	atributos = []
	for linea in datos:
		count = 0
		for x in linea:
			if x == '1':
				count = count + 1
		atributos.append(float(count))
	return atributos

def normalizar(datos, TA):
	'''
	Funcion que normaliza la base de conocimiento.
	Normalizas los datos con respecto al total de atributos.
	Divide el atributo entre la raíz(Total Atributos).
	'''
	normalizado = []
	i = 0
	for linea in datos:
		product = []
		for x in linea[1:]:
			product.append(float(x)/math.sqrt(TA[i]))
		normalizado.append(product)
		i = i + 1
	return normalizado

def matchUserInput(like, dislike, conocimiento):
	'''
	Función para obtener en Vector Usuario, cuando al usuario le gusta un atributo es 1 si no le gusta el atributo es -1.
	Podemos hacer una deducción y trasladar las caracteristicas de este producto para predecir cuales otros le gustarían.
	'''
	pref = []
	for text in conocimiento:
		found = False
		for r in like:
			if r.strip().lower() == text.strip().lower():
				#print("MATCH:", r)
				pref.append(1.0)
				found = True
				break
		for r in dislike:
			if r.strip().lower() == text.strip().lower():
				#print("MATCH:", r)
				pref.append(-1.0)
				found = True
				break
		if not found:
			pref.append(0.0)
	return pref

def interesAtributo(norm, vect):
	'''
	Función que calcula los Intereses por Atributo que busca intereses positivos o negativos que se calculan a partir de un producto punto. 
	'''
	IpA = [0.0 for _ in range(len(norm[0]))]
	j = 0
	for linea in norm:
		for i, elem in enumerate(linea):
			IpA[i] += vect[j]*elem
		j += 1
	return IpA


def obtenerDF(conocimiento):
	'''
	Función para obtener DF que es el Total de apariciones (Frecuencia del termino el nuestra BaseConocimiento).
	Es la suma de columna, de la tabla original, cuantas veces aparece el atributo.
	'''
	df = [0 for _ in range(len(conocimiento[0])-1)]
	for linea in conocimiento:
		for i, elem in enumerate(linea[1:]):
			if elem == '1':
				df[i] += 1
	return df

def obtenerIDF(df,conocimiento):
	'''
	Función para obtener IDF (Inverso de la frecuencia que calculamos anteriormente).
	Formula: log(TotalProductos/DF) = Cercanos a 1 pero nunca es mayor a 1
	'''
	tp = len(conocimiento)
	idf = []
	for x in df:
		idf.append(math.log(tp/x))
	return idf



def prediccion(norm, idf, IpA):
	'''
	Función para calcular las predicciones con Producto Punto
	Formula: ProductoPunto(FilaNormalizada,IDF,IpA)
	IpA = Interes por Atributo
	'''
	pred = []
	for linea in norm:
		suma = 0.0
		for i, elem in enumerate(linea):
			suma += (elem*idf[i]*IpA[i])
		pred.append(suma)
	return pred


def matchPreference(like, pred, conocimiento):
	recomendado = []
	'''
	Calcular el angulo minimo entre el input, y la base de conocimiento
	'''
	match = 0.0
	for i, x in enumerate(pred):
		if conocimiento[i] in like:
			continue
		if x > match:
			recomendado = [conocimiento[i]]
			match = x
		elif x == match:
			recomendado.append(conocimiento[i])
	return recomendado