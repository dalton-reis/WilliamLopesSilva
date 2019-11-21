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

import speech_recognition as sr
import multiprocessing, ctypes
import time
from actions import distanciaDirecao
from database import statusDatabase
from new_points import read_file
from tts import play_audio_tts
from connect_wifi_bluetooth import have_internet

task_black = multiprocessing.Value(ctypes.c_bool, False)  # (type, init value)
task_main = multiprocessing.Value(ctypes.c_bool, True)  # (type, init value)
tts_on = multiprocessing.Value(ctypes.c_bool, False)  # (type, init value)
lock = multiprocessing.Manager().Lock()
keywords = [("start", 1), ("stop", 1), ("offline", 1), ]


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
    t1 = multiprocessing.Process(target=task_speech)
    t2 = multiprocessing.Process(target=task_black_glasses)
    t1.start()
    t2.start()

def task_speech():
    global task_main, task_black, keywords, tts_on
    print("Iniciando reconhecimento de voz")
    play_audio_tts("start_speech")
    print("Thread: Microfone")
    microfone = sr.Recognizer()

    while task_main:
        if not tts_on.value:
            with sr.Microphone() as source:
                microfone.adjust_for_ambient_noise(source)
                print("Diga alguma coisa: ")
                audio = microfone.listen(source)
            try:
                # Passa o audio para o reconhecedor de padroes do speech_recognition
                frase = microfone.recognize_sphinx(audio, keyword_entries=keywords, grammar='Grammar.jsgf')
                print("Voce disse:", frase)
                # Após alguns segundos, retorna a frase falada
                if "start" in frase:
                    play_audio_tts("start_black")
                    with lock:
                        task_black.value = True
                        tts_on.value = True
                    print("Recebido o comando para iniciar a Aplicação: ", frase)
                elif "stop" in frase:
                    play_audio_tts("stop_black")
                    with lock:
                        task_black.value = False
                        tts_on.value = False
                    print("Recebido o comando para parar a Aplicação: ", frase)
                elif "offline" in frase:
                    play_audio_tts("offline")
                    with lock:
                        task_black.value = False
                        task_main.value = False
                    print("Recebido o comando para desligar a Aplicação: ", frase)
                else:
                    print("O comando " + frase + " não é valido")
            except sr.UnknownValueError:
                print("Não entendi favor repetir")


def task_black_glasses():
    global task_main, task_black, tts_on
    print("Executando black glasses")
    while task_main.value:
        if task_black.value:
            with lock:
                tts_on.value = True
            pontosInteresses = distanciaDirecao()
            play_audio_tts(pontosInteresses)
            with lock:
                tts_on.value = False
            time.sleep(30)
        else:
            print("Black glasses aguardando comando para iniciar!")
            time.sleep(5)

if __name__ == "__main__":
    validation_task()
