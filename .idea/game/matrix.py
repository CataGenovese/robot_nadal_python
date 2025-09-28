# Crear tablero 20x20 lleno de 🧱
tablero = []
for _ in range(20):
    fila = []
    for _ in range(20):
        fila.append("🧱")
    tablero.append(fila)


#tauler[19][0]="🤖"

#actualment per a que el robot estigui a la part esquerra inferior la coordenada es (19,0), quan hauria de ser (0,0)
#fila_robot= 0
#columna_robot=0
#index 19 (20-1)
fila_tablero= mida_tauler -1
# fila_tablero - fila_robot serveix per invertir les coordenades
tauler[fila_tablero-fila_robot][columna_robot] = "🤖"

for fila in tauler:
    print("".join(fila))