import random

colores = {
    "verde": '\u001b[42;30m',
    "amarillo": '\u001b[43;30m',
    "gris": '\u001b[47;30m',
    "reset": '\u001b[0m'
}

jugadores_registrados = {
    "Jamon": {"juegos": 5, "puntos": 600, "promedio": 90},
    "Queso": {"juegos": 8, "puntos": 640, "promedio": 80},
    "Fresco": {"juegos": 10, "puntos": 700, "promedio": 70},
    "Batata": {"juegos": 6, "puntos": 300, "promedio": 50},
    "Boca": {"juegos": 12, "puntos": 840, "promedio": 70},
    "River": {"juegos": 4, "puntos": 100, "promedio": 25},
    "Cabildo": {"juegos": 7, "puntos": 490, "promedio": 70},
    "Juramento": {"juegos": 9, "puntos": 360, "promedio": 40}
}

banco_palabras = {
    "es": {
        5: ("razón", "árbol"),
        6: ("imagen", "entero"),
        7: ("domingo", "mensaje"),
        8: ("computar", "libreria")
    },
    "en": {
        5: ("apple", "bread"),
        6: ("animal", "bridge"),
        7: ("airport", "balance"),
        8: ("building", "computer")
    },
    "pt": {
        5: ("livro", "prato"),
        6: ("cidade", "janela"),
        7: ("amarelo", "sistema"),
        8: ("computar", "montanha")
    }
}

mapa_reemplazos = {
        'á':'a','à':'a','ä':'a','â':'a','ã':'a',
        'é':'e','è':'e','ë':'e','ê':'e',
        'í':'i','ì':'i','ï':'i','î':'i',
        'ó':'o','ò':'o','ö':'o','ô':'o','õ':'o',
        'ú':'u','ù':'u','ü':'u','û':'u',
        'ç':'c',
        'Á':'a','À':'a','Ä':'a','Â':'a','Ã':'a',
        'É':'e','È':'e','Ë':'e','Ê':'e',
        'Í':'i','Ì':'i','Ï':'i','Î':'i',
        'Ó':'o','Ò':'o','Ö':'o','Ô':'o','Õ':'o',
        'Ú':'u','Ù':'u','Ü':'u','Û':'u',
        'Ç':'c'
}

intentos_por_longitud = {5: 6, 6: 7, 7: 9, 8: 10}



def documentacion():
    """
    Muestra un menú con la documentación de las funciones del programa.

    Imprime un texto de bienvenida y una lista numerada con los nombres de las funciones. Si el usuario escribe un número válido, se muestra el docstring de esa función. Si presiona ENTER, vuelve al menú principal.
    """
    print("\n==========================================")
    print("           D O C U M E N T A C I Ó N      ")
    print("==========================================\n")
    print(
        "Bienvenido a la documentación del programa.\n"
        "A continuación verás una lista numerada de funciones.\n"
        "Ingresá el número de una función para ver su descripción,\n"
        "o presioná ENTER para volver al menú principal.\n"
    )

    funciones = [
        ("main", main),
        ("bienvenida", bienvenida),

        ("definir_jugador", definir_jugador),
        ("iniciar_sesion", iniciar_sesion),

        ("seleccionar_idioma", seleccionar_idioma),
        ("seleccionar_longitud", seleccionar_longitud),
        ("elegir_palabra", elegir_palabra),

        ("normalizar", normalizar),
        ("colorear_intento", colorear_intento),
        ("imprimir_historial", imprimir_historial),
        ("calcular_puntaje", calcular_puntaje),
        ("jugar_turno", jugar_turno),
        ("actualizar_estadisticas", actualizar_estadisticas),

        ("estadisticas", estadisticas),
        ("estadisticas_general", estadisticas_general),
        ("estadisticas_ranking", estadisticas_ranking),
        ("estadisticas_jugador", estadisticas_jugador),

        ("documentacion", documentacion),
    ]

    indice = 0
    while indice < len(funciones):
        nombre_funcion, _ = funciones[indice]
        print(f"{indice + 1}. {nombre_funcion}")
        indice = indice + 1

    print("\nIngresá un número para consultar una función, o ENTER para volver.")

    seguir_consultando = True
    while seguir_consultando:
        entrada = input("> ").strip()
        if entrada == "":
            bienvenida()
            return
        else:
            if entrada.isdigit():
                numero = int(entrada)
                if 1 <= numero <= len(funciones):
                    nombre_funcion, referencia = funciones[numero - 1]
                    doc = referencia.__doc__
                    print("\n------------------------------------------")
                    print(f"Documentación de {nombre_funcion}:\n")
                    if doc is None:
                        print("No hay documentación disponible para esta función.")
                    else:
                        print(doc.strip())
                    print("------------------------------------------")
                    print("Ingresá otro número para consultar otra función, o ENTER para volver.")
                else:
                    print("Número fuera de rango. Ingresá un número válido o ENTER para volver.")
            else:
                print("Entrada inválida. Ingresá un número o presioná ENTER para volver.")

