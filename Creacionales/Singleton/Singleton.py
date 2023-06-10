# Creation date: 30/01/2020
# Last modified date: 30/01/2020
# Author: Javier Ramos Pérez
# Description: Implementación del patrón de diseño Singleton en Python

class Singleton:
    """
    El patrón de diseño Singleton se utiliza cuando queremos que una clase tenga una única instancia.
    Para ello, la clase Singleton tiene un método estático que devuelve la instancia de la clase.
    Si la instancia no existe, la crea. Si ya existe, devuelve la instancia ya creada.
    """
    __instance = None

    @staticmethod
    def getInstance():
        # Si la instancia no existe, la creamos
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        # Si la instancia ya existe, lanzamos un error
        if Singleton.__instance != None:
            raise Exception("Esta clase es un singleton!")
        else:
            Singleton.__instance = self

# Creamos una instancia
singleton1 = Singleton.getInstance()
# Creamos otra instancia
singleton2 = Singleton.getInstance()

# Comprobamos que ambas instancias son la misma
print(singleton1 is singleton2)