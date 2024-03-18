class ListaMaquetas:

    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertarMaqueta(self, nodoMaqueta):
        
        if self.cabeza == None:
            self.cabeza = nodoMaqueta
            self.cola = nodoMaqueta
        else:
            nodoMaqueta.anterior = self.cola
            self.cola.siguiente = nodoMaqueta
            self.cola = nodoMaqueta

    def ordenarMaquetas(self):
        if self.cabeza == None:
            return
        
        tmpNodo1 = self.cabeza.siguiente

        while tmpNodo1:
            tmpValor = tmpNodo1.valor
            tmpNodoAnterior = tmpNodo1.anterior

            while tmpNodoAnterior != None and tmpNodoAnterior.valor.nombreMaqueta > tmpValor.nombreMaqueta:
                tmpNodoAnterior.siguiente.valor = tmpNodoAnterior.valor
                tmpNodoAnterior = tmpNodoAnterior.anterior

            if tmpNodoAnterior == None:
                self.cabeza.valor = tmpValor
            else:
                tmpNodoAnterior.siguiente.valor = tmpValor

            tmpNodo1 = tmpNodo1.siguiente

        return
    

    def imprimirMaquetas(self):
        tmpNodoActual = self.cabeza

        while tmpNodoActual:
            print("-------------------------------------------------")
            print(f"Nombre Maqueta: {tmpNodoActual.valor.nombreMaqueta}")
            print(f"Nro de filas: {tmpNodoActual.valor.filaMaqueta}")
            print(f"Nro de columnas: {tmpNodoActual.valor.columnaMaqueta}")
            print(f"Entrada de la maqueta: {tmpNodoActual.valor.entradaMaqueta.filaEntrada}x{tmpNodoActual.valor.entradaMaqueta.columnaEntrada}")
            print("     OBJETIVOS---------------------")
            tmpNodoActual.valor.objetivosMaqueta.imprimeObjetivos()
            tmpNodoActual.valor.estructuraMaqueta.imprimeEstructura(tmpNodoActual.valor.columnaMaqueta)
            tmpNodoActual = tmpNodoActual.siguiente
        return