from estructuras.no_lineales.expression_tree import ExpressionTree

def mostrar_menu():
    print("\nÁRBOL DE EXPRESIÓN")
    print("1. Ingresar expresión en notación postfija")
    print("2. Recorrido en Preorden (Prefija)")
    print("3. Recorrido en Inorden (Infija)")
    print("4. Recorrido en Posorden (Postfija original)")
    print("5. Evaluar expresión")
    print("6. Salir")

tree = ExpressionTree()  # Inicializa el contenedor del árbol de expresión

while True:
    mostrar_menu()
    option = input("Selecciona una opción: ")

    if option == "1":
        expresion = input("Ingresa la expresión postfija (separa los tokens con espacios, ej: A B + C *): ")
        tokens = expresion.split()
        if tokens:
            try:
                tree.build_expression_tree(tokens)
                print("Árbol de expresión construido exitosamente.")
            except Exception as e:
                print(f"Error al construir el árbol: {e}")
        else:
            print("La expresión no puede estar vacía.")

    elif option == "2":
        print("Recorrido en preorden (Prefija):")
        try:
            tree.preorden()
        except Exception as e:
            print(f"Primero debes construir el árbol. Error: {e}")

    elif option == "3":
        print("Recorrido en inorden (Infija):")
        try:
            tree.inorden()
        except Exception as e:
            print(f"Primero debes construir el árbol. Error: {e}")

    elif option == "4":
        print("Recorrido en posorden (Postfija):")
        try:
            tree.posorden()
        except Exception as e:
            print(f"Primero debes construir el árbol. Error: {e}")

    elif option == "5":
        print("Evaluación de la expresión:")
        try:
            resultado = tree.evaluar() 
            print(f"Resultado: {resultado}")
        except AttributeError:
            print("El método de evaluación no está implementado en la clase ExpressionTree.")
        except Exception as e:
            print(f"Error al evaluar: {e}")

    elif option == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")