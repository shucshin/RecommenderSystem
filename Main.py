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

    '''Contiene los Nombres de los Vinos'''
    Nombres = []
    for x in Base:
        Nombres.append(x[0])

    '''Cabeceras'''
    Cabe = Funciones.cabeceras()

    '''Total Atributos'''
    TA = Funciones.totalAtributos(Base)

    '''Normalización'''
    norm = Funciones.normalizar(Base,TA)

    '''Vector Usuario'''
    vect = Funciones.matchUserInput(like,dislike,Nombres)

    '''Interes por Atributo'''
    IpA = Funciones.interesAtributo(norm, vect)

    '''DF'''
    df = Funciones.obtenerDF(Base)

    '''IDF'''
    idf = Funciones.obtenerIDF(df,Base)
    
    '''Predicción'''
    pred = Funciones.prediccion(norm, idf, IpA)

    '''Recomendación'''
    ans = Funciones.matchPreference(like, pred, Nombres)
    print("Los Vinos que le recomendamos son: ", end="")
    print(ans)