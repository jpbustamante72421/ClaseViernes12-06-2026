from estructuras.lineales.lista_enlazada_simple import Linkedlist

def main():
    lista = Linkedlist()
    lista.insert_at_beginning(10)
    lista.insert_at_beginning(20)   
    lista.insert_at_beginning(30)
    lista.print_linked_list()

if __name__ == "__main__":  
    main()