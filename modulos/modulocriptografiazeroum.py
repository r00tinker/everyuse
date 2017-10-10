#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.

#Importar as bibliotecas necessarias
import crypt, hashlib, base64

def senhaslinux(senhahash, arq):
    try:
        salt = senhahash.split('$')
        salt = '$'+salt[1]+'$'+salt[2]+'$'
        wordlist = open(arq, 'rb')
        i=0
        print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
        print('Hash:', senhahash)
        print('Salt:', salt)
        print('Wordlist:', arq)
        print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')

        for linha in wordlist.readlines():
            senha = linha.strip().decode()
            hashgerado = crypt.crypt(senha, salt)
            if hashgerado == senhahash:
                print('» Encontramos a senha:', senha)
                i=1
                break
            else:
                continue
        if i==0:
            print('  Não encontramos a senha :c Tente utilizar outra wordlist.')
    except IndexError:
        print('\033[31m+\033[0;1m--------------------------\033[31m+\033[0;0m')
        print('Hash:', senhahash, '[Não é uma hash do linux]')
        print('Salt: Invalido')
        print('Wordlist:', arq)
        print('\033[31m+\033[0;1m--------------------------\033[31m+\033[0;0m')

def hashs(senhahash,tipohash, arq):
    wordlist = open(arq, 'rb')
    i=0
    print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
    print('Hash:', senhahash)
    print('Tipo:', tipohash)
    print('Wordlist:', arq)
    print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')

    for linha in wordlist.readlines():
        senha = linha.strip().decode()
        if tipohash == 'md5':
            hashgerada = hashlib.md5(senha.encode('utf-8')).hexdigest()
        elif tipohash == 'sha1':
            hashgerada = hashlib.sha1(senha.encode('utf-8')).hexdigest()
        elif tipohash == 'sha224':
            hashgerada = hashlib.sha224(senha.encode('utf-8')).hexdigest()
        elif tipohash == 'sha256':
            hashgerada = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        elif tipohash == 'sha384':
            hashgerada = hashlib.sha384(senha.encode('utf-8')).hexdigest()
        elif tipohash == 'sha512':
            hashgerada = hashlib.sha512(senha.encode('utf-8')).hexdigest()

        if hashgerada == senhahash:
            print('» Encontramos a senha:', senha)
            i = 1
            break
        else:
            continue
    if i==0:
        print('  Não encontramos a senha :c Tente utilizar outra wordlist.')

def cryptobase64(senhahash, tipo):
    if tipo == 'decode':
        try:
            senha = base64.b64decode(senhahash.encode()).decode()
            print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
            print('Base64:', senhahash)
            print('Descriptografado:', senha)
            print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
        except Exception as err:
            print(err)
            if str(err) == 'Incorrect padding':
                print('\033[31m+\033[0;1m--------------------------\033[31m+\033[0;0m')
                print('Base64: Invalido')
                print('Descriptografado: Invalido')
                print('\033[31m+\033[0;1m--------------------------\033[31m+\033[0;0m')
                exit(0)
            elif str(err).startswith("'utf-8' codec"):
                senhalt = base64.b64decode(senhahash.encode())
                print('\033[31m+\033[0;1m--------------------------\033[31m+\033[0;0m')
                print('Base64:', senhahash)
                print('Descriptografado:', str(senhalt) + ' [Erro ao converter de Bytes para UTF-8]')
                print('\033[31m+\033[0;1m--------------------------\033[31m+\033[0;0m')
                exit(0)
    elif tipo == 'encode':
        try:
            senha = base64.b64encode(senhahash.encode()).decode()
            print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
            print('Descriptografado:', senhahash)
            print('Base64:', senha)
            print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
        except Exception as err:
            print('\033[31m+\033[0;1m--------------------------\033[31m+\033[0;0m')
            print('Descriptografado: Invalido')
            print('Base64: Invalido')
            print('Erro:', err)
            print('\033[31m+\033[0;1m--------------------------\033[31m+\033[0;0m')
