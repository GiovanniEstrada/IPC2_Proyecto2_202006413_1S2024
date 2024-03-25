from tkinter import messagebox

from Nodos.NodoPosicion import NodoPosicion
from Clases.ClasePosicion import ClasePosicion
from Listas.ListaPosiciones import ListaPosiciones
from Listas.ListaResultados import ListaResultado
from Nodos.NodoResultado import NodoResultado
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
    
    def existePosicion(self, listaPosiciones, posicion):
        tmpListaPosiciones = listaPosiciones.cabeza

        while tmpListaPosiciones:
            if int(tmpListaPosiciones.valor.fila) == int(posicion.fila) and int(tmpListaPosiciones.valor.columna) == int(posicion.columna):
                return True
            tmpListaPosiciones = tmpListaPosiciones.siguiente


    def esObjetivo(self, posX, posY, objetivos):
        tmpObjetivos = objetivos
        while tmpObjetivos:
            if int(tmpObjetivos.valor.filaObjetivo) == int(posY) and int(tmpObjetivos.valor.columnaObjetivo) == int(posX):
                return True
            
            tmpObjetivos = tmpObjetivos.siguiente
        
        return False

    
    def validaPosicion(self, sigMovimiento, antMovimiento, Estructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos):

        limiteY = valFila
        limiteX = valColumna



        if int(sigMovimiento) == 1: # IZQUIERDA

            tmpEstructura = Estructura.anterior
            if int(posX) == 0 or str(tmpEstructura.valor) == "*" or int(antMovimiento) == 2:
                return False
            
            movimientoX = posX - 1
            movimientoY = posY

            clasePosicion = ClasePosicion(movimientoY, movimientoX)

            # SE VALIDA QUE NO VUELVA HACIA UNA MISMA POSICION
            if self.existePosicion(listaPosiciones, clasePosicion):
                return False
            
            if self.esObjetivo(movimientoX, movimientoY, objetivos):
                objetivosAlcanzados += 1

            nodoPosicion = NodoPosicion(clasePosicion)
            listaPosiciones.insertarPosicion(nodoPosicion)
            nodoMovimiento = NodoPosicion(sigMovimiento)
            listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)
        
        if int(sigMovimiento) == 2: # DERECHA

            tmpEstructura = Estructura.siguiente
            if int(posX) == int(limiteX) - 1 or str(tmpEstructura.valor) == "*" or int(antMovimiento) == 1:
                return False
            
            movimientoX = posX + 1
            movimientoY = posY
            clasePosicion = ClasePosicion(movimientoY, movimientoX)
            # SE VALIDA QUE NO VUELVA HACIA UNA MISMA POSICION
            if self.existePosicion(listaPosiciones, clasePosicion):
                return False
            
            if self.esObjetivo(movimientoX, movimientoY, objetivos):
                objetivosAlcanzados += 1
            
            nodoPosicion = NodoPosicion(clasePosicion)
            listaPosiciones.insertarPosicion(nodoPosicion)
            nodoMovimiento = NodoPosicion(sigMovimiento)
            listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)

        if int(sigMovimiento) == 3: # ABAJO
            
            if int(posY) >= int(limiteY) - 1 or int(antMovimiento) == 4:
                return False


            tmpEstructura = Estructura
            n = 0
            while n != int(limiteX):
                tmpEstructura = tmpEstructura.siguiente
                n += 1
            
            if str(tmpEstructura.valor) == "*":
                return False
            
            movimientoX = posX
            movimientoY = posY + 1
            clasePosicion = ClasePosicion(movimientoY, movimientoX)
            # SE VALIDA QUE NO VUELVA HACIA UNA MISMA POSICION
            if self.existePosicion(listaPosiciones, clasePosicion):
                return False
            
            if self.esObjetivo(movimientoX, movimientoY, objetivos):
                objetivosAlcanzados += 1
            
            nodoPosicion = NodoPosicion(clasePosicion)
            listaPosiciones.insertarPosicion(nodoPosicion)
            nodoMovimiento = NodoPosicion(sigMovimiento)
            listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)

        if int(sigMovimiento) == 4: # ARRIBA
            
            if int(posY) == 0 or int(antMovimiento) == 3:
                return False


            tmpEstructura = Estructura
            n = 0
            while n != int(limiteX):
                tmpEstructura = tmpEstructura.anterior
                n += 1

            if str(tmpEstructura.valor) == "*":
                return False
            
            movimientoX = posX
            movimientoY = posY - 1
            clasePosicion = ClasePosicion(movimientoY, movimientoX)
            # SE VALIDA QUE NO VUELVA HACIA UNA MISMA POSICION
            if self.existePosicion(listaPosiciones, clasePosicion):
                return False
            
            if self.esObjetivo(movimientoX, movimientoY, objetivos):
                objetivosAlcanzados += 1

            nodoPosicion = NodoPosicion(clasePosicion)
            listaPosiciones.insertarPosicion(nodoPosicion)
            nodoMovimiento = NodoPosicion(sigMovimiento)
            listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)

        if self.buscarPosiciones(tmpEstructura, movimientoX, movimientoY, listaPosiciones, limiteY, limiteX, contadorObjetivos, objetivosAlcanzados, objetivos):
            return True


    def buscarPosiciones(self, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos):
        if contadorObjetivos == objetivosAlcanzados:
            return True
        
        # SE VALIDA MOVIMIENTO HACIA LA IZQUIERDA
        if(self.validaPosicion(1, listaPosiciones.listaMovimientos.cola.valor, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos)):
            return True
        # SE VALIDA MOVIMIENTO HACIA LA DERECHA
        if(self.validaPosicion(2, listaPosiciones.listaMovimientos.cola.valor, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos)):
            return True
        # SE VALIDA MOVIMIENTO HACIA ABAJO
        if(self.validaPosicion(3, listaPosiciones.listaMovimientos.cola.valor, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos)):
            return True
        # SE VALIDA MOVIMIENTO HACIA ARRIBA
        if(self.validaPosicion(4, listaPosiciones.listaMovimientos.cola.valor, tmpEstructura, posX, posY, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, objetivos)):
            return True
        
        listaPosiciones.borrarPosicion()
        listaPosiciones.listaMovimientos.borrarPosicion()

    def resolverMaqueta(self, selMaqueta):
        if selMaqueta == "":
            messagebox.showerror("Error", "Por favor, seleccione una maqueta")
            return
        
        print(f"Maqueta seleccionada: {selMaqueta}")

        maqueta = self.cabeza

        while maqueta:
            if maqueta.valor.nombreMaqueta == selMaqueta:
                break
            maqueta = maqueta.siguiente

        if maqueta is None:
            messagebox.showerror("Error", "No se encontró la maqueta, vuelve a seleccionarlo")
            return
        
        filaInicio = maqueta.valor.entradaMaqueta.filaEntrada
        columnaInicio = maqueta.valor.entradaMaqueta.columnaEntrada
        valFila = maqueta.valor.filaMaqueta
        valColumna = maqueta.valor.columnaMaqueta

        # ENCONTRAMOS EL PUNTO DE INICIO
        tmpEstructura = maqueta.valor.estructuraMaqueta.cabeza
        i = 0
        j = 0 
        while tmpEstructura:
            
            if i == int(filaInicio) and j == int(columnaInicio):
                print(f"se encontró inicio en {i}x{j}")
                break

            if j == int(valColumna) - 1:
                i += 1
                j = 0
            else:
                j += 1
            tmpEstructura = tmpEstructura.siguiente


        # CONTADOR DE OBJETIVOS
        tmpObjetivos = maqueta.valor.objetivosMaqueta.cabeza
        contadorObjetivos = 0
        objetivosAlcanzados = 0
        while tmpObjetivos:
            contadorObjetivos += 1
            tmpObjetivos = tmpObjetivos.siguiente

        listaResultados = ListaResultado()
        listaPosiciones = ListaPosiciones()
        listaPosiciones.listaMovimientos = ListaPosiciones()
        nodoMovimiento = NodoPosicion(0)
        listaPosiciones.listaMovimientos.insertarPosicion(nodoMovimiento)
        self.buscarPosiciones(tmpEstructura, j, i, listaPosiciones, valFila, valColumna, contadorObjetivos, objetivosAlcanzados, maqueta.valor.objetivosMaqueta.cabeza)
        if listaPosiciones.cabeza == None:
            messagebox.showerror("Error", "Maqueta no tiene solución")