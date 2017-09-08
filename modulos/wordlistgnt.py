#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.
def gerarwl(adic, carac, qtd, nomesaida):
    arquivo = open(nomesaida, 'w')
    passw = [char for char in carac]
    for n in range(0, qtd-1):
        passw = [char+oth for char in carac for oth in passw]

    for sen in passw:
        if adic == '' or adic == ' ':
            arquivo.write(adic + sen + '\n')
        else:
            arquivo.write(adic+sen+'\n')
            arquivo.write(sen+adic+'\n')
    arquivo.close()