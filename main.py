from funciones import (leer_archivo,imprimir_menu,mostrar_nombre_jugadores,mostrar_logros_NBA,validar_jugador_estadistica,
                       calcular_mostrar_promedio_puntos,imprimir_dato,calcular_mostrar_key,mayor_logros_obtenidos,
                       mostrar_jugadres_segun_dato_ingresado,promedio_pts_partido_ecluyente,ordenar_posicion_valor)

lista_jugadores = leer_archivo(r"C:\Users\pablo\Desktop\parcial_nba_noot\dt.json")
lista_jugadores_copia = lista_jugadores.copy()
def parcial_nba(lista_jugadores_copia):
      
    while True:
        respuesta = imprimir_menu()
        if respuesta == "1":
            mostrar_nombre_jugadores(lista_jugadores_copia)
        elif respuesta == "2":
            validar_jugador_estadistica(lista_jugadores_copia)
        elif respuesta == "3":
            mostrar_logros_NBA(lista_jugadores_copia,False)
        elif respuesta == "4":
            calcular_mostrar_promedio_puntos(lista_jugadores_copia)
        elif respuesta == "5":
           mostrar_logros_NBA(lista_jugadores_copia,True)
        elif respuesta == "6":
           calcular_mostrar_key(lista_jugadores_copia,"rebotes_totales")
        elif respuesta == "7":
            calcular_mostrar_key(lista_jugadores_copia,"porcentaje_tiros_de_campo")
        elif respuesta == "8":
           calcular_mostrar_key(lista_jugadores_copia,"asistencias_totales")
        elif respuesta == "9":
           mostrar_jugadres_segun_dato_ingresado(lista_jugadores_copia,"promedio_puntos_por_partido")
        elif respuesta == "10":
            mostrar_jugadres_segun_dato_ingresado(lista_jugadores_copia,"promedio_rebotes_por_partido")
        elif respuesta == "11":
           mostrar_jugadres_segun_dato_ingresado(lista_jugadores_copia,"promedio_asistencias_por_partido")
        elif respuesta == "12":
           calcular_mostrar_key(lista_jugadores_copia,"robos_totales")
        elif respuesta == "13":
           calcular_mostrar_key(lista_jugadores_copia,"bloqueos_totales")
        elif respuesta == "14":
           mostrar_jugadres_segun_dato_ingresado(lista_jugadores_copia,"porcentaje_tiros_libres")
        elif respuesta == "15":
           promedio_pts_partido_ecluyente(lista_jugadores_copia)
        elif respuesta == "16":
           mayor_logros_obtenidos(lista_jugadores_copia)
        elif respuesta == "17":
           mostrar_jugadres_segun_dato_ingresado(lista_jugadores_copia,"porcentaje_tiros_triples")
        elif respuesta == "18":
           calcular_mostrar_key(lista_jugadores_copia,"temporadas",True)
        elif respuesta == "19":
           ordenar_posicion_valor(lista_jugadores_copia)
        elif respuesta == "20":
           pass
        elif respuesta == "21":
            break
        else:
            imprimir_dato("Respuesta incorrecta, vuelva a intentarlo.\n")


parcial_nba(lista_jugadores)
