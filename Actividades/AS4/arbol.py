class NodoFama:

    def __init__(self, usuario, padre=None):
        # No modificar
        self.usuario = usuario
        self.padre = padre
        self.hijo_izquierdo = None
        self.hijo_derecho = None


class ArbolBinario:

    def __init__(self):
        # No modificar
        self.raiz = None

    def crear_arbol(self, nodos_fama):
        # No modificar
        for nodo in nodos_fama:
            self.insertar_nodo(nodo, self.raiz)

    def insertar_nodo(self, nuevo_nodo, padre=None):
        # Completar
        nodo_actual = None

        while padre is not None:
            nodo_actual = padre
            if nuevo_nodo.usuario.fama < padre.usuario.fama:
                padre = padre.hijo_izquierdo
            else:
                padre = padre.hijo_derecho
        
        if nodo_actual is None:
            self.raiz = nuevo_nodo
        
        elif nuevo_nodo.usuario.fama < nodo_actual.usuario.fama:
            nodo_actual.hijo_izquierdo = nuevo_nodo
        
        else:
            nodo_actual.hijo_derecho = nuevo_nodo
            
    def buscar_nodo(self, fama, padre=None):
        # Completar
        nodo_actual = self.raiz
        #Caso en que se busque la raiz
        if nodo_actual.usuario.fama == fama:
            return nodo_actual

        #Caso en que no se busque la raiz
        while nodo_actual.hijo_izquierdo or nodo_actual.hijo_derecho:

            hijo_izquierdo = nodo_actual.hijo_izquierdo
            hijo_derecho = nodo_actual.hijo_derecho

            if hijo_izquierdo is not None:
                if hijo_izquierdo.usuario.fama == fama:
                    return hijo_izquierdo
                elif nodo_actual.usuario.fama < fama:
                    nodo_actual = hijo_izquierdo

            elif hijo_derecho is not None:
                if hijo_derecho.usuario.fama == fama:
                    return hijo_derecho
                elif nodo_actual.usuario.fama > fama:
                    nodo_actual = hijo_derecho
        return None

    def print_arbol(self, nodo=None, nivel_indentacion=0):
        # No modificar
        indentacion = "|   " * nivel_indentacion
        if nodo is None:
            print("** DCCelebrity Arbol Binario**")
            self.print_arbol(self.raiz)
        else:
            print(f"{indentacion}{nodo.usuario.nombre}: "
                  f"{nodo.usuario.correo}")
            if nodo.hijo_izquierdo:
                self.print_arbol(nodo.hijo_izquierdo,
                                 nivel_indentacion + 1)
            if nodo.hijo_derecho:
                self.print_arbol(nodo.hijo_derecho,
                                 nivel_indentacion + 1)
