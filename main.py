hola = "hola"

lista = []


def altas():
    dic = {
        "Cod_Articulo": "",
        "Nombre": "",
        "Descripcion": "",
        "Precio": ""
    }
    cont = 2
    while cont != 0:
        cont = int(input("Pulse 0 para salir de Altas o un valor distinto de 0 para continuar: "))
        if cont == 0:
            break
        dic["Cod_Articulo"] = int(input("Introduzca el cod_articulo: "))
        dic["Nombre"] = input("Introduzca el Nombre: ")
        dic["Descripcion"] = input("Introduzca la Descripcion: ")
        dic["Precio"] = float(input("introduzca el Precio: "))
        lista.append(dic)
        print("¡Añadido!\n")


def bajas():



def mod():
    cont = 2
    while cont != 0:
        cont = int(input("Pulse 0 para salir de modificar o un valor distinto a 0 para continuar: "))
        if cont == 0:
            break


        v = int(input("Pulse 1 para modificar el nombre, \n"
                      "Pulse 2 para modificar la descripcion, \n"
                      "Pulse 3 para modificar el precio, \n"))
        match v :
            case 1:
                nombre = input("Introduce el nuevo nombre: ")
                pass
            case 2:
                des = input("Introduce la nueva descripcion: ")
                pass
            case 3:
                precio = input("Introduce el nuevo precio: ")

def bus():
    cont = 2
    while cont != 0:
        cont = int(input("Pulse 0 para salir de buscar o un valor distinto de 0 para continuar: "))
        if cont == 0:
            break
        cod = int(input("Introduce el cod_articulo a buscar: "))
        for i in lista:
            if i["Cod_Articulo"] == cod:
                str(i)
                print("\n")


def listar():
    for i in lista:
        str(i)

    print("\n")


def menu():
    print(
        "\n"
        "Pulse 0 para salir del programa.\n"
        "Pulse 1 para las altas.\n"
        "Pulse 2 para las bajas.\n"
        "Pulse 3 para las modificaciones.\n"
        "Pulse 4 para las busquedas.\n"
        "Pulse 5 para listar los datos.\n"
    )


def subMenu():
    cont = 2
    while cont != 0:
        cont = int(input())


def str(x):
    print("____________")
    for k, v in x.items():
        print("%s -> %s" % (k, v))


if __name__ == '__main__':
    opMenu = 6
    while opMenu != 0:

        menu()

        opMenu = int(input())

        match opMenu:
            case 1:
                altas()
                pass
            case 2:
                bajas()
                pass
            case 3:
                mod()
                pass
            case 4:
                bus()
                pass
            case 5:
                listar()
                pass
