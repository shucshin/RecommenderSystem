import Funciones

if __name__ == '__main__':
    print("Favor de indicar los Vinos que le gusta:") 
    user = input()
    like = user.split(',')
    like = [s.lower() for s in like]
    print("Favor de indicar los Vinos que no le gusta:") 
    user = input()
    dislike = user.split(',')
    dislike = [s.lower() for s in dislike]

    Base = Funciones.leerBase()
    print("Base: ", end="")
    print(Base)

    '''Contiene los Nombres de los Vinos'''
    Nombres = []
    for x in Base:
        Nombres.append(x[0])

    '''Cabeceras'''
    Cabe = Funciones.cabeceras()

    '''Total Atributos'''
    TA = Funciones.totalAtributos(Base)
    print("TA: ", end="")
    print(TA)

    '''Normalización'''
    norm = Funciones.normalizar(Base,TA)
    print("Normalizado: ", end="")
    print(norm)

    '''Vector Usuario'''
    vect = Funciones.matchUserInput(like,dislike,Nombres)
    print("Vector Usuario: ", end="")
    print(vect)

    '''Interes por Atributo'''
    IpA = Funciones.interesAtributo(norm, vect)
    print("Interes por atributo: ", end="")
    print(IpA)

    '''DF'''
    df = Funciones.obtenerDF(Base)
    print("DF: ", end="")
    print(df)

    '''IDF'''
    idf = Funciones.obtenerIDF(df,Base)
    print("IDF: ", end="")
    print(idf)
    
    '''Predicción'''
    pred = Funciones.prediccion(norm, idf, IpA)
    print("Prediccion: ", end="")
    print(pred)

    '''Recomendación'''
    ans = Funciones.matchPreference(like, pred, Base)
    print("Respuesta: ", end="")
    print(ans)
"""
1. Conteo de cuantos atributos en total estamos tomando en cuenta para hacer nuestra
recomendación.
Columna de Total Atributos (Suma de las columnas de cada producto)
Recuento de cuantas caracteristicas vamos a tomar en cuenta

2. Hay productos que tienen más características que otros (más de un tipo de uva)
Concepto de Normalización: normalizar los datos con respecto al total de atributos
Dividir el atributo entre la raíz(Total Atributos)
So if there is 2 types of grape we count both and divide by total number of atributes
1+2+1+0 = 5/4 (4 atributes)

3. Crear un Usuario (Vector Usuario (1,0,-1,1,0,-1)), cuando al usuario le gusta un atributo es 1
si no le gusta el atributo es -1. Puede poner 4 preferencias de 6 (criterio que
vamos a suponer en base a la info que tenemos hasta ahorita).

Trasladar el interes en estos aspectos del producto, (si le gusta mario kart,
es nintendo, carreras, miscelaneo, carreras, E10+) Podemos hacer una deducción
y trasladar las caracteristicas de este producto para predecir cuales otros le gustarían.

4. Interes por Atributo: buscar intereses positivos o negativos que se calculan a partir 
de un producto punto. 
Marcar el producto punto de la categoria (columna) en la parte normalizada (Rojo)
con el Vector Usuario
Ejemplo: Para el usuario si no le gusta mario kart y la columna EA tiene valor de 0.4, entonces vale -0.4
si le gusta Minecraft y la columna EA tiene valor 0.7, vale +0.7 por lo que aportaría a que el final tenga +0.3

5. DF (Total de apariciones (Frecuencia del termino el nuestra BaseConocimiento))
Es la suma de columna, de la tabla original, cuantas veces aparece el atributo.

6. IDF (Inverso de la frecuencia que calculamos anteriormente)
- Formulazo: log(TotalProductos/DF) = Cercanos a 1 pero nunca es mayor a 1
TotalProductos = 6 en el excel de Link

7. Predicción
- Formulazo: ProductoPunto(FilaNormalizada,IDF,IpA) (2.,6.,4.)
IpA = Interes por Atributo
Cuando el usuario no ha asignado si le gusta o no:
- Negativo si contiene atributos que no le gustan al usuario
- Positivo en otro caso.
(Fila Normalizada es la fila roja de la tabla normalizada)
Asegurar que los 3 parámetros tengan la misma longitud (FilaNormalizada,IDF,IpA)

"""