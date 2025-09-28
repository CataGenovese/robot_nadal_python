
MIDA_TAULER = 20

class Robot:
    #init -> inicialitzem els valors del robot i taulell
    def __init__(self):
        self.x= 0
        self.y= 0
        self.velocitat= 1
        self.tauler_blocs = MIDA_TAULER

    #funcio per invertir l'eix de les Y
    def fila_tauler(self):
        #formula: (n_files -1) - l'eix de la Y actual
        #volta 1-> (20 -1) - 19 = 0 -> per tant la coordenada Y que abans era 19 passaria a ser la 0
        #volta 2-> (20 -1) -18 = 1 -> 1 (d'abaix cap a dalt)
        return self.tauler_blocs -1 - self.y

    #funció per verificar que el robot no surti dels limits
    def dins_limit(self, x, y):
        #si l'eix de les X sen va fora (cap a l'esquerra) || sen va cap a la dreta
        if x < 0 or x >= self.tauler_blocs:
            return False
        #si sen va cap abaix || cap a dalt
        if y < 0 or y >= self.tauler_blocs:
            return False
        #si no surt d'enlloc ens retorna true
        else:
            return True

    #funció per pujar Y segons la velocitat
    def dalt(self):
        posicio_y_actual= self.y + self.velocitat
        if self.dins_limit(self.x, posicio_y_actual):
            self.y = posicio_y_actual
        else:
            print("No pots sortir del taulell per dalt")

    #funció per baixar Y segons la velocitat
    def baix(self):
        posicio_y_actual= self.y - self.velocitat
        if self.dins_limit(self.x, posicio_y_actual):
            self.y= posicio_y_actual
        else:
            print("No pots sortir del taulell per baix!")

    #funcio per mouret cap a la dreta
    def dreta(self):
        posicio_x_actual= self.x + self.velocitat
        if self.dins_limit(posicio_x_actual, self.y):
            self.x= posicio_x_actual
        else:
            print("està sortint per la dreta")

    #funcio per mouret cap a lesquerra
    def esquerra(self):
        posicio_x_actual= self.x - self.velocitat
        if self.dins_limit(posicio_x_actual, self.y):
            self.x= posicio_x_actual
        else:
            print("està sortint per lesquerra")

    #incrementar la velocitat
    def accelerar(self):
        if(self.velocitat)< 5:
            self.velocitat += 1
        else:
            print("Ha superat el limit de velocitat")

    #decrementar la velocitat
    def frenar(self):
        if self.velocitat > 0:
            self.velocitat-=1
        else:
            print("No es pot incrementar la velocitat")

    #posicio actual
    def posicio(self):
        print(f"La posició del robot és ({self.x}, {self.y})")

    #funcio coordenades -> va despres del planol dels blocs
    def mostrar(self):
        print((f"Coordenades: ({self.x}, {self.y}"))

    #funcio per imrpimir la velocitat actual
    def velocitat_actual(self):
        print(f"La velocitat del robot és de {self.velocitat} m/s")

    #funcio per reiniciar la posició del robot
    def reiniciar(self):
        self.x= 0
        self.y= 0
        self.velocitat=1
