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
# Classe responsavel pelas ações
# do sistema

from database import conectaBanco
from tts import textToSpeech


def buscaUltimaPosicao():
    cursor = conectaBanco().cursor()
    cursor.execute("SELECT * FROM posicao_atual ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()
    cursor.close()
    return resultado


def distanciaDirecao():
    distDir = buscaUltimaPosicao()
    br = textToSpeech()
    cursor = conectaBanco().cursor()
    sql = ("SELECT *, (6371 * acos(cos(radians('%s')) * cos(radians(lat)) * cos(radians('%s')- radians(lng)) + "
           "sin(radians('%s')) * sin(radians(lat))))AS distance FROM coordenada HAVING distance <= '%s'")

    try:
        cursor.execute(sql, (distDir[1], distDir[2], distDir[1], 0.7))
        resultado = cursor.fetchall()
        print(resultado)

    except:
        print "Erro: O banco especificado nao foi encontrado"
        br.say("Erro O banco especificado nao foi encontrado")
        br.runAndWait()
