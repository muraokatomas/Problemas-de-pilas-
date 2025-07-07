def pide_cant_pilas (tipo_de_pila):
    """ Ingresan por parametros  el tipo de pila y se pide
    cantidad de gramos de pilas  y devuelve los gramos  que
        esten en cierto rango """
    gramos = int(input("Ingrese gramos de pilas " + tipo_de_pila + ": "))
    while gramos < 0 or gramos > 99000:
        gramos = int(input("Ingrese una cantidad válida de gramos de pilas " + tipo_de_pila + ": "))
    return gramos
