from player import LinkedList

lista = LinkedList()
print("----Mascarade----\n")
nplayer = int(input("Introduzca la cantidad de jugadores: "))
lista.agregar(nplayer)
lista.imprimir()
a = 0
while a != 1:
    i = nplayer
    while i != 0:     
        print("---------------------------")
        print("\nTurno del jugador: ",lista[i])
        lista.imprimirmoneda(i)    
        print("\nEliga que accion desea hacer")
        print("1.mirar\n")
        print("2.Intercambiar\n")
        print("3.Anunciar\n")
        opc  = int(input("Ingrese el numero: "))
        if opc == 1:
            lista.vercarta(i)
        elif opc ==2:
            lista.intercambiar(i)
        elif opc ==3:
            lista.eleccion(i)
            '''
            opcr = input("Ingrese el nombre de la carta: ")
            if opcr == "Juez":
                lista.Juez(i)
            elif opcr == "Obispo":
                lista.Obispo()
            elif opcr == "Rey":
                lista.Rey(i)
            elif opcr == "Reina":
                lista.Reina(i)
            elif opcr == "Ladron":
                lista.Ladron(i)
            elif opcr == "Tahur":
                lista.Tahur(i)
                '''
        i-=1 

print("Presione cualquiere valor menos 1 para seguir: ")
a = int(input())
