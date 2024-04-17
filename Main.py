import Funciones

if __name__ == '__main__':
    Base = Funciones.leerBase()
    Cabe = Funciones.cabeceras()

    print("Favor de indicar su preferencia de Champagne en el siguiente orden:\nUva, País, Año, Precio(Dólares).\nEjemplo: Prosecco, Italy, 2019, 40") 
    pref = input()
    datos = pref.split(',')

    match = Funciones.matchPreference(datos,Base)
    print("Los Champagnes que le recomendamos son: ")
    print(match)
