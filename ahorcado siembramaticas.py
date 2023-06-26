
import os  #establecemos la libreria os
import random #establecemos el comando random, para aleateorizar la palabra que se va a jugar
import time # establecemos el comando tiempo, para generar la cuenta regresiva del inicio del juego

palabraAdivinada = [] #queda en intervalo abierto la palabra aletoria
letrasEscritas = [] #queda en intervalo abierto las letras que vamos a escribir  
intentos = 6 #numero de intentos posibles
palabraSecretaAjustes = "siembramaticas" #establecemos la contraseña para ajustar las cofiguraciones
nombreArchivoGrupos = "palabras.txt" #establecemos el archivo de las palabras

def LimpiarPantalla(): 
    print("\n"* 40)

def ImprimirEntrada():
    print("BIENVENIDO AL JUEGO DE")
    print("       .__                                     .___     ")  #creamos la portada de nuestro ahorcado
    print("_____  |  |__   ___________   ____ _____     __| _/____  ")
    print("\__  \ |  |  \ /  _ \_  __ \_/ ___\\__  \   / __ |/  _ \ ")
    print(" / __ \|   Y  (  <_> )  | \/\  \___ / __ \_/ /_/ (  <_> )")
    print("(____  /___|  /\____/|__|    \___  >____  /\____ |\____/ ")
    print("     \/     \/                   \/     \/      \/       ")
    print("CREADORES: SANTIAGO DIAZ DEVIA, SANTIAGO GALINDO HERNANDEZ")

def prepararPalabra(original): #establecemos el funcionamiento del ahorcado, poniendo en global la palabra usada
    global palabraAdivinada
    original = original.lower()
    palabraAdivinada = []
    for letra in original:
        palabraAdivinada.append({
            "letra": letra,
            "adivinada": False,
        })


def imprimirPalabra(): #es decir la mecanica de adivinar una palabra letra por letra
    for letraCompuesta in palabraAdivinada:
        if letraCompuesta["adivinada"]:
            print(letraCompuesta["letra"], end="")
        else:
            print("-", end="")
    print("")


def imprimirPalabraOriginal(): #se establece la palabra que se va a elejir
    for letraCompuesta in palabraAdivinada:
        print(letraCompuesta["letra"], end="")


def descubrirLetra(letraDeUsuario): #se establece la funcion de descubrir cada letra 
    global palabraAdivinada  #en el dado caso que se adivine ser aportada a la frase 
    global letrasEscritas #  en el caso de que no entonces no ser reportada y restar un intento
    global intentos
    letraDeUsuario = letraDeUsuario.lower()
    if letraDeUsuario in letrasEscritas:
        return
    else:
        letrasEscritas.append(letraDeUsuario)
    if not letraEstaEnPalabra(letraDeUsuario):
        intentos -= 1
    else:
        for letraCompuesta in palabraAdivinada:
            if letraCompuesta["letra"] == letraDeUsuario:
                letraCompuesta["adivinada"] = True


def letraEstaEnPalabra(letra):   #se define la funcion de sumar una letra a la palabra al acertar
    global palabraAdivinada
    for letraCompuesta in palabraAdivinada:
        if letraCompuesta["letra"] == letra:
            return True
    return False


def imprimirAhorcado():
    if intentos == 0:
        print("""
                        ____
                       |    |
                     |_O_   |
                       | |_ |
                       |    |
                      / \   |
                     _| |_  |
                      ______|
        """)
    elif intentos == 1:
        print("""
                        ____
                       |    |
                     |_O_   |
                       | |_ |
                       |    |
                        \   |
                        |_  |
                      ______|
        """)
    elif intentos == 2:
        print("""
                        ____
                       |    |
                     |_O_   |
                       | |_ |
                       |    |
                            |
                            |
                      ______|
        """)
    elif intentos == 3:
        print("""
                        ____
                       |    |
                     |_O_   |
                         |_ |
                            |
                            |
                            |
                      ______|
        """)
    elif intentos == 4:
        print("""
                        ____
                       |    |
                       O_   |
                         |_ |
                            |
                            |
                            |
                      ______|
        """)
    elif intentos == 5:
        print("""
                        ____
                       |    |
                       O    |
                            |
                            |
                            |
                            |
                      ______|
        """)
    elif intentos == 6:
        print("""
                        ____
                       |    |
                            |
                            |
                            |
                            |
                            |
                      ______|
        """)

