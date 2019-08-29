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
# Classe responsavel pela conversão
# de texto para fala

import pyttsx

def textToSpeech():
    en = pyttsx.init()
    en.setProperty('voice', b'brazil')
    en.setProperty('rate', 200)

    return en