def ejercicio1():
    lista=["P", "y"]
    lista_aux=list("python")
    for i in range (len(lista), len(lista_aux)):
        lista.append(lista_aux[i])
    print(lista)
#Metemos la palabra python en una lista auxiliar, después, añadimos a la lista loa elementos que no se encuentran en ella.
#Comenzaremos en la posición final de la lista y terminaremos en la posición final de la lista auxiliar, con la función .append iremos añadiendo los elementos.

def ejercicio2():
    lista = [1, 4, 2, 5, 4, 3, 4, 7, 5, 8, 9]
    lista=lista[1:6:2]
    print (lista)
#Guardamos en la lista unicamente los valores que van del 1 al 6, de dos en dos, es decir, los de la posición 1,3 y 5.

def main():
    ejercicio1()
    ejercicio2()

if __name__=='__main__':
    main()
