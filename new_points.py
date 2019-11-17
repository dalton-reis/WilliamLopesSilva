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
import csv, sys
import pymysql
from decimal import Decimal
from database import conectDatabase
from tts import save_audio_tts
from unicodedata import normalize

file_name = 'C://temp//coordenada.csv'


def query_pont_interest(lat, lng):
    cursor = conectDatabase().cursor()
    cursor.execute("""SELECT * FROM ponto_interesse where lat = %s and lng = %s"""
                   % (lat, lng))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return True
    return False


def new_audio_point_interest(lat, lng):
    cursor = conectDatabase().cursor()
    cursor.execute("""SELECT * FROM ponto_interesse where lat = %s and lng = %s"""
                   % (lat, lng))
    result = cursor.fetchone()
    cursor.close()
    if result:
        save_audio_tts(result[0], result[3])
    elif not result:
        print("Ponto de interesse não encontrado!")


def insert_pont_interest(lat, lng, pontoInteresse):
    cursor = conectDatabase().cursor()
    pontoInteresseUnicode = normalize('NFKD', pontoInteresse).encode('ASCII', 'ignore').decode('ASCII')
    try:
        cursor.execute("""INSERT INTO ponto_interesse (lat,lng,ponto_interesse) VALUES (%s, %s, %s)""",
                       (Decimal(lat), Decimal(lng), pontoInteresseUnicode))
    except pymysql.Error as e:
        print("Erro: " + cursor)


def read_file():
    global file_name
    with open(file_name, newline='', encoding='utf-8') as file:
        next(file)
        reader = csv.reader(file)
        try:
            for line in reader:
                p = line[0].split(';')
                if not query_pont_interest(p[0], p[1]):
                    insert_pont_interest(p[0], p[1], p[2])
                    new_audio_point_interest(p[0], p[1])
                    print("Ponto de interesse %s cadastrado com sucesso!" % (p[2]))
                else:
                    print("Ponto de interesse %s já cadastrado!" % (p[2]))
        except csv.Error as e:
            sys.exit('ficheiro %s, linha %d: %s' % (file_name, reader.line_num, e))