def dibujarIntentos():
    print("Intentos restantes: " + str(intentos)) #es la funcion entre los intentos restantes y la evolucion del dibujo


def haGanado(): #establecemos la funcion al adivinar la palabra
    global palabraAdivinada
    for letra in palabraAdivinada:
        if not letra["adivinada"]:
            return False
    return True



def instrucciones(): #definimos e indicamos las reglas
    print("""
INSTRUCCIONES
El objetivo de este juego es descubrir una palabra adivinando las letras que la componen.
1. Debes seleccionar de qué conjunto de palabras quisieras jugar
2. Inicias con """ + str(intentos) + "vidas" +
          """
         3. Ingresa una letra que creas vaya en la palabra a adivinar
          Suerte con el juego
          """)


def obtenerPalabra(): 
    print("Jugar con: ")
    grupos = obtenerGrupos()
    indice = imprimirGruposYSolicitarIndice(grupos)
    grupo = grupos[indice]
    palabras = obtenerPalabrasDeGrupo(grupo)
    return random.choice(palabras) #se define la aleatoriedad de la palabra a jugar

def cuenta_regresiva():
    tiempo = 10 # Tiempo inicial de la cuenta regresiva (en segundos)
    print("¡Comienza el juego!")
    print("Tienes", tiempo, "segundos para jugar.")
    tiempo_inicial = time.time() # Guardar el tiempo inicial
    
    while tiempo > 0:
        tiempo_restante = tiempo - int(time.time() - tiempo_inicial) # Calcular el tiempo restante
        if tiempo_restante <= 0:
            break
        print("Tiempo restante:", tiempo_restante, "segundos")
        time.sleep(1) # Esperar 1 segundo
        
    print("Tiempo agotado.")

cuenta_regresiva()

def jugar(): #se define todo el proceso de la opcion jugar
    global letrasEscritas
    global intentos
    intentos = 6
    letrasEscritas = []
    palabra = obtenerPalabra()
    prepararPalabra(palabra) 
    while True:
        imprimirAhorcado() #se dibuja el ahorcado
        dibujarIntentos() #se presentan los intentos de juego
        imprimirPalabra() # se presentan los espacios de la palabra
        descubrirLetra(input("Ingresa la letra: ")) #se ingresan las letras
        if intentos <= 0:
            print("Perdiste. La palabra era: ") #secuencia al perder
            imprimirPalabraOriginal()
            return
        if haGanado():
            print("Ganaste") #secuencia al ganar
            return


def ajustes(): #proceso ventan de ajustes
    if input("Ingrese la contraseña: ") != palabraSecretaAjustes: #ingreso de la contraseña
        print("Contraseña incorrecta") #mensaje al ser incorrecta la contraseña
        return #al ingresar la correcta se dan paso a los ajustes
    menu = """ 
1. Eliminar grupo de palabras
2. Crear grupo de palabras
3. Modificar grupo de palabras
"""
    grupos = obtenerGrupos()

    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion > 3:
        print("No válido")
        return
    if eleccion == 1:
        eliminarGrupoDePalabras(grupos) #funcion de eliminar grupo de palabras
    elif eleccion == 2:
        crearGrupoDePalabras(grupos) #funcion de crear grupo de palabras
    elif eleccion == 3:
        modificarGrupoDePalabras(grupos) #funcion de modificacion de grupo de palabras


def eliminarGrupoDePalabras(grupos): 
    indice = imprimirGruposYSolicitarIndice(grupos)
    grupoEliminado = grupos[indice]
    del grupos[indice]
    os.unlink(grupoEliminado + ".txt") #con la libreria os se accede al archivo para eliminar el grupo
    escribirGrupos(grupos) 


def imprimirGruposYSolicitarIndice(grupos):
    for i, grupo in enumerate(grupos):
        print(f"{i + 1}. {grupo}")
    return int(input("Seleccione el grupo: ")) - 1 #mensaje y ejecucion de eliminar el grupo


def crearGrupoDePalabras(grupos): 
    grupo = input("Ingrese el nombre del grupo: ") #introduce nombre del grupo
    palabras = solicitarPalabrasParaNuevoGrupo()
    escribirPalabrasDeGrupo(palabras, grupo) #introducen la palabras del grupo
    grupos.append(grupo) 
    escribirGrupos(grupos)
    print("Grupo creado correctamente") #se creo el grupo


