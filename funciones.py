
import re 
import json


def leer_archivo(archivo_json:str)->list:
    """
    recibe el archivo .json
    lee el archivo en modo escritura
    devuelve una lista con el contenido del json

    """
    with open(archivo_json,"r") as archivo:
        dict_json = json.load(archivo)
        lista_heroe = dict_json["jugadores"]

    return lista_heroe

def imprimir_dato(texto:str)->None:
     """
     recibe un dato (str)
     imprime el dato recibido por parametro
     None
     """
     print(texto)

def imprimir_menu()->None:
    """
    None
    imprime el menu de la app
    None
    """
    imprimir_dato("\n1- \n"
                    "2- \n"
                    "3- \n"
                    "4- \n"
                    "5- \n"
                    "6- \n"
                    "7- \n"
                    "8- \n"
                    "9- \n"
                    "10- \n"
                    "11- \n"
                    "12- \n"
                    "13- \n"
                    "14- \n"
                    "15- \n"
                    "16- \n"
                    
                    "17- \n"
                    "18- \n"
                    "19- \n"
                    "20- \n"
                    "Z- Salir  \n")