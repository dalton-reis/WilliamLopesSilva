# ! /usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: William Lopes
# Data: 14/08/2019
# Language: Python

# ========= IMPORTANT ===========
# # # The code is free to use,
# # # cite and share as long as its
# # # source and author are maintained.
# # # Thank you.

# =========== RESUME =============
# Class responsible for database
# connection

import pymysql
from tts import textToSpeech
# =========================================================================================================================
def conectDatabase():
    HOST = "localhost"
    USER = "root"
    PASSWD = "Wiiu12345*"
    BASE = "vision"

    br = textToSpeech()
    try:
        conect = pymysql.connect(HOST, USER, PASSWD)
        conect.select_db(BASE)
        print("Banco conectado")
        # br.say("Banco conectado")
        # br.runAndWait()
    except :
        print("Erro: O banco especificado nao foi encontrado")
        # br.say("Erro O banco especificado nao foi encontrado")
        # br.runAndWait()

    return conect
