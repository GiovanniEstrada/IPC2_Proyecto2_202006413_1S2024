class ListaEntradas:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarEntrada(self, nodoEntrada):
        
        if self.cabeza == None:
            self.cabeza = nodoEntrada
            self.cola = nodoEntrada
        else:
            nodoEntrada.anterior = self.cola
            self.cola.siguiente = nodoEntrada
            self.cola = nodoEntrada