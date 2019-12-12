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
import pymysql

from database import conectDatabase
import math
import sys

import pynmea2
import serial
import time
import py_qmc5883l

#
sensor = py_qmc5883l.QMC5883L()
ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)

resultdistanciaDirecao = []
points_result = []


def setDirection(resultBearing):
    if resultBearing > 338 or resultBearing < 22:
        bearing = "a_frente"
    elif resultBearing > 22 and resultBearing < 68:
        bearing = "a_frente_a_direita"
    elif resultBearing > 68 and resultBearing < 113:
        bearing = "a_direita"
    elif resultBearing > 113 and resultBearing < 158:
        bearing = "atras_a_direita"
    elif resultBearing > 158 and resultBearing < 203:
        bearing = "atras"
    elif resultBearing > 203 and resultBearing < 248:
        bearing = "atras_a_esquerda"
    elif resultBearing > 248 and resultBearing < 293:
        bearing = "a_esquerda"
    elif resultBearing > 293 and resultBearing < 338:
        bearing = "a_frente_a_esquerda"
    return bearing

def distanciaDirecao():
    global resultdistanciaDirecao, points_result
    resultdistanciaDirecao = []
    currentPosition = gps()
    currentBearing = compass()
    resut = []
    cursor = conectDatabase().cursor()
    sql = ("SELECT *, (6371 * acos(cos(radians('%s')) * cos(radians(lat)) * cos(radians('%s')- radians(lng)) + "
           "sin(radians('%s')) * sin(radians(lat))))AS distance FROM ponto_interesse HAVING distance <= '%s'")

    try:
        cursor.execute(sql, (currentPosition[0], currentPosition[1], currentPosition[0], 0.05))
        result = cursor.fetchall()
        for data in result:
            id = int(data[0])
            lat = float(data[1])
            lng = float(data[2])
            pointInterest = str(id) + "_" + data[3]
            distanceMeters = str(int(round(data[4], 4) * 1000)) + "_" + str("metros")
            destinationPosition = lat, lng
            finishBearingPosition = calculate_initial_compass_bearing(currentPosition, destinationPosition)
            if currentBearing < finishBearingPosition:
                resultBearing = finishBearingPosition - currentBearing
            else:
                auxBearing = currentBearing - finishBearingPosition
                resultBearing = 360 - auxBearing

            bearing = setDirection(resultBearing)
            points_result.append(pointInterest)
            points_result.append(distanceMeters)
            points_result.append(bearing)
            resultdistanciaDirecao.append(points_result)
            points_result = []

    except:
        print("Nenhum ponto de interesse por perto")

    return resultdistanciaDirecao

def compass():
    # sensor.declination = -19.31
    # bearing = sensor.get_bearing()
    # bearing = 145 #shopping
    bearing = 110  # furb caixa dgua
    # bearing = 120
    return bearing

def gps():
    # while True:
    #    data = ser.readline()
    #    if sys.version_info[0] == 3:
    #        data = data.decode("utf-8", "ignore")
    #    if data[0:6] == '$GNGGA':
    #        newmsg = pynmea2.parse(data)
    #        lat = round(newmsg.latitude, 6)
    #        lng = round(newmsg.longitude, 6)
    #        break;
    # lat = -26.907058
    # lng = -49.079089
    # lat = -26.919343#shopping
    # lng = -49.069266#shopping
    lat = -26.905754  # furb caixa dgua
    lng = -49.079427  #furb caixa dgua
    return lat, lng


def status_gps_compass():
    compass_data = compass()
    gps_data = gps()
    if compass_data and gps_data:
        return True
    return False

def calculate_initial_compass_bearing(pointA, pointB):
    startx, starty, endx, endy = pointA[0], pointA[1], pointB[0], pointB[1]
    angle = math.atan2(endy - starty, endx - startx)
    if angle >= 0:
        return math.degrees(angle)
    else:
        return math.degrees((angle + 2 * math.pi))

# if __name__ == "__main__":
#     status_gps_compass()