def bienvenida():
    """
    Muestra el banner y el menú principal.

    ENTER comienza el juego. 1 muestra las instrucciones aquí mismo y luego vuelve al menú. 5 muestra las estadísticas. 9 sale del juego. Permanece en un bucle leyendo la opción hasta que se elija jugar o salir.

    Retorna:
        True / False
    """
    banner = (
        "\n"
        "==========================================\n"
        "              W  O  R  D  L  E            \n"
        "==========================================\n"
    )
    menu = (
        "Presiona ENTER para jugar.\n"
        "Ingresa 1 para ver las instrucciones.\n"
        "Ingresa 5 para ver las estadísticas de jugadores.\n"
        "Escribi 9 para salir del juego.\n"
        "==========================================\n"
    )

    instrucciones = (
        "De que se trata?\n"
        "Adivinar la palabra oculta antes de que se te acaben los intentos.\n\n"
        "Cómo jugar\n"
        "1) Elegi idioma y largo de palabra. Cuanto mas larga sea la palabra, mas intentos para adivinarla vas a tener!\n"
        "2) Escribi en cada turno una palabra con ese largo. OJO: no es necesario respetar mayusculas ni acentos!\n"
        "3) Wordle te va a devolver tu palabra coloreada segun los siguientes criterios:\n"
        "   • Verde: letra correcta en posición correcta.\n"
        "   • Amarillo: letra presente pero en otra posición.\n"
        "   • Gris: letra ausente en la palabra palabra.\n\n"
        "Puntaje\n"
        "• Desde el 2º intento, el puntaje empieza en 100 y disminuye con cada intento usado hasta llegar a 0 si no se acierta en el ultimo.\n"
        "• Si acertás en el primer intento... Ganas 150 puntos!\n"
    )

    print(banner)
    print("MENU PRINCIPAL")
    print("==========================================")
    print(menu)

    listo_para_jugar = False
    while not listo_para_jugar:
        opcion = input("> ").strip()
        if opcion == "":
            listo_para_jugar = True
        elif opcion == "1":
            print("==========================================\n")
            print(instrucciones)
            print("==========================================\n")
            print(menu)
        elif opcion == "5":
            print("==========================================\n")
            estadisticas()
            print("\n==========================================\n")
            print(menu)
        elif opcion == "documentacion":
            documentacion()
        elif opcion == "9":
            return False
        else:
            print("==========================================\n")
            print("Opción no válida.")
            print(menu)
    return True

def definir_jugador():
    """
    Pide al jugador que ingrese su nombre.

    Se valida que no esté vacío y que contenga solo letras. Se formatea capitalizando la primera letra. Saluda según exista o no en jugadores_registrados.

    Retorna:
        jugador
    """
    jugador = ""
    while jugador.strip() == "":
        jugador = input("Ingrese el nombre del jugador: ")
        jugador = jugador.strip()
        while not jugador.isalpha():
            print("El nombre solo puede contener letras.")
            jugador = input("Ingrese el nombre del jugador: ")
            jugador = jugador.strip()
    jugador = jugador.title()

    return jugador


def iniciar_sesion(jugador):
    """
    Saluda según jugador exista o no en jugadores_registrados.
    """
    if jugador in jugadores_registrados:
        print(f"Bienvenido de vuelta, {jugador}!")
    else:
        print(f"Bienvenido a tu primer juego de Wordle, {jugador}!")


def seleccionar_idioma():
    """
    Permite elegir el idioma del juego.

    Solo acepta es/en/pt. Repite la pregunta hasta que se ingrese un valor válido.

    Retorna:
        idioma
    """
    print("Idiomas disponibles: es (español), en (inglés), pt (portugués)")
    idioma = ""
    while idioma not in ("es", "en", "pt"):
        idioma = input("Elija idioma [es/en/pt]: ").strip().lower()
        if idioma not in ("es", "en", "pt"):
            print("Idioma no válido. Intente de nuevo.")
    return idioma

