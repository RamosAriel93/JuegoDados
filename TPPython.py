# condiciones del scrip para juego de dados:
# 1)Simular el lanzamiento de dos dados de seis caras.
# 2)Para ganar la mano, la suma entre ambos dados debe ser igual a cuatro.
# 3)Si la suma entre ambos dados es menor a cuatro, entonces se pierde esta mano.
# 4)Si la suma entre ambos dados es mayor a cuatro, debe volver a tirar.

from random import randint


def juego_de_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    suma_dado = dado1 + dado2

    print("Su resultado en esta mano es :", suma_dado)
    if suma_dado == 4:
        print(" *** HAS GANADO ESTA MANO! ***")
    elif suma_dado <= 4:
        print(" Pierdes esta mano, suerte en la proxima! ")
    else:
        while suma_dado > 4:
            print(" (vuelves a tirar nuevamente) ")
            dado1 = randint(1, 6)
            dado2 = randint(1, 6)
            suma_dado = dado1 + dado2

            print("Su resultado en esta mano es :", suma_dado)
            if suma_dado == 4:
                print(" *** HAS GANADO ESTA MANO! *** ")
            elif suma_dado <= 4:
                print("Pierdes esta mano, suerte en la proxima! ")


juego_de_dados()
