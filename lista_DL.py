#Lista doblemente enlazada

class Nodo():

    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

    def verNodo(self):
        return self.info

class ListaDoblementeE():
    #Creamos la lista doblemente enlazada
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    #Comprobamos si esta vacia
    def vacia(self):
        return self.primero == None

    #Agregamos al final un elemento
    def Agregar_Final(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo 
            self.ultimo = aux.siguiente = Nodo(dato) #Ultimo nodo se convierte en el nuevo nodo
            self.ultimo.anterior = aux 

        self.tamanio += 1

    def Agregar_Inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux

        self.tamanio += 1

    def Eliminar_principio(self):
        if self.vacia():
            print("Esta vacio")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.tamanio = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.tamanio -= 1

    def Eliminar_final(self):
        if self.vacia():
            print("Esta vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.tamanio = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.tamanio -= 1


    def Recorrer_LDE(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente

    def Recorrer_LDE_Alreves(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior

        