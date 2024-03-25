# LIBRERIAS PYTHON
from xml.dom import minidom
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

# Importación de listas
from Listas.ListaEntradas   import ListaEntradas
from Listas.ListaMaquetas   import ListaMaquetas
from Listas.ListaObjetivos  import ListaObjetivos
from Listas.ListaEstructura import ListaEstructura

# importación de nodos
from Nodos.NodoEntrada  import NodoEntrada
from Nodos.NodoMaqueta  import NodoMaqueta
from Nodos.NodoObjetivo import NodoObjetivo
from Nodos.NodoEstructura import NodoEstructura

# importación de clases
from Clases.ClaseEntrada import ClaseEntrada
from Clases.ClaseMaqueta import ClaseMaqueta
from Clases.ClaseObjetivo import ClaseObjetivo


def lectorXML(listaMaquetas):
    urlArchivo = filedialog.askopenfile(filetype=[('XML files', '*.xml')])
    if not urlArchivo:
        print("Fallo an intentar cargar el archivo, vuelve a intentarlo")
        return
    
    listaMaquetas.cabeza = None
    listaMaquetas.cola = None
    xml = minidom.parse(urlArchivo)
    maquetas = xml.getElementsByTagName('maqueta')

    for i in maquetas:
        print(i.getElementsByTagName('nombre')[0].firstChild.data)
        print(i.getElementsByTagName('filas')[0].firstChild.data)
        print(i.getElementsByTagName('columnas')[0].firstChild.data)
        print(i.getElementsByTagName('estructura')[0].firstChild.data)
        entrada = ClaseEntrada(i.getElementsByTagName('fila')[0].firstChild.data, 
                               i.getElementsByTagName('columna')[0].firstChild.data)
        print(entrada.filaEntrada)
        print(entrada.columnaEntrada)
        listaObjetivos = ListaObjetivos()
        objetivos = i.getElementsByTagName('objetivos')[0].getElementsByTagName('objetivo')
        for objetivo in objetivos:
            print(objetivo.getElementsByTagName('nombre')[0].firstChild.data)
            print(objetivo.getElementsByTagName('fila')[0].firstChild.data)
            print(objetivo.getElementsByTagName('columna')[0].firstChild.data)
            claseObjetivo = ClaseObjetivo(objetivo.getElementsByTagName('nombre')[0].firstChild.data,
                                          objetivo.getElementsByTagName('fila')[0].firstChild.data,
                                          objetivo.getElementsByTagName('columna')[0].firstChild.data)
            nodoObjetivo = NodoObjetivo(claseObjetivo)
            listaObjetivos.insertarObjetivo(nodoObjetivo)
        
        estructura = i.getElementsByTagName('estructura')[0].firstChild.data
        listaEstructura = ListaEstructura()
        for j in estructura:
            if j == ' ':
                continue
            nodoEstructura = NodoEstructura(j)
            listaEstructura.insertarEstructura(nodoEstructura)

        claseMaqueta = ClaseMaqueta(i.getElementsByTagName('nombre')[0].firstChild.data,
                                    i.getElementsByTagName('filas')[0].firstChild.data,
                                    i.getElementsByTagName('columnas')[0].firstChild.data,
                                    entrada,
                                    listaObjetivos,
                                    listaEstructura)
        
        nodoMaqueta = NodoMaqueta(claseMaqueta)
        listaMaquetas.insertarMaqueta(nodoMaqueta)

        print("------------------------------\n\n")
    
    listaMaquetas.ordenarMaquetas()
    listaMaquetas.imprimirMaquetas()


def seleccionMaqueta(listaMaqueta):
    window = tk.Tk()
    window.geometry("500x400")
    window.title("Selección de maquetas")

    listbox = tk.Listbox(window)
    tmpListaMaquetas = listaMaqueta.cabeza
    i = 0
    while tmpListaMaquetas:
        listbox.insert(i, f"{tmpListaMaquetas.valor.nombreMaqueta}")
        i += 1
        tmpListaMaquetas = tmpListaMaquetas.siguiente

    listbox.pack()

    boton_imprimir = tk.Button(window, text="Imprimir", command= lambda: listaMaqueta.imprimirMaqueta(listbox.get(listbox.curselection()), None))
    boton_imprimir.pack()


    boton_resolver = tk.Button(window, text="Resolver laberinto", command= lambda: listaMaqueta.resolverMaqueta(listbox.get(listbox.curselection())))
    boton_resolver.pack()

    window.mainloop()  



def main():

    listaMaquetas = ListaMaquetas()
    root = tk.Tk()
    root.geometry("500x400")
    root.title("PROYECTO 2")

    btnCargaArchivo = tk.Button(root, text="Cargar Archivo", width=40, height=5, command = lambda: lectorXML(listaMaquetas))
    btnCargaArchivo.pack(pady=10)

    btnSeleccionMaqueta = tk.Button(root, text="Seleccionar Maqueta", width=40, height=5, command = lambda: seleccionMaqueta(listaMaquetas))
    btnSeleccionMaqueta.pack(pady=15)

    btnAyuda = tk.Button(root, text="Ayuda", width=40, height=5, command = lambda: print("DUMMY"))
    btnAyuda.pack(pady=15)
    root.mainloop()

    


if __name__ == "__main__":
    main()