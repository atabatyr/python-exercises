# -*- coding: utf-8 -*-
"""
@author: A
"""
from translate import Translator

with open('translate.txt', mode = 'r') as my_file:
    text = my_file.read()

translator= Translator(to_lang="es")
translation = translator.translate(text)

print(translation)