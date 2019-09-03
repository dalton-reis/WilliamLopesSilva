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

from database import conectDatabase
from tts import textToSpeech
# import py_qmc5883l
import math


def setDirection(resultBearing):
    if resultBearing > 338 or resultBearing < 22:
        bearing = "a frente"
    elif resultBearing > 22 and resultBearing < 113:
        bearing = "a frente a direita"
    elif resultBearing > 113 and resultBearing < 158:
        bearing = "a direita"
    elif resultBearing > 158 and resultBearing < 203:
        bearing = "atrás a direita"
    elif resultBearing > 203 and resultBearing < 248:
        bearing = "atrás"
    elif resultBearing > 203 and resultBearing < 248:
        bearing = "atrás a esquerda"
    elif resultBearing > 248 and resultBearing < 293:
        bearing = "a esquerda"
    elif resultBearing > 293 and resultBearing < 338:
        bearing = "a frente a esquerda"
    return bearing

def buscaUltimaPosicao():
    cursor = conectDatabase().cursor()
    cursor.execute("SELECT * FROM posicao_atual ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()
    cursor.close()
    return resultado


def distanciaDirecao():
    currentPosition = gps()
    currentBearing = compass()
    br = textToSpeech()
    cursor = conectDatabase().cursor()
    sql = ("SELECT *, (6371 * acos(cos(radians('%s')) * cos(radians(lat)) * cos(radians('%s')- radians(lng)) + "
           "sin(radians('%s')) * sin(radians(lat))))AS distance FROM coordenada HAVING distance <= '%s'")

    try:
        cursor.execute(sql, (currentPosition[0], currentPosition[1], currentPosition[0], 0.7))
        result = cursor.fetchall()

        for data in result:
            lat = float(data[1])
            lng = float(data[2])
            pointInterest = data[3]
            distanceMeters = str(int(round(data[4], 4) * 1000))
            destinationPosition = lat, lng
            finishBearingPosition = calculate_initial_compass_bearing(currentPosition, destinationPosition)
            if currentBearing < finishBearingPosition:
                resultBearing = finishBearingPosition - currentBearing
            else:
                auxBearing = currentBearing - finishBearingPosition
                resultBearing = 360 - auxBearing

            bearing = setDirection(resultBearing)
            br.say(pointInterest + " a " + distanceMeters + " metros " + bearing)
            br.runAndWait()
            print("teste")

    except:
        br.say("Nenhum ponto de interesse por perto")
        br.runAndWait()


def compass():
    # br = textToSpeech()
    # sensor = py_qmc5883l.QMC5883L()
    # sensor.declination = -19, 31
    #
    # try:
    #     return sensor.get_bearing()
    #
    # except:
    #     print("Erro: Não foi possivel obter retorno da bussola")
    #     br.say("Erro não foi possivel obter retorno da bussola")
    #     br.runAndWait()
    # TODO mock de dados da direção atual para teste local
    bearing = 10.0
    return bearing


def gps():
    # TODO mock de dados da posição atual para teste ate instalar o chip de GPS
    lat = -26.915143
    lng = -49.081917
    return lat, lng


def calculate_initial_compass_bearing(pointA, pointB):
    startx, starty, endx, endy = pointA[0], pointA[1], pointB[0], pointB[1]
    angle = math.atan2(endy - starty, endx - startx)
    if angle >= 0:
        return math.degrees(angle)
    else:
        return math.degrees((angle + 2 * math.pi))
