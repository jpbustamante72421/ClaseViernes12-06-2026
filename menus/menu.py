from estructuras.lineales.lista_enlazada_simple import LinkedList

class MenuListaEnlazada(object):
    def __init__(self):
        self.lista_enlazada = LinkedList()

    def mostrar_menu(self):
        print("Menú de Lista Enlazada")
        print("1. Agregar inicio")
        print("2. Agregar final")
        print("3. Buscar")
        print("4. Mostrar lista")
        print("5. Eliminar Inicial")
        print("6. Eliminar Final")
        print("7. Salir")

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            elemento = input("Ingrese el elemento a agregar: ")
            self.lista_enlazada.insert_at_beginning(elemento)
            print(f"Elemento '{elemento}' agregado a la lista.")
        elif opcion == 2:
            elemento = input("Ingrese el elemento a agregar: ")
            self.lista_enlazada.insert_at_end(elemento)
            print(f"Elemento '{elemento}' eliminado de la lista.")
        elif opcion == 3:
            elemento = input("Ingrese el elemento a buscar: ")
            encontrado = self.lista_enlazada.search(elemento)
            if encontrado:
                print(f"Elemento '{elemento}' encontrado en la lista.")
            else:
                print(f"Elemento '{elemento}' no encontrado en la lista.")
        elif opcion == 4:
            print("Contenido de la lista enlazada:")
            self.lista_enlazada.print_linked_list()

        elif opcion == 5:
            elemento = input("Ingrese el elemento a eliminar: ")
            self.lista_enlazada.delete_at_beginning()
            print(f"Elemento '{elemento}' eliminado de la lista.")

        elif opcion == 6:
             elemento = input("Ingrese el elemento a eliminar: ")
             self.lista_enlazada.delete_at_end()
             print(f"Elemento '{elemento}' eliminado de la lista.")
        elif opcion == 7:
            print("Saliendo del menú.")
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

    def iniciar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = int(input("Seleccione una opción: "))
                if opcion == 7:
                    self.ejecutar_opcion(opcion)
                    break
                self.ejecutar_opcion(opcion)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")