def seleccionar_longitud():
    """
    Pide la longitud de la palabra y valida que esté entre 5 y 8.

    Solo acepta números enteros en ese rango y repite la pregunta hasta que sea válido.

    Retorna:
        longitud
    """
    while True:
        entrada = input("Elija largo de palabra (5 a 8): ").strip()
        if entrada.isdigit():
            longitud = int(entrada)
            if 5 <= longitud <= 8:
                return longitud
            else:
                print("Debe ser un número entre 5 y 8.")
        else:
            print("Ingrese un número válido entre 5 y 8.")

def elegir_palabra(idioma, longitud):
    """
    Elige una palabra del banco según idioma y longitud.

    Usa banco_palabras[idioma][longitud] para obtener la tupla de palabras y selecciona una al azar.

    Parametros:
        idioma, longitud
    Retorna:
        palabra
    """
    lista_palabras = banco_palabras[idioma][longitud]
    indice = random.randint(0, len(lista_palabras) - 1)
    palabra = lista_palabras[indice]

    return palabra


def normalizar(texto):
    """
    Convierte un texto a minúsculas y sin acentos.

    Reemplaza vocales acentuadas y ç por su forma simple usando mapa_reemplazos. Útil para comparar entradas del jugador con la palabra objetivo sin depender de mayúsculas ni tildes.

    Parametros:
        texto
    Retorna:
        texto_normalizado
    """

    texto_normalizado = ""
    indice = 0

    while indice < len(texto):
        caracter = texto[indice]
        if caracter in mapa_reemplazos:
            texto_normalizado = texto_normalizado + mapa_reemplazos[caracter]
        else:
            texto_normalizado = texto_normalizado + caracter.lower()
        indice = indice + 1

    return texto_normalizado

def preparar_fondo(entrada, palabra):
    """
    Compara la entrada con la palabra objetivo y arma la lista de colores por letra.

    Primero marca en verde las coincidencias exactas y cuenta las letras restantes de la palabra. Luego, para las posiciones no verdes, marca en amarillo si la letra del intento aún está disponible en ese conteo. El resto queda gris.

    Parametros:
        entrada, palabra
    Retorna:
        fondo
    """
    longitud = len(palabra)
    fondo = []
    i = 0
    while i < longitud:
        fondo.append("gris")
        i = i + 1

    entrada_normalizada = normalizar(entrada)
    palabra_normalizada = normalizar(palabra)

    letras_disponibles = {}
    i = 0
    while i < longitud:
        if entrada_normalizada[i] == palabra_normalizada[i]:
            fondo[i] = "verde"
        else:
            no_es_verde = palabra_normalizada[i]
            if no_es_verde in letras_disponibles:
                letras_disponibles[no_es_verde] = letras_disponibles[no_es_verde] + 1
            else:
                letras_disponibles[no_es_verde] = 1
        i = i + 1

    i = 0
    while i < longitud:
        if fondo[i] != "verde":
            es_amarillo = entrada_normalizada[i]
            if (es_amarillo in letras_disponibles) and (letras_disponibles[es_amarillo] > 0):
                fondo[i] = "amarillo"
                letras_disponibles[es_amarillo] = letras_disponibles[es_amarillo] - 1
        i = i + 1

    return fondo

def pintar_resultado(entrada, fondo):
    """
    Devuelve la representación coloreada de la palabra ingresada.

    Toma la lista de colores (fondo) y la palabra en mayúsculas, arma cada bloque con los códigos ANSI y los une en un string listo para imprimir.

    Parametros:
        entrada, fondo
    Retorna:
        resultado
    """
    letras_fondo = []
    indice = 0
    entrada_mayuscula = entrada.upper()

    while indice < len(fondo):
        letra = entrada_mayuscula[indice]
        letras_fondo.append(f"{colores[fondo[indice]]} {letra} {colores['reset']}")
        indice = indice + 1

    resultado = " ".join(letras_fondo)
    return resultado

