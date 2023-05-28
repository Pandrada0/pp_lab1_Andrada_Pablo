import re 
import json

def leer_archivo(archivo_json:str)->list:
    """
    recibe la ruta de un .json
    lee el archivo en modo escritura
    devuelve una lista con el contenido del json
    """
    with open(archivo_json,"r") as archivo:
        dict_json = json.load(archivo)
        lista_jugadores = dict_json["jugadores"]

    return lista_jugadores

def imprimir_dato(texto:str)->None:
     """
     recibe un dato (str)
     imprime el dato recibido por parametro
     return = None
     """
     print(texto)

def imprimir_menu()->int:
    """
    recibe = None
    imprime el menu de la app valida la respusta
    retorna la respuesta de ser validada o -1 caso contrario
    """
    imprimir_dato("\n1- Mostrar la lista de todos los jugadores del Dream Team \n"
                    "2- Elejir un jugador por su índice, mostrar sus estadísticas completas y exportarlas a CSV \n"
                    "3- Buscar un jugador por su nombre y mostrar sus logros  \n"
                    "4- Mostrar el promedio de puntos por partido de todo el equipo del Dream Team \n"
                    "5- Mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto\n"
                    "6- El jugador con la mayor cantidad de rebotes totales \n"
                    "7- El jugador con la mayor porcentaje de tiros de campo \n"
                    "8- El jugador con la mayor cantidad de asistencias totales \n"
                    "9- Mostrar los jugadores que han promediado más puntos por partido que el valor \n"
                    "10- Mostrar los jugadores que han promediado rebotes por partido que el valor \n"
                    "11- Mostrar los jugadores que han promediado más asistencias por partido que el valor \n"
                    "12- Mostrar el jugador con la mayor cantidad de robos totales \n"
                    "13- Mostrar el jugador con la mayor cantidad de bloqueos totales \n"
                    "14- Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior al valor \n"
                    "15- Promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido\n"
                    "16- El jugador con la mayor cantidad de logros obtenidos\n"        
                    "17- Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor\n"
                    "18- Mostrar el jugador con la mayor cantidad de temporadas jugadas \n"
                    "19- Ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior al valor\n"
                    "20- Bonus \n"
                    "21- Salir  \n")

    respuesta = input("ingrese la opcion que desea: ")
    repuesta_validada = re.match(r"^[0-9]|[1]{1}[0-9]{1}|[2]{1}[0]{1}$",respuesta)
    if repuesta_validada != None:
        return respuesta
    else: 
        return -1  


def mostrar_nombre_jugadores(lista_jugadores_copia:list[dict])->None:
    """
    Recibe una copia de la lista de jugadores (list[dict])
    Muestra el nombre y la posicion con un formato especifico
    return = None
    """
    if len(lista_jugadores_copia) != 0:
        imprimir_dato("\n Nombre jugador   - Posición.")
        contador = 0
        for jugador in lista_jugadores_copia:
            imprimir_dato("{0}) {1} - {2}".format(contador,jugador["nombre"],jugador["posicion"]))
            contador += 1
    else:
        imprimir_dato("la lista se encuentra vacia")

def estadisticas_jugador(lista_jugadores_copia:list[dict])->list[dict]:
    """
    Recibe una copia de la lista de jugadores (list[dict]).
    muestra el jugador segun el indice ingresado.
    retorna una lista con el indce del jugador
    """
    if len(lista_jugadores_copia) != 0:
        mostrar_nombre_jugadores(lista_jugadores_copia)
        indice = input("ingrese el indice del jugador que desea ver sus estadisticas: ")
        indice_validado = re.match(r"^[0-9]{1}|[1]{1}[0-2]{1}$",indice)
        lista_aux = []
        
        if indice_validado != None:
            indice_int = int(indice)
            if indice_int < len(lista_jugadores_copia):
                lista_aux = lista_jugadores_copia[indice_int]
                for clave in lista_jugadores_copia[indice_int]:
                    if  clave == "logros":
                        break
                    elif clave != "estadisticas":
                        imprimir_dato(" {0} : {1} ".format(clave,lista_jugadores_copia[indice_int][clave]))
                    else:
                        for clave_estad,valores in lista_jugadores_copia[indice_int]["estadisticas"].items():
                            imprimir_dato(" {0} : {1} ".format(clave_estad,valores))
                return lista_aux
            else: 
                imprimir_dato("el indice supera el largo de la lista")
                return -1
        else:
            imprimir_dato("indice invalido")

    else:
        imprimir_dato("la lista se encuentra vacia")

