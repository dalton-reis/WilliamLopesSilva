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
# Classe responsavel pela conexao
# com o banco de dados

import pymysql
from tts import textToSpeech
# =========================================================================================================================
def conectaBanco():
    HOST = "localhost"
    USER = "root"
    PASSWD = "Wiiu12345*"
    BANCO = "vision"

    br = textToSpeech()
    try:
        conecta = pymysql.connect(HOST, USER, PASSWD)
        conecta.select_db(BANCO)
        print "Banco conectado"
        # br.say("Banco conectado")
        # br.runAndWait()
    except :
        print "Erro: O banco especificado nao foi encontrado"
        # br.say("Erro O banco especificado nao foi encontrado")
        # br.runAndWait()

    return conecta