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

def buscaUltimaPosicao():
    cursor = conectaBanco().cursor()
    cursor.execute("SELECT * FROM posicao_atual ORDER BY id DESC LIMIT 1")
    resultadoCount = cursor.fetchall()
    for dadosTeste in resultadoCount:
        lat = dadosTeste[1]
        lng = dadosTeste[2]
        direcao = dadosTeste[3]

    return lat,lng,direcao

def distanciaDirecao():
    distDir = buscaUltimaPosicao()
