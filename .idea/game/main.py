#https://elpythonista.com/listas-python python matrix

from Robot import Robot  #importem la classe Robot on tenim els metodees
ROBOT_CHAR = "🤖"
BLOQUE_CHAR = "🧱"
MIDA_TAULER = 20

#funcio per crear el planol
def creacio_tauler():
    tauler = []
#recorrem les files
    for fila_matriu in range(MIDA_TAULER):
        fila = [] #crea una nova fila buida
        for columna_matriu in range(MIDA_TAULER): #recorrem les columnes de les files
            fila.append(BLOQUE_CHAR) #afegim un mao a cada cela de la fila
        tauler.append(fila) #quan la fila arribi a 20 celes, lafegim al tauler
    return tauler

# Funció per actualitzar el taulell amb la posició del robot
def actualitzar_tauler(tauler, robot):
    #tornem a recorrer el tauler
    for y in range(MIDA_TAULER):
        for x in range(MIDA_TAULER):
            #posem en cada cela el mao
            tauler[y][x] = BLOQUE_CHAR
            #posem el robot a la seva posicio actual
    tauler[robot.fila_tauler()][robot.x] = ROBOT_CHAR

#Imprimir taulell
def mostrar_tauler(tauler):
    for fila in tauler:
        print("".join(fila))

#main del programa
def main():
    #definim els objectes i els metodes que farem servir
    robot= Robot()
    tauler= creacio_tauler()
    actualitzar_tauler(tauler, robot)
    mostrar_tauler(tauler)

#diccionari per mapear instruccions a metodes
#clau: dalt
#valor: funcio
    comandes = {
    "DALT": robot.dalt,
    "BAIX": robot.baix,
    "DRETA": robot.dreta,
    "ESQUERRA": robot.esquerra,
    "ACCELERAR": robot.accelerar,
    "FRENAR": robot.frenar,
    "POSICIO": robot.posicio,
    "VELOCITAT": robot.velocitat_actual,
    "REINICIAR": robot.reiniciar
    }

    input_usuari = ""
    while input_usuari != "END":
        input_usuari= input("> ")

        if input_usuari == "MOSTRAR":
            #actualitzem la posició del robot
            actualitzar_tauler(tauler, robot)
            #mostrem el tauler i les coordenades del robot
            mostrar_tauler(tauler)
            robot.posicio()

        #si un dels inputs existeix a comandes
        elif input_usuari in comandes:
            comandes[input_usuari]()

        else:
            print("comanda no reconeguda")

main()






