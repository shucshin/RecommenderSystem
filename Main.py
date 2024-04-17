import Funciones

if __name__ == '__main__':
    Base = Funciones.leerBase()
    Cabe = Funciones.cabeceras()

    for x in Base:
        print(x)
    print(Cabe)

    print("Favor de indicar su preferencia en la siguiente orden Marca,Talla,Color,Aumento(cm). Ejemplo: Nike,25,Negro,4") # Ejemplo: Nike,25,Negro,4
    pref = input()
    datos = pref.split(',')
    print(datos)

    match = Funciones.matchPreference(datos,Base)
    print(match)
