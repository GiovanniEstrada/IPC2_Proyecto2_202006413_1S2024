class ListaObjetivos:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarObjetivo(self, nodoObjetivo):
        
        if self.cabeza == None:
            self.cabeza = nodoObjetivo
            self.cola = nodoObjetivo
        else:
            nodoObjetivo.anterior = self.cola
            self.cola.siguiente = nodoObjetivo
            self.cola = nodoObjetivo

    def imprimeObjetivos(self):
        tmpNodoActual = self.cabeza
        while tmpNodoActual:
            print(f"     Nombre objetivo: {tmpNodoActual.valor.nombreObjetivo} | Posición: {tmpNodoActual.valor.filaObjetivo}x{tmpNodoActual.valor.columnaObjetivo}")
            tmpNodoActual = tmpNodoActual.siguiente
        return