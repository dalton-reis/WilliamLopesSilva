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
import threading
from tts import voice
import speech_recognition as sr
import time
from datetime import datetime
from actions import distanciaDirecao

execute_black = False
cron = 0.0
keywords = [("google", 1), ("stop", 1), ("offline", 1), ]
curren_minute_initial = datetime.now()


def task_speech():
    global cron, execute_black, curren_minute_initial
    voice("Iniciando reconhecimento de voz")

    microfone = sr.Recognizer()

    print("Thread: Microfone")
    while True:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("Diga alguma coisa: ")
            audio = microfone.listen(source)
        try:
            # Passa o audio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_sphinx(audio, keyword_entries=keywords)
            # Após alguns segundos, retorna a frase falada
            if "google" in frase:
                voice("Recebido o comando para iniciar a Aplicação")
                print("Recebido o comando para iniciar a Aplicação")
                task_black_glass()
                execute_black = True
                cron = 0.0
            elif "stop" in frase:
                voice("Recebido o comando para parar a Aplicação")
                print("Recebido o comando para parar a Aplicação")
                execute_black = False
            elif "offline" in frase:
                voice("Recebido o comando para desligar a Aplicação")
                print("Recebido o comando para desligar a Aplicação")
                break
            else:
                print("O comando " + frase + " não é valido")
        except sr.UnknownValueError:
            print("Não entendi favor repetir")
        if not execute_black:
            print("Black glass parado")
        if execute_black and cron < 59.0:
            delta = datetime.now() - curren_minute_initial
            cron = float(delta.total_seconds())
            print("Black glass em modo espera a", delta.total_seconds())
            cron += 1.0
        elif execute_black and cron > 59.0:
            task_black_glass()
            cron = 0.0


def task_black_glass():
    global curren_minute_initial
    print("Executando black glass")
    print("ta executando topt top")
    pontosInteresses = distanciaDirecao()
    for x in pontosInteresses:
        voice(x)
        time.sleep(2)
        print("Encontrado " + str(x))
    print('Proxima verificação em 1 minuto')
    curren_minute_initial = datetime.now()

if __name__ == "__main__":
    t1 = threading.Thread(target=task_speech, name='t1')
    t1.start()
