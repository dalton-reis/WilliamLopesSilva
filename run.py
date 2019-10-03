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

import _thread
import time
import speech_recognition as sr

num_thread = 0
max_loop = 5
thread_started = False
run = True


# Funcao responsavel por ouvir e reconhecer a fala
def ouvir_microfone(task_name):
    global run, thread_started
    microfone = sr.Recognizer()
    print("Thread : %s" % (task_name))
    while run:
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("%s Diga alguma coisa: " % (task_name))
            audio = microfone.listen(source)
        try:
            # Passa o audio para o reconhecedor de padroes do speech_recognition
            frase = microfone.recognize_google(audio, language='pt-BR')
            # Após alguns segundos, retorna a frase falada
            if (frase.__eq__("iniciar")):
                print("Recebido o comando para " + frase + " a Aplicação")
                thread_started = True
                start_application()
            elif (frase.__eq__("parar")):
                print("Recebido o comando para " + frase + " a Aplicação")
                thread_started = False
            elif (frase.__eq__("desligar")):
                print("Recebido o comando para " + frase + " a Aplicação")
                run = False
            else:
                print("O comando " + frase + " não é valido")
        except sr.UnknownValueError:
            print("Não entendi favor repetir")


def black_vision(task_name):
    global thread_started
    print("Thread : %s" % (task_name))
    while thread_started:
        print("Executando %s" % (task_name))
        time.sleep(2)
    if not thread_started:
        print("Finalizando %s" % (task_name))


def start_application():
    _thread.start_new_thread(black_vision, ("Black Vision",))


if __name__ == "__main__":
    _thread.start_new_thread(ouvir_microfone, ("Microfone",))

    while run:
        pass
