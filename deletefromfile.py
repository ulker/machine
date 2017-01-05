# -*- coding: utf-8 -*-


with open('/home/furkan/Masaüstü/kelime.txt', 'r') as f:
    mywords = [line.strip() for line in f]

print type(mywords)