def exportar_csv(jugadores_estadistica:list[dict])->None:
    """
    Recibe una lista (list[dict]) que contiene los datos de un solo juagdor.
    copia el dato recibo a un archivo .csv y de no existir lo crea
    return = None
    """
    lista_jugador_copia = jugadores_estadistica
    nombre = lista_jugador_copia["nombre"]
    path = r"C:\Users\pablo\Desktop\parcial_nba_noot\estadisticas_{0}.csv".format(nombre)
    texto_aux = ""
    with open (path,"w") as archivo:
        for clave,valor in lista_jugador_copia.items():
            if clave == "logros":
                break
            elif clave != "estadisticas":
                texto_aux += ("{0},".format(valor))
            elif clave == "estadisticas":
                key = (lista_jugador_copia["estadisticas"]).keys()
                for indice in key:
                    if indice != "porcentaje_tiros_libres":
                        texto_aux += ("{0},".format(lista_jugador_copia["estadisticas"][indice]))
                texto_aux += ("{0}".format(lista_jugador_copia["estadisticas"]["porcentaje_tiros_libres"]))

        archivo.write("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}\n".format("nombre","posicion","temporadas",
                                                                                   "puntos_totales","promedio_puntos_por_partido",
                                                                                   "rebotes_totales","promedio_rebotes_por_partido",
                                                                                   "asistencias_totales",
                                                                                   "promedio_asistencias_por_partido","robos_totales",
                                                                                   "bloqueos_totales","porcentaje_tiros_de_campo",
                                                                                   "porcentaje_tiros_libres","porcentaje_tiros_triples" ))                                                                                          
        archivo.write(texto_aux)
      
def validar_jugador_estadistica(lista_jugadores_copia:list[dict])->None:
    """
    Recibe una copia de la lista de jugadores (list[dict]) y la estadistica de un jugador elejido por el usuario.
    Valida si el usuario quiere exportar a un csv el jugador anterioemente elejido y llama a la funcion,
    exportar_csv
    return = None
    """
    jugador_estadisticas = estadisticas_jugador(lista_jugadores_copia)
    if jugador_estadisticas != -1:
        respuesta = input("¿Desea exportar el jugador selecionado a un CSV?")
        respuesta_validada = re.match(r"^[siSI]{2}|[noNO]{2}$",respuesta)
    
        if respuesta_validada != None :
            if respuesta.lower() == "si":
                exportar_csv(jugador_estadisticas)
            elif respuesta.lower() == "no":
                pass
            else:   
                imprimir_dato("respuesta invalida")     
        else:
             imprimir_dato("La opcion es incorrecta")

def mostrar_logros_NBA(lista_jugadores_copia:list[dict],flag:bool)->None:
    """
    Recibe una copia de la lista de jugadores (list[dict])  y un bool
    Muestra los logros del jugador ingresado por el usuario, el bool decide si,
    se muestra las estadisticas de los jugadores o el promedio del equipo
    return = None
    """
    if len(lista_jugadores_copia) != 0:
        mostrar_nombre_jugadores(lista_jugadores_copia)
        
        imprimir_dato("\n")
        jugador_ingresado = input("Ingrese el nombre del jugador: ")
        jugador_validado = re.match(r"^[A-Za-z ]+$",jugador_ingresado)
        flag_nombre = True

        if jugador_validado != None:
            imprimir_dato("\n")
            for jugador in lista_jugadores_copia: 
                nombre = re.search(jugador_ingresado.lower(),(jugador["nombre"]).lower())
                if nombre != None:
                    flag_nombre = False
                    if flag == False:
                        for indice in range(len(jugador["logros"])):
                            imprimir_dato("{0}".format(jugador["logros"][indice]))
                    else:
                        miembro = "Miembro del Salon de la Fama del Baloncesto"
                        if miembro in jugador["logros"]:
                            imprimir_dato(" {0} se encuentra en el salon de la fama.".format(jugador["nombre"]))
                        else:
                            imprimir_dato("No se encuentra en el salon de la fama.")
            if flag_nombre:
                imprimir_dato("El nombre no existe en la base de datos")       
                        
        else:
            imprimir_dato("El nombre ingresado es incorrecto")
    else:
            imprimir_dato("la lista se encuentra vacia") 

def calcular_mostrar_promedio_puntos (lista_jugadores_copia:list[dict])->None:
    """
    Recibe una copia de la lista de jugadores (list[dict])
    Saca el promedio de puntos por partido del Dream Team
    return = None
    """
    if len(lista_jugadores_copia) != 0:
        acumulador = 0
        contador = 0
        if len(lista_jugadores_copia) != 0:
            for jugador in lista_jugadores_copia:
                acumulador += float(jugador["estadisticas"]["promedio_puntos_por_partido"])
                contador += 1 
            
        else:
            imprimir_dato("La lista esta vacia")

        promedio = acumulador / contador
        imprimir_dato("Promedio de puntos por partido del equipo Dream Team: {0}".format(promedio))
    else:
            imprimir_dato("la lista se encuentra vacia") 

def calcular_mostrar_key(lista_jugadores_copia:list[dict],key:str,flag:bool=False)->None:
    """
    Recibe una copia de la lista de jugadores (list[dict]), un bool y una key.
    Calula el mayor recorriendo la lista segun la key y lo imprime y el bool es por si comparten podio.
    return = None
    """
    if len(lista_jugadores_copia) != 0:
        if key == "asistencias_totales" or key == "robotes_totales" or key == "temporadas":
            key_tipo = int
        else:
            key_tipo = float
        for jugador in lista_jugadores_copia:
            if lista_jugadores_copia[0] == jugador or key_tipo( key_tipo(jugador["estadisticas"][key] > jugador_aux["estadisticas"][key]) ):
                jugador_aux = jugador

        if flag:
            for jugador in lista_jugadores_copia:
                if key_tipo(jugador_aux["estadisticas"]["temporadas"]) == key_tipo(jugador["estadisticas"]["temporadas"]):
                    imprimir_dato("Nombre:{0} - {1}:{2}".format(jugador["nombre"],key,jugador["estadisticas"][key]))

        else:
            imprimir_dato("Nombre:{0} - {1}:{2}".format(jugador_aux["nombre"],key,jugador_aux["estadisticas"][key]))

    else:
        imprimir_dato("la lista se enceuntra vacia")

