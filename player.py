import random

class Nodo():
    def __init__(self, nombre = None, moneda = None, carta = None, anterior = None, siguiente = None):
        self.nombre = nombre
        self.moneda = moneda
        self.carta = carta
        self.anterior = anterior
        self.siguiente = siguiente

class LinkedList:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.contador = 0
        self.banco = 100
        self.carta1 = 'Juez'
        self.carta2 = 'Obispo'
        self.carta3 = 'Rey'
        self.carta4 = 'Bufon'
        self.carta5 = 'Reina'
        self.carta6 = 'Ladron'
        self.carta7 = 'Bruja'
        self.carta8 = 'Espia'
        self.carta9 = 'Campesino'
        self.carta10 = 'Tahur'
        self.carta11 = 'Inquisidor'
        self.carta12 = 'Viuda'

    def agregarInicio(self,nombre,moneda,carta):
        if(self.validar()):
            nuevo = Nodo(nombre,moneda,carta,None,None)
            self.inicio = nuevo
            self.fin = nuevo
        else:
            nuevo = Nodo(nombre,moneda,carta,None,self.inicio)
            self.inicio.anterior = nuevo
            self.inicio = nuevo

    def agregar(self, rep):
        #asignacion de las cartas extras en caso de que sean de 4 a 5 jugadores
        if rep == 4:    
            tiposcartasx = random.choice([self.carta1,self.carta2,self.carta3,self.carta5,self.carta6,self.carta10])
            nombre = "carta1"
            moneda = 0
            carta = tiposcartasx
            self.agregarInicio(nombre,moneda,carta)
            tiposcartasx2 = random.choice([self.carta1,self.carta2,self.carta3,self.carta5,self.carta6,self.carta10])
            nombre = "carta2"
            moneda = 0
            carta = tiposcartasx2
            self.agregarInicio(nombre,moneda,carta)
        elif rep == 5:
            tiposcartasx = random.choice([self.carta1,self.carta2,self.carta3,self.carta5,self.carta6,self.carta10])
            nombre = "carta1"
            moneda = 0
            carta = tiposcartasx
            self.agregarInicio(nombre,moneda,carta)
        while self.contador != rep:
            #configuraciones de las cartas segun la cantidad de jugadores
            if rep == 4:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta5,self.carta6,self.carta10])
            elif rep == 5:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta5,self.carta6,self.carta10])
            elif rep == 6:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta5,self.carta7,self.carta10])
            elif rep == 7:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta5,self.carta6,self.carta7,self.carta8])
            elif rep == 8:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta4,self.carta5,self.carta7,self.carta9])
            elif rep == 9:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta4,self.carta5,self.carta7,self.carta9,self.carta10])
            elif rep == 10:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta4,self.carta5,self.carta7,self.carta8,self.carta9,self.carta10])
            elif rep == 11:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta4,self.carta5,self.carta7,self.carta8,self.carta9,self.carta10,self.carta11])
            elif rep == 12:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta4,self.carta5,self.carta7,self.carta8,self.carta9,self.carta10,self.carta11,self.carta12])
            elif rep == 13:
                tiposcartas = random.choice([self.carta1,self.carta2,self.carta3,self.carta4,self.carta5,self.carta6,self.carta7,self.carta8,self.carta9,self.carta10,self.carta11])
            
            nombre = input("Digite su nombre: ")
            moneda = 6
            carta = tiposcartas
            temp = self.inicio
            while temp != None:
                if temp.nombre == nombre:
                    print("Error, este nombre ya existe", nombre)
                    temp = temp.anterior
                    self.eliminar(nombre)
                    break
                temp = temp.siguiente
            self.agregarInicio(nombre,moneda,carta)
            self.contador += 1

    def iterar(self):
        actual = self.inicio
        while actual:
            nombre = actual.nombre
            actual = actual.siguiente
            yield nombre    

    def __getitem__(self, indice):
        if indice >= 0 and indice <= self.contador:
            actual = self.inicio
            for _ in range(indice - 1):
                actual = actual.siguiente
            return actual.nombre
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')

    def eliminar(self, nombre):
        actual = self.inicio
        eliminado = False
        if actual is None:
            eliminado = False
        elif actual.nombre == nombre:
            self.inicio = actual.nombre
            self.inicio.anterior = None
            eliminado = True
        elif self.fin.nombre == nombre:
            self.fin = self.fin.anterior
            self.fin.siguiente = None
            eliminado = True
        else:
            while actual:
                if actual.nombre == nombre:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    eliminado = True
                actual = actual.siguiente
        if eliminado:
            self.contador -= 1

    def vercarta(self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre  == name:
                print("\nCarta: ", temp.carta)
            temp = temp.siguiente
        return

    def intercambiar(self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre == name:
                cartaux = temp.carta
            temp = temp.siguiente
        name2 = input("Con quien desea intercambiar la carta?: ")
        temp = self.inicio
        while temp != None:
            if temp.nombre == name2:
                cartaux2 = temp.carta
                temp.carta = cartaux
            temp = temp.siguiente
        temp = self.inicio
        while temp != None:
            if temp.nombre == name:
                temp.carta = cartaux2
            temp = temp.siguiente

    def Juez(self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre == name:
                temp.moneda = temp.moneda+3
                self.banco -=3
            temp = temp.siguiente          

    def Rey(self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre == name:
                temp.moneda = temp.moneda+3
                self.banco -=3
            temp = temp.siguiente

    def Reina(self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre == name:
                temp.moneda = temp.moneda+2
                self.banco -=2
            temp = temp.siguiente

    def Ladron(self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre == name:
                name2 = self.__getitem__(indice-1)
                temp = self.inicio
                while temp != None:
                    if temp.nombre == name2:
                        temp.moneda-=1
                    temp = temp.siguiente
                name3 = self.__getitem__(indice+1)
                temp.self.inicio
                while temp != None:
                    if temp.nombre == name3:
                        temp.moneda-=1
                    temp = temp.siguiente
                temp.moneda += 2    
            temp = temp.siguiente

    def Tahur(self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre == name:
                if temp.moneda >=10:
                    temp.moneda = 13
            temp = temp.siguiente

    def Obispo(self):
        return print("en obras")
    
    def eleccion (self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre  == name:
                if temp.carta == self.carta1:
                    self.Juez(indice)
                elif temp.carta == self.carta2:
                    self.Obispo()
                elif temp.carta == self.carta3:
                    self.Rey(indice)
                elif temp.carta == self.carta5:
                    self.Reina(indice)
                elif temp.carta == self.carta6:
                    self.Ladron(indice)
                elif temp.carta == self.carta10:
                    self.Tahur(indice)
                
            temp = temp.siguiente
        return

    def imprimirmoneda(self,indice):
        name = self.__getitem__(indice)
        temp = self.inicio
        while temp != None:
            if temp.nombre == name:
                print("Moneda: ",str(temp.moneda))
            temp = temp.siguiente

    def imprimir(self):
        temp = self.inicio
        while temp != None:
            print (temp.nombre , str(temp.moneda) , temp.carta)
            temp = temp.siguiente

    def validar(self):
        if(self.inicio==None):
            return True
        return False
