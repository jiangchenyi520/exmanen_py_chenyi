import csv
filename = "winequality.csv"
def read_data(filename): 
    """
      Dado un nombre de fichero conn muestras de vino devuelve un diccionario

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    f = open(filename, mode= "rt", encoding= "utf-8")
    reader = csv.reader(f)
    for row in reader: 
        return(row)
        dicctionary = dict(row)
    

read_data(filename)

#ejercicio3 


def split(diccionary): 
    """
    Dado un diccionario, devuelve dos diccionarios. EL primero es un diccionario con las muestras 
    que tengan el valor white en el atributo type y el segundo es un diccionario con los datos que tengan 
    el valor red en ese atributo. EL atirbuto type se eliminara de cada dato en estos diccionarios devueltos
    """
    dict1 = {}
    dict2 = {}
    for k, v in diccionary.items():
        if k == "white": 
            return dict2(v)
        elif k == "red":
            return dict1(v)


#ejercicio4 
def reduce(dicctionary, atributo):
    for key, value in dicctionary.items(): 
        if key != atributo: 
            raise ValueError("Ha ocurrido la excepción")
        elif key == atributo:
            return list(key,value)

#ejercicio 5
def silhouette(lista1, lista2): 
    return 0


"Crea una funcion silhouette que recibe dos listas y devuelve el coeficiente de Silhouette de la primera de las dos listas"