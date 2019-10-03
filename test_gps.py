#!/usr/bin/python3
import sys
# import pynmea2
# import serial
import time
from datetime import datetime


# import py_qmc5883l
# ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

def gps():
    # TODO mock de dados da posição atual para teste ate instalar o chip de GPS
    lat = -26.915143
    lng = -49.081918
    returnCoordenada = str(lat) + ";" + str(lng) + ";"
    return returnCoordenada


while True:
    # data = ser.readline()
    # if sys.version_info[0] == 3:
    #     data = data.decode("utf-8","ignore")
    # if data[0:6] == '$GNGGA':
    #     newmsg=pynmea2.parse(data)
    #     lat=round(newmsg.latitude, 6)
    #     lng=round(newmsg.longitude, 6)
    #     gps = "Latitude=" + str(lat) + " and Longitude=" + str(lng)
    #     print(gps)
    #     time.sleep(0.3)
    arquivo = open('C://Users//william.silva//Desktop//Furb//TCC2//coordenadas.txt', 'r')  # Abra o arquivo (leitura)
    conteudo = arquivo.readlines()
    conteudo.append(gps() + str(datetime.now()) + "\n\n")  # insira seu conteúdo

    arquivo = open('C://Users//william.silva//Desktop//Furb//TCC2//coordenadas.txt',
                   'w')  # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

    arquivo.close()
    time.sleep(5.0)
