import Funciones

if __name__ == '__main__':
    Base = Funciones.leerBase()
    Cabe = Funciones.cabeceras()

    print("Favor de indicar su preferencia de Champagne en el siguiente orden:\nUva, País, Año, Precio(Dólares).\nEjemplo: Pinot Noir, France, 2014, 70") 
    pref = input()
    datos = pref.split(',')

    match = Funciones.matchPreference(datos,Base)
    print("El Champagne que le recomendamos es: ")
    print(match)
