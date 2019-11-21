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
import vlc
import time
from mutagen.mp3 import MP3

def save_audio_tts(id, ponto_interesse):
    tts = gTTS(text=ponto_interesse, lang='pt-br')
    # Replace all runs of whitespace with a single dash
    ponto_interesse = re.sub(r"\s+", '_', ponto_interesse)
    # Save the audio file
    tts.save('/Users/william.silva/Desktop/Furb/TCC/gttsAudios/' + str(id) + '_' + ponto_interesse + '.mp3')


def play_audio_tts(file):
    if type(file) is str:
        print(file)
        instance = vlc.Instance('--aout=alsa')
        p = instance.media_player_new()
        m = instance.media_new('/home/pi/Desktop/TCC/TCC-Furb/audios/' + file + '.mp3')
        p.set_media(m)
        p.play()
        vlc.libvlc_audio_set_volume(p, 80)
        time.sleep(song_length(file))
    else:
        for i in file:
            for j in i:
                instance = vlc.Instance('--aout=alsa')
                p = instance.media_player_new()
                m = instance.media_new('/home/pi/Desktop/TCC/TCC-Furb/audios/' + j + '.mp3')
                p.set_media(m)
                p.play()
                vlc.libvlc_audio_set_volume(p, 80)
                time.sleep(song_length(j))


def song_length(name):
    audio = MP3('/home/pi/Desktop/TCC/TCC-Furb/audios/' + name + '.mp3')
    return float(audio.info.length + 0.7)