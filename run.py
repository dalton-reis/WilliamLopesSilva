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

from threading import Thread
from tts import voice
import speech_recognition as sr
import time
from actions import distanciaDirecao

runListening = True
thread_start = False


def listening():
    global runListening, thread_start
    voice("Iniciando reconhecimento de voz")

    microfone = sr.Recognizer()

    print("Thread: Microfone")
    while runListening:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("Diga alguma coisa: ")
            audio = microfone.listen(source)
        try:
            # Passa o audio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_google(audio, language='pt-BR')
            # Após alguns segundos, retorna a frase falada
            if "iniciar" in frase:
                voice("Recebido o comando para iniciar a Aplicação")
                print("Recebido o comando para iniciar a Aplicação")
                thread_start = True
                th1 = Thread(target=black_glass)
                th1.start()
            elif "parar" in frase:
                voice("Recebido o comando para parar a Aplicação")
                print("Recebido o comando para parar a Aplicação")
                thread_start = False
            elif "desligar" in frase:
                voice("Recebido o comando para desligar a Aplicação")
                print("Recebido o comando para desligar a Aplicação")
                runListening = False
            else:
                print("O comando " + frase + " não é valido")
        except sr.UnknownValueError:
            print("Não entendi favor repetir")


def black_glass():
    global thread_start
    print("Thread : black glass")
    while thread_start:
        print("Executando black glass")
        print("ta executando topt top")
        pontosInteresses = distanciaDirecao()
        for x in pontosInteresses:
            voice(x)
            print("Encontrado " + str(x))
        print('Working 1')
        time.sleep(3)

    if not thread_start:
        print("Finalizando black glass")

if __name__ == "__main__":
    th = Thread(target=listening)
    th.start()
