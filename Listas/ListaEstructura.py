class ListaEstructura:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarEstructura(self, nodoEstructura):
        
        if self.cabeza == None:
            self.cabeza = nodoEstructura
            self.cola = nodoEstructura
        else:
            nodoEstructura.anterior = self.cola
            self.cola.siguiente = nodoEstructura
            self.cola = nodoEstructura

    def imprimeEstructura(self, columna):
        tmpNodoActual = self.cabeza

        i = 0
        fila = ""
        while tmpNodoActual:
            i += 1
            fila += f"|{tmpNodoActual.valor}|"
            if i == int(columna):
                print(fila)
                fila = ""
                i = 0
            tmpNodoActual = tmpNodoActual.siguiente