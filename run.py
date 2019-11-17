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

task_black = multiprocessing.Value(ctypes.c_bool, False)  # (type, init value)
task_main = multiprocessing.Value(ctypes.c_bool, True)  # (type, init value)
lock = multiprocessing.Manager().Lock()
keywords = [("start", 1), ("stop", 1), ("offline", 1), ]

def task_speech():
    global task_main, task_black, keywords
    print("Iniciando reconhecimento de voz")
    print("Thread: Microfone")
    microfone = sr.Recognizer()

    while task_main:
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
                with lock:
                    task_black.value = True
                print("Recebido o comando para iniciar a Aplicação: ", frase)
            elif "stop" in frase:
                with lock:
                    task_black.value = False
                print("Recebido o comando para parar a Aplicação: ", frase)
            elif "offline" in frase:
                with lock:
                    task_black.value = True
                    task_main.value = True
                print("Recebido o comando para desligar a Aplicação: ", frase)
            else:
                print("O comando " + frase + " não é valido")
        except sr.UnknownValueError:
            print("Não entendi favor repetir")


def task_black_glasses():
    global task_main, task_black
    print("Executando black glasses")
    while task_main.value:
        if task_black.value:
            pontosInteresses = distanciaDirecao()
            for x in pontosInteresses:
                time.sleep(2)
                print("Encontrado " + str(x))
            print('Proxima verificação em 30 segundos')
            time.sleep(30)
        else:
            print("Black glasses aguardando comando para iniciar!")
            time.sleep(5)


if __name__ == "__main__":
    t1 = multiprocessing.Process(target=task_speech)
    t2 = multiprocessing.Process(target=task_black_glasses)
    t1.start()
    t2.start()