def escribirGrupos(grupos): 
    with open(nombreArchivoGrupos, "w") as archivo:
        for grupo in grupos:
            archivo.write(grupo + "\n") # se accede al archivo para integrar el nuevo grupo


def escribirPalabrasDeGrupo(palabras, grupo):
    with open(grupo + ".txt", "w") as archivo: #se accede al archivo para integrar las palabras del nuevo grupo
        for palabra in palabras:
            archivo.write(palabra + "\n")


def solicitarPalabrasParaNuevoGrupo():
    palabras = []
    while True:
        palabra = input("Ingrese la palabra. Deje la cadena vacía si quiere terminar: ") #ingresan las palabras del nuevo grupo
        if palabra == "":
            return palabras
        palabras.append(palabra)


def modificarGrupoDePalabras(grupos): 
    indice = imprimirGruposYSolicitarIndice(grupos)
    grupoQueSeCambia = grupos[indice]
    palabras = obtenerPalabrasDeGrupo(grupoQueSeCambia)
    menu = """
1. Cambiar una palabra
2. Agregar una palabra
3. Eliminar una palabra
Seleccione: """
    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion > 3:
        print("No válido")
        return
    if eleccion == 1:
        cambiarUnaPalabra(grupoQueSeCambia, palabras) #fincion cambio de palabra
    elif eleccion == 2:
        agregarUnaPalabra(grupoQueSeCambia, palabras) #funcion agragar una palabra
    elif eleccion == 3:
        eliminarUnaPalabra(grupoQueSeCambia, palabras) #funcion eliminar una palabra


def cambiarUnaPalabra(grupo, palabras): #define el proceso de cambio de palabra
    indice = imprimirPalabrasYSolicitarIndice(palabras)
    palabraCambiada = palabras[indice]
    print("Se cambia la palabra " + palabraCambiada) 
    nuevaPalabra = input("Ingrese la nueva palabra: ")
    palabras[indice] = nuevaPalabra
    escribirPalabrasDeGrupo(palabras, grupo)
    print("Palabra cambiada correctamente")


def agregarUnaPalabra(grupo, palabras): #define el proceso de adicion de palabra
    palabra = input("Ingrese la palabra que se agrega: ")
    palabras.append(palabra)
    escribirPalabrasDeGrupo(palabras, grupo)
    print("Palabra agregada correctamente")


def eliminarUnaPalabra(grupo, palabras): #define el proceso de eliminacion de palabra
    indice = imprimirPalabrasYSolicitarIndice(palabras)
    del palabras[indice]
    escribirPalabrasDeGrupo(palabras, grupo)
    print("Palabra eliminada correctamente")


def imprimirPalabrasYSolicitarIndice(palabras): 
    for i, palabra in enumerate(palabras):
        print(f"{i + 1}. {palabra}")
    return int(input("Seleccione la palabra: ")) - 1


def obtenerGrupos(): # define el proceso de integracion de un nuevo grupo al archivo
    grupos = []
    with open("palabras.txt") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            grupos.append(linea)
    return grupos


def obtenerPalabrasDeGrupo(grupo): #define en el archivo las palabras del grupo
    palabras = []
    with open(grupo + ".txt") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            palabras.append(linea)
    return palabras


def prepararArchivo(): #define la preparacion del archivo con las palbra nuevas en el nuevo grupo
    if not os.path.isfile(nombreArchivoGrupos):
        with open(nombreArchivoGrupos, "w") as archivo:
            archivo.write("")


def menu_principal(): # menu
    LimpiarPantalla() 
    ImprimirEntrada() # portada
    menu = """
1. Jugar
2. Instrucciones
3. Ajustes
4. Salir
Seleccione: """
    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion >= 4: #al oprimir 4 o otro numero mayor a 4 se sale del juego
        exit()
    if eleccion == 1: #al oprimir uno se ingresa al juego
        jugar()
    elif eleccion == 2: #al oprimir 2 se dirije a las instrucciones
        instrucciones()
    elif eleccion == 3: #al oprimir 3 se accede a los ajustes
        ajustes()


def main(): #se define la funcion main del programa
    prepararArchivo()
    while True:
        menu_principal()


main()  