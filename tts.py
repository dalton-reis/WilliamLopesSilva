# ! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: William Lopes
# Data: 14/08/2019
# Linguagem: Python

# ========= IMPORTANTE ===========
# # # O codigo esta livre para usar,
# # # citar e compartilhar desde que
# # # mantida sua fonte e seu autor.
# # # Obrigado.

# =========== Resumo =============
# Classe responsavel pela conversão
# de texto para fala

import pyttsx3

def textToSpeech():
    br = pyttsx3.init()
    br.setProperty('voice', b'brazil')
    br.setProperty('rate', 200)

    return br


def voice(data):
    br = textToSpeech()
    br.say(data)
    br.runAndWait()
    br.stop()
