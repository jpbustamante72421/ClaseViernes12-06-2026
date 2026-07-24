from estructuras.no_lineales.binary_tree import BinaryTree

def mostrar_menu():
    print("\nÁRBOL BINARIO DE BÚSQUEDA")
    print("1. Insertar un valor")
    print("2. Buscar un valor")
    print("3. Recorrido en preorden")
    print("4. Recorrido en inorden")
    print("5. Recorrido en posorden")
    print("6. Contar nodo")
    print("7. Salir")

tree = BinaryTree()

while True:
    mostrar_menu()
    option = input("Selecciona una opción: ")

    if option == "1":
        try:
            value = int(input("Ingresa el valor que deseas insertar: "))
            tree.insertar(value)
            print("Operación realizada.")
        except ValueError:
            print("Debes ingresar un número entero.")

    elif option == "2":
        try:
            value = int(input("Ingresa el valor que deseas buscar: "))
            if tree.buscar(value):
                print("El valor se encuentra en el árbol.")
            else:
                print("El valor no se encuentra en el árbol.")
        except ValueError:
            print("Debes ingresar un número entero.")
    
    elif option == "3":
        print("Recorrido en preorden:")
        tree.preorden()

    elif option == "4":
        print("Recorrido en inorden:")
        tree.inorden()

    elif option == "5":
        print("Recorrido en posorden:")
        tree.posorden()

    elif option == "6":
        print(tree.contar())
        
    elif option == "7":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
