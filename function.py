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
    """
      reader = csv.reader(f)
    dato = {}
    for row in reader: 
        columnas 
        return(row)
    """

    for linea in f:
        linea = linea.rstrip("\n")  # Quitar salto de línea
        columnas = linea.split()
        dato= {}
        tipo = columnas[0]
        actividad = (columnas[1])
        acid= float(columnas[2])
        acid2 = float(columnas[3])
        sugar = float(columnas[4])
        chlorides = float(columnas[5])
        sulfur = float(columnas[6])
        total = float(columnas[7])
        density = float(columnas[8])
        ph = (columnas[9])
        sulphates= (columnas[10])
        alcohol = (columnas[11])
        dato.append({
            "tipo": tipo,
            "fixed acidity": actividad,
            "volatile acidity" : acid,
            "adic": acid2,
            "x2": sugar,
            "x3": chlorides,
            "j": sulfur,
            "total" : total, 
            "density" : density, 
            "ph" : ph,  
            "sulphates": sulphates,
            "alcohol" : alcohol 
        })
        return dato
        

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

