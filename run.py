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

from database import conectaBanco
from tts import textToSpeech
from actions import buscaUltimaPosicao, distanciaDirecao
import time

def main():
    try:
        conecta = conectaBanco()
        sinalGPS()

        while True:
            # posicao = buscaUltimaPosicao()
            gpsCompass = distanciaDirecao()
            print("teste")


    except :
        print "Ocorreu erro aplicacao inicia em 10 segundos"
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