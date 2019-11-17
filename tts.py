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
from gtts import gTTS
import re


def save_audio_tts(id, ponto_interesse):
    tts = gTTS(text=ponto_interesse, lang='pt-br')
    # Replace all runs of whitespace with a single dash
    ponto_interesse = re.sub(r"\s+", '_', ponto_interesse)
    # Save the audio file
    tts.save('/Users/william.silva/Desktop/Furb/TCC/gttsAudios/' + str(id) + '_' + ponto_interesse + '.mp3')
