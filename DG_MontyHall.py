import random as rd
import numpy as np

#Funcion para establecer lo que hay detras de cada puerta
def sort_doors():
    #Arreglo que cuenta con los valores tras las puertas
    x=[ 'goat' , 'goat' , 'car' ]
    #Variar el orden del arreglo
    rd.shuffle(x)
    return x

#Funcion para establecer la eleccion del participante
def choose_door():
    #Arreglo que cuenta con las posibles elecciones
    x=np.array([0,1,2])
    #Eleccion del participante
    return np.random.choice(x)

#Funcion para revelar una puerta
def reveal_door(lista, choice):
    #Iteracion en la lista que entra como parametro
    for i in range(3):
        #Se busca la puerta que no sea seleccionada por el participante y tenga una cabra
        if(i!=choice and lista[i]=='goat'):
            #Se cambia esta posicicion a un nuevo valor 'GOAT_MONTY'
            lista[i]='GOAT_MONTY'
    return lista

#Funcion para acabar el juego
def finish_game(lista,choice,change):
    #Se retorna la eleccion del jugador, si este no decidio cambiarla
    if(change==False):
        return lista[choice]
    else:
        #Se recorre la lista que entra como parametro
        for i in range(3):
            #Se busca la puerta que no es 'GOAT_MONTY' ni la elegida inicialmente por el participante
            if(i!=choice and lista[i]!='GOAT_MONTY'):
                return lista[i]

#Se simula el juego con 1000 intentos
def simulation(change):
    #Variable para guardar los casos favorable
    contar=0.0
    #Iteracion de los mil juegos
    for i in range(1000):
        #Se establece el premio detras de todas las puertas
        y=sort_doors()
        #Se establece la eleccion del jugador
        c=choose_door()
        #Se revela una puerta
        y=reveal_door(y,c)
        #Se revelan todas las puertas y se termina el juego
        r=finish_game(y,c,change)
        #Se establece si se obtuvo el premio o no
        if(r=='car'):
            contar=contar+1.0
    #Se encuentra la probabilidad respectiva
    return contar/1000.0

#Se imprime el mensaje correspondiente a la probabilidad respectiva si se hizo el cambio de puerta o no
print "Cuando hubo un cambio de la puerta la probabilidad fue: ", simulation(True), ". Por otra parte si el jugador no cambia la puerta la probabilidad es de: ", simulation(False)