def colorear_intento(entrada, palabra):
    """
    Muestra el intento como una string coloreada por letra.

    Parametros:
        entrada
        palabra
    Retorna:
        resultado
        acierto
    """
    palabra_normalizada = normalizar(palabra)
    entrada_normalizada = normalizar(entrada)
    entrada_mayuscula = entrada.upper()
    longitud = len(palabra_normalizada)

    fondo = []
    indice = 0
    while indice < longitud:
        fondo.append("gris")
        indice = indice + 1

    letras_disponibles = {}
    indice = 0
    while indice < longitud:
        if entrada_normalizada[indice] == palabra_normalizada[indice]:
            fondo[indice] = "verde"
        else:
            letra = palabra_normalizada[indice]
            if letra in letras_disponibles:
                letras_disponibles[letra] = letras_disponibles[letra] + 1
            else:
                letras_disponibles[letra] = 1
        indice = indice + 1

    letras_fondo = []
    indice = 0
    while indice < longitud:
        if fondo[indice] != "verde":
            l = entrada_normalizada[indice]
            if (l in letras_disponibles) and (letras_disponibles[l] > 0):
                fondo[indice] = "amarillo"
                letras_disponibles[l] = letras_disponibles[l] - 1
            else:
                fondo[indice] = "gris"
        letras_fondo.append(f"{colores[fondo[indice]]} {entrada_mayuscula[indice]} {colores['reset']}")
        indice = indice + 1

    resultado = " ".join(letras_fondo)
    acierto = (entrada_normalizada == palabra_normalizada)
    return resultado, acierto

def imprimir_historial(historial):
    """
    Imprime el historial completo del turno en orden.

    Parametros:
        historial
    """
    intentos = 0
    while intentos < len(historial):
        print(historial[intentos])
        intentos = intentos + 1

def calcular_puntaje(acierto, nro_intento, intentos_totales):
    """
    Calcula el puntaje del juego según el intento en el que se acierta.

    Si no se acierta, devuelve 0. Si se acierta en el primer intento, devuelve 150. Desde el segundo intento, el puntaje parte de 100 y baja en pasos iguales según los intentos permitidos. Nunca devuelve un valor negativo.

    Parametros:
        acierto, nro_intento, intentos_totales
    Retorna:
        puntos
    """
    if not acierto:
        return 0
    if nro_intento == 1:
        return 150
    bajar_puntos = 100 // intentos_totales
    puntos = 100 - (nro_intento - 1) * bajar_puntos
    if puntos < 0:
        puntos = 0
    return puntos

def jugar_turno():
    """
    Ejecuta un turno del juego para el jugador.

    Pide idioma y longitud, elige una palabra, valida cada intento sin consumir cuando la longitud no coincide y muestra el historial coloreado. Si se acierta, calcula el puntaje. Al final informa el resultado y pregunta si se quiere jugar otra vez; devuelve si se sigue y los puntos del turno.

    Parametros:
        jugador
    Retorna:
        seguir, puntos
    """
    idioma = seleccionar_idioma()
    longitud = seleccionar_longitud()
    palabra = elegir_palabra(idioma, longitud)
    intentos_totales = intentos_por_longitud[longitud]

    historial = []
    intento_actual = 0
    acierto = False
    puntos = 0

    print(f"Palabra de {longitud} letras. Intentos permitidos: {intentos_totales}.")
    print("Verde: letra correcta en posición correcta. Amarillo: letra en otra posición. Gris: letra ausente.")

    while (intento_actual < intentos_totales) and (not acierto):
        if intento_actual == intentos_totales - 1:
            print("¡ÚLTIMO INTENTO!")

        entrada_valida = False
        entrada = ""
        while not entrada_valida:
            entrada = input(f"Intento {intento_actual + 1}/{intentos_totales} - Ingrese una palabra: ").strip()
            if len(entrada) == longitud:
                entrada_valida = True
            else:
                print(f"La palabra debe tener exactamente {longitud} letras.")

        resultado, acierto = colorear_intento(entrada, palabra)
        historial.append(resultado)
        imprimir_historial(historial)

        if acierto:
            puntos = calcular_puntaje(True, intento_actual + 1, intentos_totales)

        intento_actual = intento_actual + 1

    if acierto:
        print(f"¡Correcto! La palabra era: {palabra.upper()}. Puntos del juego: {puntos}")
    else:
        puntos = 0
        print(f"Sin intentos. La palabra era: {palabra.upper()}. Puntos del juego: {puntos}")

    respuesta = input("¿Jugar otra vez? (S/N): ").strip().lower()
    seguir = (respuesta == "s")

    return seguir, puntos


