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
import time
from database import statusDatabase
from new_points import read_file


def have_internet():
    return True


def validation_task():
    validation = True
    while validation:
        if statusDatabase():
            print("Banco de dados conectado")
            validation = False
        else:
            print("Banco de dados desconectado, proxima tentativa em 10 segundos")
            time.sleep(10)

    if not validation and have_internet():
        read_file()

    print("chama as task após validar")
    # t1 = multiprocessing.Process(target=task_speech)
    # t2 = multiprocessing.Process(target=task_black_glasses)
    # t1.start()
    # t2.start()


if __name__ == "__main__":
    validation_task()
