import Funciones

if __name__ == '__main__':
    Base = Funciones.leerBase()
    Cabe = Funciones.cabeceras()

    # Solo para checar que lee el input bien
    print("Base")
    for x in Base:
        print(x)
    print("Cabeceras")
    print(Cabe)

    print("Favor de indicar su preferencia en la siguiente orden Marca,Talla,Color,Aumento(cm). Ejemplo: Nike,25,Negro,4") # Ejemplo: Nike,25,Negro,4
    pref = input()
    datos = pref.split(',')

    match = Funciones.matchPreference(datos,Base)
    print("El tennis que le recomendamos es: ")
    print(match)
