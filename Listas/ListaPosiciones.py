class ListaPosiciones:

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.movimientos = 0
        self.listaMovimientos = None

    def insertarPosicion(self, nodoPosicion):
        
        if self.cabeza == None:
            self.cabeza = nodoPosicion
            self.cola = nodoPosicion
        else:
            nodoPosicion.anterior = self.cola
            self.cola.siguiente = nodoPosicion
            self.cola = nodoPosicion

    def borrarPosicion(self):
        if self.cabeza == None:
            return
        
        if self.cabeza.siguiente == None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            actual.siguiente = None
            self.cola = actual

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