def actualizar_estadisticas(jugador, puntos):
    """
    Actualiza juegos y puntos del jugador y recalcula su precisión (puntos // juegos).

    Parametros:
        jugador, puntos
    """
    if jugador not in jugadores_registrados:
        jugadores_registrados[jugador] = {"juegos": 0, "puntos": 0}
    jugador = jugadores_registrados[jugador]
    jugador["juegos"] = jugador["juegos"] + 1
    jugador["puntos"] = jugador["puntos"] + puntos
    jugador["promedio"] = jugador["puntos"] // jugador["juegos"]


def estadisticas():
    """
    Muestra un menú de estadísticas.

    Ofrece ver estadísticas generales, top 5 o ver datos por jugador. ENTER vuelve al menú principal.

    Retorna:
        None
    """
    banner_estadisticas = (
        "\n==========================================\n"
        "          E S T A D Í S T I C A S  \n"
        "==========================================\n"
    )
    menu_estadisticas = (
        "Elegi una opcion:\n"
        "1) Estadisticas generales\n"
        "2) TOP 5\n"
        "3) Buscar por jugador\n"
        "ENTER para volver\n"
    )

    print(banner_estadisticas)
    print(menu_estadisticas)

    seguir = True
    while seguir:
        opcion = input("> ").strip()
        if opcion == "":
            seguir = False
        elif opcion == "1":
            print("\n------------------------------------------")
            estadisticas_general()
            print("------------------------------------------\n")
            print(menu_estadisticas)
        elif opcion == "2":
            print("\n------------------------------------------")
            estadisticas_ranking()
            print("------------------------------------------\n")
            print(menu_estadisticas)
        elif opcion == "3":
            print("\n------------------------------------------")
            estadisticas_jugador()
            print("------------------------------------------\n")
            print(menu_estadisticas)
        else:
            print("Opción no válida. Probá de nuevo o ENTER para volver.")
            print(menu_estadisticas)


def estadisticas_general():
    """
    Muestra las estadísticas tal como figuran en jugadores_registrados.

    Recorre los jugadores y muestra juegos, puntos y, si existe, precisión.
    """
    print("Estadísticas generales:\n")
    for jugador in jugadores_registrados:
        estadisticas = jugadores_registrados[jugador]
        linea = f"- {jugador}: Juegos: {estadisticas['juegos']}, Puntos: {estadisticas['puntos']}, Promedio: {estadisticas['promedio']}"
        print(linea)


def estadisticas_ranking():
    """
    Muestra el ranking de hasta 5 jugadores ordenados por promedio
    """
    print("\n==========================================")
    print("                 T O P   5               ")
    print("==========================================")

    ranking_jugadores = []
    for jugador in jugadores_registrados:
        ranking_jugadores.append([
            jugadores_registrados[jugador]["promedio"],
            jugadores_registrados[jugador]["puntos"],
            jugador
        ])
    ranking_jugadores.sort(reverse=True)

    limite = 5
    if len(ranking_jugadores) < 5:
        limite = len(ranking_jugadores)

    for posicion in range(0, limite):
        print(f"#{posicion + 1} // {ranking_jugadores[posicion][2]} // Promedio: {ranking_jugadores[posicion][0]}")

    print("\nIngresá ENTER para volver")
    seguir = True
    while seguir:
        respuesta = input("> ").strip().lower()
        if respuesta == "":
            seguir = False
        else:
            print("Ingresá ENTER para volver")


def estadisticas_jugador():
    """
    Permite ingresar un nombre y muestra sus estadísticas si existe.

    Usa definir_jugador() para tomar el nombre normalizado.
    """
    jugador = definir_jugador()
    if jugador in jugadores_registrados:
        datos = jugadores_registrados[jugador]
        print(f"{jugador}: Juegos: {datos['juegos']}, Puntos: {datos['puntos']}, Promedio: {datos['promedio']}")

    else:
        print(f"No hay registros para {jugador}.")



def main():
    """
    Menú principal del programa.

    Llama a bienvenida() para decidir si jugar o salir. Si se juega, pide el nombre, verifica o crea el jugador y entra en un bucle de partidas hasta que el jugador decida volver al menú.
    """
    activo = True
    while activo:
        jugar = bienvenida()
        if not jugar:
            print("Hasta la proxima!")
            return

        jugador = definir_jugador()
        iniciar_sesion(jugador)

        seguir = True
        while seguir:
            seguir, puntos = jugar_turno()
            actualizar_estadisticas(jugador, puntos)

main()