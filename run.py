# ! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: William Lopes
# Data: 14/08/2019
# Linguagem: Python

# ========= IMPORTANTE ===========
# O codigo esta livre para usar,
# citar e compartilhar desde que
# mantida sua fonte e seu autor.
# Obrigado.

from database import conectDatabase
from tts import textToSpeech
from actions import *
import time

def main():
    try:
        # conecta = conectDatabase()
        # sinalGPS()
        # pointA = -26.915143, -49.081917
        # pointB = -26.91534000, -49.08198400
        # bearing = calculate_initial_compass_bearing(pointA, pointB)
        # print(bearing)

        while True:
            # posicao = buscaUltimaPosicao()
            gpsCompass = distanciaDirecao()
            print("teste")


    except:
        print("Ocorreu erro aplicacao inicia em 10 segundos")
        time.sleep(10)
        main()


def sinalGPS():
    statusSinal = True
    br = textToSpeech()

    try:
        print("Estabelecido sinal de GPS")
        br.say("Estabelecido sinal de GPS")
        br.runAndWait()
    except:
        print("teste")

    return statusSinal


if __name__ == '__main__':
    main()