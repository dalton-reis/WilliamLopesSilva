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

# =========== Resumo =============
# Classe para testes

from threading import Thread
import time
from tts import textToSpeech
from actions import distanciaDirecao

run = False
count = 0


def func1():
    global run
    br = textToSpeech()
    br.say("Iniciando reconhecimento de voz")
    br.runAndWait()
    while run:
        pontosInteresses = distanciaDirecao()
        for x in pontosInteresses:
            br.say(x)
            br.runAndWait()
            print("Encontrado " + str(x))
        print('Working 1')
        time.sleep(2)


def func2():
    global run, count
    while True:
        print('Working 2')
        count += 1
        if count > 3:
            if not run:
                run = True
                th1 = Thread(target=func1)
                th1.start()
        time.sleep(2)


if __name__ == "__main__":
    th = Thread(target=func2)
    th.start()