def mostrar_jugadres_segun_dato_ingresado(lista_jugadores_copia:list[dict],key:str)->None:
    """
    Recibe una copia de la lista de jugadores (list[dict]) y una key.
    Muesrta el mayor recorriendo la lista segun la key pasada
    return = None
    """
    if len(lista_jugadores_copia) != 0:
        valor = input("ingrese el valor: ")
        imprimir_dato("\n")
        valor_validado = re.match(r"^[0-9 ]+$",valor)
        flag = True

        if valor_validado != None:
            key_tipo = float
            for jugador in lista_jugadores_copia:

                if key_tipo(valor) < key_tipo(jugador["estadisticas"][key]):
                    imprimir_dato("Nombre: {0} - {1}: {2}".format(jugador["nombre"],key,jugador["estadisticas"][key]))
                    flag = False
            if flag:
                imprimir_dato("Ningun jugador supera el valor ingresado")
        else:
            imprimir_dato("El valor ingresado es incorrecto:")
    else:
        imprimir_dato("la lista se enceuntra vacia")

def promedio_pts_partido_ecluyente(lista_jugadores_copia:list[dict])->None:
    """
    Recibe una copia de la lista de jugadores (list[dict])
    Saca el promedio de puntos por partido exclueyndo al de menor puntaje
    return = None
    """
    if len(lista_jugadores_copia) != 0:
        jugador_aux = {}
        acumulador = 0
        contador = 0 
        for jugador in lista_jugadores_copia:

            if lista_jugadores_copia[0] == jugador or \
            float(jugador_aux["estadisticas"]["promedio_puntos_por_partido"]) > jugador["estadisticas"]["promedio_puntos_por_partido"] :
                jugador_aux = jugador

        for jugador in lista_jugadores_copia:
            if jugador == jugador_aux:
                pass
            else:
                acumulador += float(jugador["estadisticas"]["promedio_puntos_por_partido"])
                contador += 1

        promedio = acumulador / contador

        imprimir_dato("El promedio del Dream Team sin el menor promedio es: {0}".format(promedio))
    else:
        imprimir_dato("la lista se enceuntra vacia")

def mayor_logros_obtenidos(lista_jugadores_copia:list[dict])->None:
    """
    Recibe una copia de la lista de jugadores (list[dict])
    Muestra al jugador con mas logros obtenidos
    return = None
    """
    if len(lista_jugadores_copia) != 0:
        for jugador in lista_jugadores_copia:

            if jugador == lista_jugadores_copia[0] or len(jugador_aux["logros"]) < len(jugador["logros"]):

                jugador_aux = jugador
        imprimir_dato("El jugador con mas logros es: {0}".format(jugador_aux["nombre"]))
        for estadisticas in jugador_aux["logros"]:
            imprimir_dato("{0}".format(estadisticas))
    else:
        imprimir_dato("la lista se enceuntra vacia")

def ordenar_posicion_valor(lista_jugadores_copia:list[dict])->None:
    """
    Recibe una copia de la lista de jugadores (list[dict])
    Muestra los jugadores que superen el valor ingresado por el orden de,
    las posiciciones en la cancha.    
    return = None
    """
    if len(lista_jugadores_copia) != 0:
        valor = input("ingrese el valor: ")
        imprimir_dato("\n")
        valor_validado = re.match(r"^[0-9 ]+$",valor)
        flag = True

        if valor_validado != None:
            lista_posicion =["Base","Escolta","Alero","Ala-Pivot","Pivot"]
            indice = 0
            contador = 0
            if valor_validado != None:
                key_tipo = float
                flag_while = True
                while flag_while:
                    for jugador in lista_jugadores_copia:
                        if jugador["posicion"] == lista_posicion[indice] and \
                            key_tipo(jugador["estadisticas"]["porcentaje_tiros_de_campo"]) > key_tipo(valor):
                                imprimir_dato("Nombre: {0} - Posicion: {1} - Porcentaje tirpos de campo: {2} ".format(jugador["nombre"],
                                                                                                                    jugador["posicion"],
                                                                                    jugador["estadisticas"]["porcentaje_tiros_de_campo"]))
                                flag = False
                        contador += 1
                        
                        if contador == 12:
                            contador = 0
                            indice += 1
                        if indice == 5:
                            flag_while = False
                if flag:
                    imprimir_dato("Ningun jugador supera el valor ingresado")
        else:
            imprimir_dato("El valor ingresado es incorrecto:")
    else:
        imprimir_dato("la lista se enceuntra vacia")


        


            
















