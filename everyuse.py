#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.

#IMPORTAR O QUE É NECESSARIO
print('[\33[36m*\033[0;0m] Importando bibliotecas padrões.')
try:
    import os
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage
    from email.mime.text import MIMEText
    import getpass
    import socket
    from socket import gaierror
    from datetime import datetime
    import requests
    import time
except ImportError:
    print('Erro ao importar as bibliotecas padroes do python.')
    exit(0)

#Banner principal do programa
def banner():
    os.system('clear')
    print("""
\033[0;0m\033[1m8888888888 888     888 8888888888 8888888b. Y88b   d88P \033[33m\033[1m888     888  .d8888b.  8888888888 
\033[0;0m\033[1m888        888     888 888        888   Y88b Y88b d88P  \033[33m\033[1m888     888 d88P  Y88b 888        
\033[0;0m\033[1m888        888     888 888        888    888  Y88o88P   \033[33m\033[1m888     888 Y88b.      888        
\033[0;0m\033[1m8888888    Y88b   d88P 8888888    888   d88P   Y888P    \033[33m\033[1m888     888  "Y888b.   8888888    
\033[0;0m\033[1m888         Y88b d88P  888        8888888P"     888     \033[33m\033[1m888     888     "Y88b. 888        
\033[0;0m\033[1m888          Y88o88P   888        888 T88b      888     \033[33m\033[1m888     888       "888 888        
\033[0;0m\033[1m888           Y888P    888        888  T88b     888     \033[33m\033[1mY88b. .d88P Y88b  d88P 888        
\033[0;0m\033[1m8888888888     Y8P     8888888888 888   T88b    888     \033[33m\033[1m "Y88888P"   "Y8888P"  8888888888
\033[0;0m\033[1m\033[31m                                        ᶠᶸᶜᵏ ˢᵒᶜᶤᵉᵗʸ\033[0;0m
    """)

#Verificar se é root
print('[\33[36m*\033[0;0m] Verificando se usuario é root.')
time.sleep(0.5)
if os.getuid() != 0:
    print(' Tivemos um erro :c')
    print(' Execute o programa como administrador')
    print(' .: sudo ./everyuse')
    exit()

#Importar os modulos.
print('[\33[36m*\033[0;0m] Importando módulos do programa.')
time.sleep(0.5)
try:
    import modulos
    from modulos import moduloengsocialzeroum
    from modulos import moduloscannerzeroum
    from modulos import modulobruteforcezeroum
    from modulos import modulocriptografiazeroum
except ImportError:
    banner()
    print('Não conseguimos encontrar os módulos necessários para utilizar o programa.')
    exit(0)

#Variaveis utilizadas
verif = requests.get('https://raw.githubusercontent.com/r00tinker/everyuse/master/version')
sair = False
sairmenu = False

#Variaveis globais
global cmevem
global cmwl
global cmptsc
global cmegsc
global cmscs
global cmbfs
global cm

#Definindo Cm
cmevem = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» '
cmptsc = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mportscan\033[0;0m» '
cmwhois = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mwhois\033[0;0m» '
cmhref = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mhrefscan\033[0;0m» '
cmwl = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33mwordlist\033[0;0m» '
cmwlbc = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33mwordlist\033[0;0m/\033[1m\033[33mbasica\033[0;0m» '
cmegsc = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m» '
cmscs = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m» '
cmcry = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mcriptografia\033[0;0m» '
cryli = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mcriptografia\033[0;0m/\033[1m\033[33mhashlinux\033[0;0m» '
cryba = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mcriptografia\033[0;0m/\033[1m\033[33mbase64\033[0;0m» '
cryha = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mcriptografia\033[0;0m/\033[1m\033[33mhash'
cmbfs = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m» '
btftp = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33mftp\033[0;0m» '
btgma = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33mgmail\033[0;0m» '
btsubd = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33msubdominio\033[0;0m» '
btdir = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33mdiretorio\033[0;0m» '
cm = '\033[1m\033[33meveryuse\033[0;0m» '

#Mensagem ao sair do programa
def sairprograma():
    print('\n\n Obrigado por utilizar o \033[1mevery\033[33muse\033[0;0m para suas tarefas.')
    print('\n    A liberdade foi confundida com a democracia. \n')
    global sair
    sair = True
    exit(0)

#Mensagem ao completar uma tarefa
def complett():
    print('\n\n     \033[0;0mAperte \033[1m\033[33m[ENTER]\033[0;0m para voltar.')
    input('')

#Se a pasta .tmpup/ existir, significa que a pessoa fez uma atualização.
if os.path.exists('.tmpup/'):
    banner()
    print('[\33[36m*\033[0;0m] O everyuse foi atualizado com sucesso !')
    os.system('rm -rf .tmpup/')
    os.system('rm -rf updeve.sh')
    complett()

#Verificando se possui uma atualização disponivel
print('[\33[36m*\033[0;0m] Verificando possiveis atualizações.')
time.sleep(0.5)
if 'v1.0-10/10' not in verif.text:
    ndatl = '(Versão nova disponivel.)'
else:
    ndatl = ''

#Função para atualizar o programa.
def atualizacao():
    banner()
    if 'v1.0-10/10' not in verif.text:
        print(verif.text)
        print(' Você precisa atualizar o everyuse!')
        sairmenu = False
        while sairmenu == False:
            sorn = input(cm + 'Deseja atualizar o programa? (s/n) ')
            if sorn.lower() == 's':
                print(' Atualizando o everyuse.')
                os.system('wget -q https://raw.githubusercontent.com/r00tinker/everyuse/master/everyuse.py')
                upmodulos = requests.get('https://raw.githubusercontent.com/r00tinker/everyuse/master/modulos/allrawupdate')
                os.system('rm -rf modulos/*')
                os.system('mkdir .tmpup/')
                for linha in upmodulos.text.split():
                    os.system('cd modulos/ && wget -q ' + linha)
                os.system('echo "#!/bin/bash" > updeve.sh')
                os.system('echo "sudo rm -rf everyuse" >> updeve.sh')
                os.system('echo "sudo mv everyuse.py everyuse" >> updeve.sh')
                os.system('echo "sudo chmod +x everyuse" >> updeve.sh')
                os.system('echo "exit" >> updeve.sh')
                os.system('sudo chmod +x updeve.sh')
                print(' Abra novamente o everyuse para concluir a atualização.')
                complett()
                os.system('./updeve.sh')
                exit(0)
            elif sorn.lower() == 'n':
                sairmenu = True
            else:
                continue
    else:
        print(verif.text)
        print(' Você não precisa atualizar o everyuse!')
        complett()
        sairmenu = True

#########################################################################################################################
#                                               BRUTE FORCE FTP                                                         #
#########################################################################################################################
def bruteftp():
    sairmenu = False
    while sairmenu == False:
        try: # Tente
            host = input(btftp + 'Alvo: ') #Pegue o alvo
            try:
                ip = socket.gethostbyname(host) #Verifique se existe
            except:
                print('Site inválido.') #Se não existir, pergunte novamente o alvo
                continue
            user = input(btftp + 'Usuario: ') #Usuario do FTP
            print("""  \033[1mSelecione uma opção:

                \033[1m1)\033[0;0m Gerar uma wordlist
                \033[1m2)\033[0;0m Usar uma wordlist

                \033[1m0)\033[0;0m Voltar
                        """)
            opt = str(input(btftp)) #Qual é a opção?
            if opt == '0': #Sai do programa
                sairmenu = True

            # Gerar uma wordlist e selecionar ela
            elif opt == '1':
                gerarwordlist()
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(btftp + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()

            # Selecionar uma wordlist
            elif opt == '2':
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(btftp + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()
            print('')
            try:
                modulobruteforcezeroum.ftp(wl, user, ip) #Execute o programa
            except KeyboardInterrupt:
                continue
            except UnboundLocalError:
                continue
            except EOFError:
                sairprograma()
            complett()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()
#########################################################################################################################
#                                               BRUTE FORCE FTP                                                         #
#########################################################################################################################
'''-------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                                   HREF SCAN                                                           #
#########################################################################################################################
def hrefscan():
    sairmenu = False
    while sairmenu == False:
        try:
            print(' Ex.: www.site.com.br')
            alvo = input(cmhref + 'Alvo: ')
            try:
                ip = socket.gethostbyname(alvo)
            except:
                continue
            try:
                moduloscannerzeroum.href(alvo, ip)  # Execute o programa
            except KeyboardInterrupt:
                continue
            except UnboundLocalError:
                continue
            except EOFError:
                sairprograma()
            complett()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()
#########################################################################################################################
#                                                   HREF SCAN                                                           #
#########################################################################################################################
'''-------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                                  HASH LINUX                                                           #
#########################################################################################################################
def hashlinux():
    sairmenu = False
    while sairmenu == False:
        try:
            hashalvo = input(cryli + 'Hash: ')
            print("""  \033[1mSelecione uma opção:

                    \033[1m1)\033[0;0m Gerar uma wordlist
                    \033[1m2)\033[0;0m Usar uma wordlist

                    \033[1m0)\033[0;0m Voltar
                            """)
            opt = str(input(cryli))  # Qual é a opção?
            if opt == '0':  # Sai do programa
                sairmenu = True

            # Gerar uma wordlist e selecionar ela
            elif opt == '1':
                gerarwordlist()
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(cryli + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()

            # Selecionar uma wordlist
            elif opt == '2':
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(cryli + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()
            try:
                modulos.modulocriptografiazeroum.senhaslinux(hashalvo, wl)  # Execute o programa
            except KeyboardInterrupt:
                continue
            except UnboundLocalError:
                continue
            except EOFError:
                sairprograma()
            complett()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()
#########################################################################################################################
#                                                  HASH LINUX                                                           #
#########################################################################################################################
'''-------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                                  HASHS ALL                                                            #
#########################################################################################################################
def whoistheserver():
    sairmenu = False
    while sairmenu == False:
        try:
            print(' Ex.: www.site.com.br')
            alvo = input(cmwhois + 'Alvo: ')
            try:
                ip = socket.gethostbyname(alvo)
            except:
                continue
            try:
                moduloscannerzeroum.whois(alvo)  # Execute o programa
            except KeyboardInterrupt:
                continue
            except UnboundLocalError:
                continue
            except EOFError:
                sairprograma()
            complett()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()
#########################################################################################################################
#                                                  HASHS ALL                                                            #
#########################################################################################################################
#########################################################################################################################
#                                                  HASHS ALL                                                            #
#########################################################################################################################
def hashsall(tipodehash):
    sairmenu = False
    while sairmenu == False:
        try:
            hashalvo = input(cryha+tipodehash+'\033[0;0m» ' + 'Hash '+tipodehash.upper()+': ')
            if tipodehash == 'sha512' and len(hashalvo) != 128:
                print(' Insira uma hash valida.')
                continue
            elif tipodehash == 'sha384' and len(hashalvo) != 96:
                print(' Insira uma hash valida.')
                continue
            elif tipodehash == 'sha256' and len(hashalvo) != 64:
                print(' Insira uma hash valida.')
                continue
            elif tipodehash == 'sha224' and len(hashalvo) != 56:
                print(' Insira uma hash valida.')
                continue
            elif tipodehash == 'sha1' and len(hashalvo) != 40:
                print(' Insira uma hash valida.')
                continue
            elif tipodehash == 'md5' and len(hashalvo) != 32:
                print(' Insira uma hash valida.')
                continue

            print("""  \033[1mSelecione uma opção:

                    \033[1m1)\033[0;0m Gerar uma wordlist
                    \033[1m2)\033[0;0m Usar uma wordlist

                    \033[1m0)\033[0;0m Voltar
                            """)
            opt = str(input(cryha+tipodehash+'\033[0;0m» '))  # Qual é a opção?
            if opt == '0':  # Sai do programa
                sairmenu = True

            # Gerar uma wordlist e selecionar ela
            elif opt == '1':
                gerarwordlist()
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(cryha+tipodehash+'\033[0;0m» ' + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()

            # Selecionar uma wordlist
            elif opt == '2':
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(cryha+tipodehash+'\033[0;0m» ' + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()
            try:
                modulos.modulocriptografiazeroum.hashs(hashalvo, tipodehash, wl)  # Execute o programa
            except KeyboardInterrupt:
                continue
            except UnboundLocalError:
                continue
            except EOFError:
                sairprograma()
            complett()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()
#########################################################################################################################
#                                                  HASHS ALL                                                            #
#########################################################################################################################
'''-------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                             BRUTE FORCE SUBDOM                                                        #
#########################################################################################################################
def brutesubdom():
    sairmenu = False
    while sairmenu == False:
        try:
            print(btsubd + 'Ex.: site.com.br')
            alvo = input(btsubd + 'Alvo: ')
            try:
               ip = socket.gethostbyname('www.'+alvo)
            except:
                continue
            print("""  \033[1mSelecione uma opção:

                \033[1m1)\033[0;0m Gerar uma wordlist
                \033[1m2)\033[0;0m Usar uma wordlist

                \033[1m0)\033[0;0m Voltar
                        """)
            opt = str(input(btsubd)) #Qual é a opção?
            if opt == '0': #Sai do programa
                sairmenu = True

            # Gerar uma wordlist e selecionar ela
            elif opt == '1':
                gerarwordlist()
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(btsubd + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()

            # Selecionar uma wordlist
            elif opt == '2':
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(btsubd + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()
            try:
                modulobruteforcezeroum.subdominio(ip, alvo, wl)
            except KeyboardInterrupt:
                continue
            except UnboundLocalError:
                continue
            except EOFError:
                sairprograma()
            complett()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()

#########################################################################################################################
#                                             BRUTE FORCE SUBDOM                                                        #
#########################################################################################################################
'''-------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                             BRUTE FORCE DIR                                                           #
#########################################################################################################################
def brutedir():
    sairmenu = False
    while sairmenu == False:
        try:
            print(btdir + 'Ex.: http://www.site.com.br/')
            alvo = input(btdir + 'Alvo: ')
            try:
                if alvo.endswith('/'):
                    req = requests.get(alvo)
                else:
                    continue
            except:
                continue
            print("""  \033[1mSelecione uma opção:

                \033[1m1)\033[0;0m Gerar uma wordlist
                \033[1m2)\033[0;0m Usar uma wordlist

                \033[1m0)\033[0;0m Voltar
                        """)
            opt = str(input(btdir)) #Qual é a opção?
            if opt == '0': #Sai do programa
                sairmenu = True

            # Gerar uma wordlist e selecionar ela
            elif opt == '1':
                gerarwordlist()
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(btdir + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()

            # Selecionar uma wordlist
            elif opt == '2':
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(btdir + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()
            try:
                modulobruteforcezeroum.diretorio(alvo, wl)
            except KeyboardInterrupt:
                continue
            except UnboundLocalError:
                continue
            except EOFError:
                sairprograma()
            complett()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()

#########################################################################################################################
#                                             BRUTE FORCE DIR                                                           #
#########################################################################################################################
'''-------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                               BRUTE FORCE GMAIL                                                       #
#########################################################################################################################
def brutegmail():
    sairmenu = False
    while sairmenu == False:
        try:
            alvo = input(btgma + 'Email do alvo: ') #Pegue o email do alvo
            print("""  \033[1mSelecione uma opção:

                \033[1m1)\033[0;0m Gerar uma wordlist
                \033[1m2)\033[0;0m Usar uma wordlist

                \033[1m0)\033[0;0m Voltar
                        """)
            opt = str(input(btgma)) #Qual é a opção?
            if opt == 0: #Sai do programa
                sairmenu = True

            # Gerar uma wordlist e selecionar ela
            elif opt == '1':
                gerarwordlist()
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(btgma + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()

            # Selecionar uma wordlist
            elif opt == '2':
                print('Ex.: /home/user/Documentos/wordlist.txt')
                f = False
                try:
                    while f == False:
                        try:
                            wl = input(btgma + 'Wordlist: ')
                            arq = open(wl)
                            f = True
                        except FileNotFoundError:
                            continue
                        except FileExistsError:
                            continue
                        except KeyboardInterrupt:
                            sairmenu = True
                            f = True
                            complett()
                        except EOFError:
                            sairprograma()
                except KeyboardInterrupt:
                    sairmenu = True
                    complett()
                except EOFError:
                    sairprograma()
            try:
                modulobruteforcezeroum.gmail(alvo, wl)
            except KeyboardInterrupt:
                continue
            except UnboundLocalError:
                continue
            except EOFError:
                sairprograma()
            complett()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()
#########################################################################################################################
#                                               BRUTE FORCE GMAIL                                                       #
#########################################################################################################################
'''-------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                         INICIO - GERAR WORDLIST BASIC                                                 #
#########################################################################################################################
def gerarumawlbasic():
    try:
        banner()
        adicional = input(cmwlbc + 'Adicione uma palavra: ')
        caracincl = input(cmwlbc + 'Caracteres: ')
        taman = int(input(cmwlbc + 'Quantidade de caracteres: '))
        nomearq = input(cmwlbc + 'Nome da wordlist: ')
        tmp = datetime.utcnow()
        modulobruteforcezeroum.gerarwl(adicional, caracincl, taman, nomearq)
        tmpd = datetime.utcnow()
        print(' Wordlist gerada com sucesso!')
        print(' Tempo para gerar wordlist: ', tmpd - tmp)
        sorn = input(cmwl + ' Deseja mover a wordlist? (S/n): ')
        if sorn.lower() == 's':
            mvd=False;
            while mvd == False:
                mov = input('Caminho para mover a wordlist: ')
                if os.path.exists(mov):
                    os.system('mv ' + nomearq + ' ' + mov)
                    print(' Wordlist movida com sucesso.')
                    mvd = True
                else:
                    print(' Diretório', mov, 'não existe.')
        complett()
    except KeyboardInterrupt:
        gerarwordlist()
    except EOFError:
        sairprograma()
#########################################################################################################################
#                                          FIM - GERAR WORDLIST BASIC                                                   #
#########################################################################################################################
#########################################################################################################################
#                                         INICIO - MENU - PORT SCAN                                                     #
#########################################################################################################################
def portpref():
    sairmenu = False
    try:
        while sairmenu == False:
            banner()
            print("""  \033[1mSelecione um tipo:
    
        \033[1m1)\033[0;0m Portas padrões
        \033[1m2)\033[0;0m Portas especificas
        \033[1m3)\033[0;0m Alcance de portas
    
        \033[1m0)\033[0;0m Voltar
                """)
            opt = str(input(cmptsc))
            if opt == '0':
                sairmenu = True
            elif opt == '1' or opt == '2' or opt == '3':
                velo = 0
                velocm = False
                print(' Ex.: www.siteteste.com')
                site = str(input(cmptsc + 'Site: '))
                while velocm == False:
                    print("""  \033[1mSelecione uma velocidade:
        
        \033[1m1)\033[0;0m Rapido (Menos preciso)
        \033[1m2)\033[0;0m Medio (Preciso)
        \033[1m3)\033[0;0m Lento (Mais preciso)
                        """)
                    velo = str(input(cmptsc + 'Velocidade: '))
                    if velo == '1':
                        velocidade = 0.05
                        velocm = True
                    elif velo == '2':
                        velocidade = 0.5
                        velocm = True
                    elif velo == '3':
                        velocidade = 5
                        velocm = True
                if opt == '3':
                    cmc = int(input(cmptsc+'Porta inicio: '))
                    fip = int(input(cmptsc+'Porta final: '))
                    fi = fip + 1
                    moduloscannerzeroum.portaespecificada(site, velocidade, range(cmc, fi))
                    complett()
                if opt == '2':
                    print(' Separe as portas por virgulas e sem espaço.')
                    ports = str(input(cmptsc+'Portas: '))
                    portas = ports.split(',')
                    moduloscannerzeroum.portaespecificada(site, velocidade, portas)
                    complett()
                if opt == '1':
                    moduloscannerzeroum.porta(site, 1, velocidade)
                    complett()
    except gaierror:
        print('\n O site informado esta incorreto')
        complett()
    except KeyboardInterrupt:
        complett()
        sairmenu = True
    except ValueError:
        portpref()
    except EOFError:
        sairprograma()

#########################################################################################################################
#                                            FIM - MENU - PORT SCAN                                                     #
#########################################################################################################################
'''------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                            INICIO - ENVIAR EMAIL                                                      #
#########################################################################################################################
def enviaremail(servidor, porta):
    try:
        de = str(input(cmevem + 'Seu email: '))
        passw = getpass.getpass(cmevem + 'Sua senha: ')
        nomeex = str(input(cmevem + 'Nome exibido: '))
        print('Obs.: Utilize "," para separar os emails.')
        para = str(input(cmevem + 'Enviar para: '))
        para = para.split(',')
        assunto = str(input(cmevem + 'Assunto: '))
        soun = str(input(cmevem + 'Deseja anexar um arquivo ? [s/n]: '))
        if soun.lower() == 's':
            sairmenu = False
            while sairmenu == False:
                print("""  \033[1mSelecione um tipo de anexo:
    
            \033[1m1)\033[0;0m Imagem
            \033[1m2)\033[0;0m Audio (.MP3/.OGG)
            \033[1m3)\033[0;0m Documento (.PDF/.DOCX)
    
            \033[1m0)\033[0;0m Voltar
                """)
                opx = str(input(cmevem))
                if opx == '0':
                    sairmenu = True
                    tipoanx = 0
                    nomearq = ''
                    anexar = 'sem'
                    break
                elif opx == '1':
                    print('Exemplo.: /home/user/Documentos/arquivo.png')
                    tipoanx = 1
                    anexar = str(input(cmevem + 'Arquivo: '))
                    nomearq = str(input(cmevem + 'Nome do arquivo: '))
                    if os.path.exists(anexar):
                        sairmenu = True
                    else:
                        print('Arquivo não encontrado.')
                elif opx == '2':
                    print('Exemplo.: /home/user/Documentos/arquivo.mp3')
                    tipoanx = 2
                    anexar = str(input(cmevem + 'Arquivo: '))
                    nomearq = str(input(cmevem + 'Nome do arquivo: '))
                    if os.path.exists(anexar) and anexar.endswith('.mp3') or anexar.endswith('.ogg'):
                        sairmenu = True
                    else:
                        print(' Arquivo não encontrado.')
                        print(' Apenas arquivos .mp3 ou .ogg')
                elif opx == '3':
                    print('Exemplo.: /home/user/Documentos/arquivo.pdf')
                    tipoanx = 3
                    anexar = str(input(cmevem + 'Arquivo: '))
                    nomearq = str(input(cmevem + 'Nome do arquivo: '))
                    if os.path.exists(anexar) and anexar.endswith('.pdf') or anexar.endswith('.docx'):
                        sairmenu = True
                    else:
                        print(' Arquivo não encontrado.')
                        print(' Apenas arquivos .pdf ou .docx')
        else:
            anexar = ''
            nomearq = ''
            tipoanx = 0
        print('Obs.: Utilize "</fim>" para terminar o texto.')
        corpocom = str(input(cmevem + 'Texto: '))
        corpolinha = str('')
        i = 1
        while corpolinha.lower() != '</fim>':
            if corpocom.lower() == '</fim>':
                corpocom = ''
                break
            i += 1
            corpolinha = str(input(cmevem + str(i) + 'º Linha: '))
            if corpolinha.lower() != '</fim>':
                corpocom += '\n' + corpolinha
            else:
                break

        qtd = int(input(cmevem + 'Quantidade de envios: '))
        print(' Enviando', str(qtd), 'email para:')
        for email in para:
            print('\033[1m☞\033[0;0m' + email)
        try:
            moduloengsocialzeroum.enviaremail(de, passw, nomeex, para, assunto, corpocom, servidor, porta, anexar, tipoanx, nomearq, qtd)
            print('\nTodos os emails foram enviados corretamente !')
            complett()
        except smtplib.SMTPAuthenticationError:
            print('\n Não foi possivel enviar os emails pois você inseriu o seu email e/ou senha errado.')
            print(' Talvez você não tenha permitido o uso de aplicativos menos seguros.')
            print(' Link para ativar: https://myaccount.google.com/lesssecureapps')
            complett()

        except smtplib.SMTPRecipientsRefused:
            print('\nNão foi possivel enviar os emails pois você inseriu um destinatario inexistente.')
            complett()
    except KeyboardInterrupt:
        complett()
    except EOFError:
        sairprograma()
#########################################################################################################################
#                                               FIM - ENVIAR EMAIL                                                      #
#########################################################################################################################


#Menu para saber o servidor de email usado pela pessoa.
def seuservidor():
    sairmenu = False
    try:
        while sairmenu == False:
            banner()
            print("""  \033[1mSelecione seu servidor:
    
        \033[1m1)\033[0;0m Gmail
        \033[1m2)\033[0;0m Outlook
    
        \033[1m0)\033[0;0m Voltar
            """)
            opt = str(input(cmevem))
            if opt == '0':
                sairmenu = True
            elif opt == '1':
                enviaremail('smtp.gmail.com', 587)
            elif opt == '2':
                enviaremail('smtp.live.com', 587)
    except KeyboardInterrupt:
        sairmenu = True
    except ValueError:
        seuservidor()
    except EOFError:
        sairprograma()

#MENU DE ENGENHARIA SOCIAL
def engenhariasocial():
    try:
        sairmenu = False
        while sairmenu == False:
            banner()
            print("""  \033[1mSelecione uma opção:
    
        \033[1m1)\033[0;0m Envio de emails
    
        \033[1m0)\033[0;0m Voltar
            """)
            opt = str(input(cmegsc))
            if opt == '0':
                sairmenu = True
            elif opt == '1':
                seuservidor()
    except KeyboardInterrupt:
        sairmenu = True
        complett()
    except ValueError:
        engenhariasocial()
    except EOFError:
        sairprograma()

#MENU DE SCANNERS
def scanners():
    print()
    sairmenu = False
    try:
        while sairmenu == False:
            banner()
            print("""  \033[1mSelecione um scanner:
    
            \033[1m1)\033[0;0m Porta
            \033[1m2)\033[0;0m Whois
            \033[1m3)\033[0;0m Hrefs
    
            \033[1m0)\033[0;0m Voltar
                """)
            opt = str(input(cmscs))
            if opt == '0':
                sairmenu = True
            elif opt == '1':
                portpref()
            elif opt == '2':
                whoistheserver()
            elif opt == '3':
                hrefscan()
    except KeyboardInterrupt:
        sairmenu = True
    except ValueError:
        scanners()
    except EOFError:
        sairprograma()

def base64ed():
    sairmenu = False
    while sairmenu == False:
        try:
            banner()
            print("""  \033[1mSelecione uma opção:
    
            \033[1m1)\033[0;0m Encode
            \033[1m2)\033[0;0m Decode
    
            \033[1m0)\033[0;0m Voltar
                """)
            opt = str(input(cryba))
            if opt == '0':
                sairmenu = True
                break
            elif opt == '1':
                cryptog = input(cryba + 'Palavra para criptografar: ')
                modulos.modulocriptografiazeroum.cryptobase64(cryptog, 'encode')
                complett()
            elif opt == '2':
                cryptog = input(cryba + 'Palavra para descriptografar: ')
                modulos.modulocriptografiazeroum.cryptobase64(cryptog, 'decode')
                complett()
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()

#Menu de criptografia
def criptografia():
    sairmenu = False
    while sairmenu == False:
        try:
            banner()
            print("""  \033[1mSelecione uma opção:

            \033[1m1)\033[0;0m Hash linux
            \033[1m2)\033[0;0m MD5
            \033[1m3)\033[0;0m SHA1
            \033[1m4)\033[0;0m SHA224
            \033[1m5)\033[0;0m SHA256
            \033[1m6)\033[0;0m SHA384
            \033[1m7)\033[0;0m SHA512
            \033[1m8)\033[0;0m Base64
            
            \033[1m0)\033[0;0m Voltar
                """)
            opt = str(input(cmcry))
            if opt == '0':
                sairmenu = True
                break
            elif opt == '1':
                hashlinux()
            elif opt == '2':
                hashsall('md5')
            elif opt == '3':
                hashsall('sha1')
            elif opt == '4':
                hashsall('sha224')
            elif opt == '5':
                hashsall('sha256')
            elif opt == '6':
                hashsall('sha384')
            elif opt == '7':
                hashsall('sha512')
            elif opt == '8':
                base64ed()
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()

#Menu de brute force
def bruteforce():
    sairmenu = False
    while sairmenu == False:
        try:
            banner()
            print("""  \033[1mSelecione uma opção:
    
            \033[1m1)\033[0;0m FTP
            \033[1m2)\033[0;0m Gmail
            \033[1m3)\033[0;0m Subdominio
            \033[1m4)\033[0;0m Diretorio
            \033[1m9)\033[0;0m Gerador de wordlist
    
            \033[1m0)\033[0;0m Voltar
                """)
            opt = str(input(cmbfs))
            if opt == '0':
                sairmenu = True
                break
            elif opt == '9':
                gerarwordlist()
            elif opt == '1':
                bruteftp()
            elif opt == '2':
                brutegmail()
            elif opt == '3':
                brutesubdom()
            elif opt == '4':
                brutedir()
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()

#Menu para gerar wordlists
def gerarwordlist():
    sairmenu = False
    while sairmenu == False:
        try:
            banner()
            print("""  \033[1mSelecione uma opção:
    
        \033[1m1)\033[0;0m Basica
    
        \033[1m0)\033[0;0m Voltar
                """)
            opt = str(input(cmwl))
            if opt == '0':
                sairmenu = True
            elif opt == '1':
                gerarumawlbasic()
        except KeyboardInterrupt:
            sairmenu = True
            complett()
        except EOFError:
            sairprograma()

#Ajuda para usuarios
def ajuda():
    sairmenu = False
    while sairmenu == False:
        try:
            banner()
            print(""" \033[1mMenu de ajuda para usuarios.:\n
            \033[1m\033[31mEngenharia social.\033[0;0m
            \033[1m║    \033[0;0mO módulo de engenharia social foi criado para ataques contra as pessoas,
            \033[1m║    \033[0;0maonde você se passa por outro alguém e tem a intenção de enganar ou
            \033[1m║    \033[0;0mpersuadir o alvo. Pensando nisso, nós trabalhamos para ajudar na
            \033[1m║    \033[0;0meficiência e no auxilio para um ataque de engenharia social, tais
            \033[1m║    \033[0;0mcomo: Phishing.
            \033[1m╠══  \033[1m\033[31mEnvio de email.\033[0;0m 
            \033[1m║        \033[0;0mA forma de utilizar o envio de email é simples, visando em apenas
            \033[1m║        \033[0;0mfornecer as informações que o programa está pedindo. Porém existe
            \033[1m║        \033[0;0malguns passos onde a pessoa pode se perder, como por exemplo, o
            \033[1m║        \033[0;0menvio de email para mais de um destinatario.
            \033[1m║        \033[31m   Uso: emaildeteste@servidor.com,emaildeteste2@servidor.com\033[0;0m
            \033[1m║        \033[0;0mUm dos problemas é não conseguir enviar email por bloqueio do    
            \033[1m║        \033[0;0mgmail, que não permite, por padrão, utilizar em aplicativos menos
            \033[1m║        \033[0;0mseguros. Arrumar este problema é facil, e basta você acessar o 
            \033[1m║        \033[0;0mlink (\033[36mhttps://myaccount.google.com/lesssecureapps\033[0;0m) e ativar a 
            \033[1m║        \033[0;0mopção.
            \033[1m║        \033[0;0mPara anexo de arquivos(Imagens/Audios/Documentos) você deverá
            \033[1m║        \033[0;0minformar o caminho para o arquivo mais a extensão do arquivo.
            \033[1m║        \033[31m   Uso: /home/user/Imagens/arquivo.jpg\033[0;0m
            \033[1m║        \033[0;0mLembrando que os arquivos de audios só permitem extensão de .mp3   
            \033[1m║        \033[0;0me .ogg, os documentos só permitem .pdf e .docx.
            \033[1m║        \033[0;0mPara adicionar linhas na sua mensagem, basta você apertar ENTER.
            \033[1m║        \033[0;0mPara determinar o fim da mensagem, adicione uma linha e escreva:
            \033[1m║        \033[31m   Uso: </fim>\033[0;0m
            \033[1m╚════════════════════════════════════════════════════════════════════════\033[0;0m
            \n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            banner()
            print(""" \033[1mMenu de ajuda para usuarios.:\n
            \033[1m\033[31mScanners.\033[0;0m
            \033[1m║    \033[0;0mO módulo de scanners foi criado para levantar informações sobre seu
            \033[1m║    \033[0;0malvo, conhecido no pentest como Information Gathering, etapa que
            \033[1m║    \033[0;0mtem como foco o levantamento de dados, além de ser a etapa mais
            \033[1m║    \033[0;0mimportante.
            \033[1m╠══  \033[1m\033[31mScanner de porta.\033[0;0m 
            \033[1m║    \033[0;0mComo qualquer outro módulo do programa, procuramos facilitar o uso
            \033[1m║    \033[0;0mpara que pessoas sem muito conhecimento, consiga fazer o scanner.
            \033[1m║    \033[0;0mNele você poderá escolher uma das três opções disponiveis, que são:
            \033[1m║    \033[31m  1)Portas padrões.\033[0;0m
            \033[1m║    \033[0;0mEsta opção faz o scanner apenas em portas mais comuns, como
            \033[1m║    \033[0;0mFTP(21)|Telnet(23)|MySql(3306)|SMTP(25)| entre muitas outras.
            \033[1m║    \033[0;0mNo total são exatamente 29 portas mais usadas.
            \033[1m║    \033[0;0mPara usar basta informar o site, sem http.
            \033[1m║    \033[31m   Uso: www.siteteste.com.br\033[0;0m
            \033[1m║    \033[0;0mLogo depois, informe a velocidade que deseja fazer o scanner.
            \033[1m║    \033[0;0mLembrando que quanto mais rapido menos precisão vai ter.
            \033[1m║    \033[31m  2)Portas especificas.\033[0;0m
            \033[1m║    \033[0;0mAonde você vai informar exatamente as mesmas coisas, porém, vai ter
            \033[1m║    \033[0;0mque informar também, as portas que você deseja scannear, separando
            \033[1m║    \033[0;0m-as por virgulas.
            \033[1m║    \033[31m   Uso: 21,23,80,443,8080\033[0;0m
            \033[1m║    \033[31m  3)Alcance de portas.\033[0;0m
            \033[1m║    \033[0;0mAonde você vai informar exatamente as mesmas coisas, porém, vai ter
            \033[1m║    \033[0;0mque informar também, uma porta de inicio e uma porta de fim.
            \033[1m║    \033[0;0mO scanner vai verificar desde a porta de inicio até a porta de fim.
            \033[1m║    \033[31m   Uso: Inicio: 0\033[0;0m                                          
            \033[1m║    \033[31m   Uso: Fim: 2000\033[0;0m                                          
            \033[1m║    \033[0;0m\n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            print("""
            \033[1m╠══  \033[1m\033[31mWhoIS.\033[0;0m
            \033[1m║    \033[0;0mO módulo whois, que significa em português: quem é? Foi criado 
            \033[1m║    \033[0;0mpara pessoas saberem mais sobre o site. Ele retorna diversos
            \033[1m║    \033[0;0mdados, tais como: CNPJ, DONO, EMAILS, DATA DE CRIAÇÃO...
            \033[1m║    \033[0;0mUma vez que esses dados podem ajudar o atacante a descobrir
            \033[1m║    \033[0;0mbastante sobre o seu alvo, foi colocado para não precisar usar
            \033[1m║    \033[0;0mo whois tradicional, além de formatar melhor o texto e traduzir.
            \033[1m║    \033[0;0mPara utilizar o módulo, basta acessar o menu scanners/whois e 
            \033[1m║    \033[0;0mpreencher o campo necessario: o alvo.
            \033[1m║    \033[31m    Uso: www.site.com.br\033[0;0m
            \033[1m║    \033[0;0mÉ importante que o site digitado não tenha "/" nem "http://"
            \033[1m║    \033[31m   Uso errado: https://www.site.com.br/\033[0;0m
            \033[1m║    \033[0;0mEm poucos segundos ele ira retornar todas as informações
            \033[1m║    \033[0;0m\n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            print("""
            \033[1m╠══  \033[1m\033[31mHrefs.\033[0;0m
            \033[1m║    \033[0;0mEste módulo foi criado para automatizar uma tarefa que é importante,
            \033[1m║    \033[0;0ma capturação de sites que são referenciados por outro.
            \033[1m║    \033[0;0mExemplo de um href em um html:
            \033[1m║    \033[31m<a href="http://site.com.br/login.php ...."\033[0;0m
            \033[1m║    \033[0;0mPensando no estilo da escrita, o programa procura por "a" e logo em
            \033[1m║    \033[0;0mseguida, procura pelo link indicado pelo "href=".
            \033[1m║    \033[0;0mVale ressaltar que isso possui alguns problemas, ele não consegue
            \033[1m║    \033[0;0mcapturar alguns links que estão no site e acaba pegando alguns links
            \033[1m║    \033[0;0mdo google, facebook, twitter, instagram, etc... que são desnecessarios
            \033[1m║    \033[0;0mentão após a utilização, ele ira perguntar se você deseja visualizar
            \033[1m║    \033[0;0mapenas os hrefs que são do site.
            \033[1m║    \033[0;0mPara utilizar o módulo, basta acessar o menu scanners/hrefs e
            \033[1m║    \033[0;0mpreencher o campo necessario.
            \033[1m║    \033[31m   Uso: www.site.com.br\033[0;0m
            \033[1m║    \033[0;0mÉ importante que o site digitado não tenha "/" nem "http://"
            \033[1m║    \033[31m   Uso errado: https://www.site.com.br/\033[0;0m
            \033[1m║    \033[0;0m\n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            banner()
            print(""" \033[1mMenu de ajuda para usuarios.:\n                                       
            \033[1m\033[31mBrute Force\033[0;0m
            \033[1m║    \033[0;0mMuitas vezes em um pentest, nós não conseguimos levantar dados o
            \033[1m║    \033[0;0msuficiente para entrar em uma conta ou acessar mais informações,
            \033[1m║    \033[0;0mai entra o brute force, traduzindo pro português, força bruta,
            \033[1m║    \033[0;0monde tenta encontrar algo, através de uma lista de palavras. 
            \033[1m╠══  \033[1m\033[31mFTP.\033[0;0m
            \033[1m║    \033[0;0mAlguns sites tem a porta FTP(21) aberta, possibilitando um
            \033[1m║    \033[0;0mataque de força bruta para descobrir a senha do FTP.
            \033[1m║    \033[0;0mFile Transfer Protocol é um protocolo que permite a
            \033[1m║    \033[0;0mtransferência de arquivos para um site.
            \033[1m║    \033[0;0mO uso é bem simples, informe o alvo desejado.
            \033[1m║    \033[0;0mLembrando que o alvo tem que ter a porta 21 aberta, por isso,
            \033[1m║    \033[0;0mfaça um levantamento de dados primeiro.
            \033[1m║    \033[31m   Uso: www.sitedeteste.com\033[0;0m
            \033[1m║    \033[0;0mDepois informe o possivel usuario do FTP.
            \033[1m║    \033[31m   Uso: root\033[0;0m
            \033[1m║    \033[0;0mO programa ira perguntar se você quer gerar uma wordlist, ou
            \033[1m║    \033[0;0mse quer usar uma wordlist já existente, em ambos os casos, o
            \033[1m║    \033[0;0mprograma ira pedir para informar o local/nome onde a wordlist
            \033[1m║    \033[0;0mestá localizada.
            \033[1m║    \033[31m   Uso: /home/user/Documentos/wordlist.txt\033[0;0m
            \033[1m║    \033[0;0mApós isso, o programa já irá fazer o processo para tentar 
            \033[1m║    \033[0;0mdescobrir a senha do FTP.
            \033[1m║    \033[0;0m\n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            print("""
            \033[1m╠══  \033[1m\033[31mGmail.\033[0;0m
            \033[1m║    \033[0;0mO gmail pode ser utilizado para diversas coisas, porém, a utilização 
            \033[1m║    \033[0;0mdele para engenharia social é a mais requisitada. Imagine que seu chefe
            \033[1m║    \033[0;0mlhe envia um email dizendo que esqueceu a senha do FTP, e te pergunta
            \033[1m║    \033[0;0mqual é a senha, você, achando que é realmente seu chefe, informa os dados
            \033[1m║    \033[0;0mperguntados e nem desconfia. Podemos utilizar também para enviar malware.
            \033[1m║    \033[0;0mA utilização é bem simples, requisitando apenas do email que ira atacar e
            \033[1m║    \033[0;0muma wordlist.
            \033[1m║    \033[0;0mPara informar o email é do jeito tradicional:
            \033[1m║    \033[31m   Uso: teste@gmail.com.br\033[0;0m
            \033[1m║    \033[0;0mO programa ira perguntar se você quer gerar uma wordlist, ou
            \033[1m║    \033[0;0mse quer usar uma wordlist já existente, em ambos os casos, o
            \033[1m║    \033[0;0mprograma ira pedir para informar o local/nome onde a wordlist
            \033[1m║    \033[0;0mestá localizada.
            \033[1m║    \033[31m    Uso: /home/user/Documentos/wordlist.txt\033[0;0m
            \033[1m║    \033[0;0mApós isso, o programa já irá fazer o processo para tentar 
            \033[1m║    \033[0;0mdescobrir a senha do GMAIL.
            \033[1m║    \033[0;0m\n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            print("""
            \033[1m╠══  \033[1m\033[31mSubdominio.\033[0;0m
            \033[1m║    \033[0;0mUm site pode ter diversos subdominios, na hora de procurarmos
            \033[1m║    \033[0;0mvulnerabilidades, o dominio principal pode não conter uma vulnerabilidade,
            \033[1m║    \033[0;0mporém, podemos utilizar outros subdominios que tenha. Por isso sempre é
            \033[1m║    \033[0;0mbom no pentest.
            \033[1m║    \033[0;0mExemplo de um subdominio:
            \033[1m║    \033[31m    Ex.: subdominio.site.com.br\033[0;0m
            \033[1m║    \033[0;0mO uso é bem simples, só informar o dominio e uma wordlist.
            \033[1m║    \033[0;0mPara informar o dominio do site:
            \033[1m║    \033[31m   Uso: site.com.br\033[0;0m
            \033[1m║    \033[0;0mO programa ira perguntar se você quer gerar uma wordlist, ou
            \033[1m║    \033[0;0mse quer usar uma wordlist já existente, em ambos os casos, o
            \033[1m║    \033[0;0mprograma ira pedir para informar o local/nome onde a wordlist
            \033[1m║    \033[0;0mestá localizada.
            \033[1m║    \033[31m    Uso: /home/user/Documentos/wordlist.txt\033[0;0m
            \033[1m║    \033[0;0mApós isso, o programa já irá procurar por subdominios no site alvo.
            \033[1m║    \033[0;0m\n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            print("""
            \033[1m╠══  \033[1m\033[31mDiretorio.\033[0;0m
            \033[1m║    \033[0;0mUm site, por ser um computador/servidor, possui diversos diretorios, alguns
            \033[1m║    \033[0;0mque podem nos informar bastante coisa sobre o sistema operacional utilizado,
            \033[1m║    \033[0;0mversões de plugins, programas e até senhas.
            \033[1m║    \033[0;0mO programa procura por diretorios utilizando uma força bruta, requisitando
            \033[1m║    \033[0;0mcada nome da wordlist junto com o alvo.
            \033[1m║    \033[31m    Ex: http://site.com.br/wp-content\033[0;0m
            \033[1m║    \033[0;0mO uso é bem simples, só informar o site alvo e uma wordlist.
            \033[1m║    \033[0;0mPara informar o dominio do site:
            \033[1m║    \033[31m   Uso: http://www.site.com.br/\033[0;0m
            \033[1m║    \033[0;0mÉ importante que se utilize exatamente dessa maneira, pois o programa ira
            \033[1m║    \033[0;0madicionar as palavras após a "/".
            \033[1m║    \033[0;0mO programa ira perguntar se você quer gerar uma wordlist, ou
            \033[1m║    \033[0;0mse quer usar uma wordlist já existente, em ambos os casos, o
            \033[1m║    \033[0;0mprograma ira pedir para informar o local/nome onde a wordlist
            \033[1m║    \033[0;0mestá localizada.
            \033[1m║    \033[31m    Uso: /home/user/Documentos/wordlist.txt\033[0;0m
            \033[1m║    \033[0;0mApós isso, o programa já irá procurar por diretorios no site alvo.
            \033[1m║    \033[0;0m\n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            print("""
            \033[1m╠══  \033[1m\033[31mGerador de wordlist.\033[0;0m
            \033[1m║    \033[0;0mNa hora de executar um brute force precisamos de uma wordlist,
            \033[1m║    \033[0;0mfoi pensando nisso que desenvolvemos o módulo para gerar elas.
            \033[1m║    \033[31m   1) Basica\033[0;0m
            \033[1m║    \033[0;0mA primeira informação que o programa precisa saber é uma
            \033[1m║    \033[0;0mpalavra que você, talvez, queira adicionar na lista.
            \033[1m║    \033[31m   Uso: Lucas\033[0;0m
            \033[1m║    \033[31m   Uso²: \033[0;0m
            \033[1m║    \033[0;0mPodemos deixar em branco para não utilizar palavras.
            \033[1m║    \033[0;0mEntão ele irá pedir os caracteres para formar a wordlist,
            \033[1m║    \033[0;0mcada caracter vai ser utilizado para gerar uma sequencia.
            \033[1m║    \033[31m   Uso: 123456\033[0;0m
            \033[1m║    \033[0;0mIsso ira formar uma wordlist numerica.
            \033[1m║    \033[0;0mO programa irá pedir a quantidade de caracteres, em outras
            \033[1m║    \033[0;0mpalavras, o tamanho da senha que ele vai formar.
            \033[1m║    \033[0;0mO programa não conta o tamanho da senha junto com a palavra
            \033[1m║    \033[0;0madicional, logo se eu colocar 6, ele irá formar uma senha
            \033[1m║    \033[0;0mcom tamanho de 6 digitos mais o tamanho da palavra adicional.
            \033[1m║    \033[31m   Uso: 6\033[0;0m
            \033[1m║    \033[0;0mPor fim o programa vai perguntar o nome que você deseja salvar
            \033[1m║    \033[0;0ma wordlist.
            \033[1m║    \033[31m   Uso: numerica.txt\033[0;0m
            \033[1m║    \033[0;0mO programa irá gerar a wordlist e perguntar se você quer mover
            \033[1m║    \033[0;0mela para algum diretorio especifico.
            \033[1m║    \033[31m   Uso: /home/user/Documentos/Wordlists/\033[0;0m
            \033[1m╚════════════════════════════════════════════════════════════════════════\033[0;0m
            \n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            banner()
            print(""" \033[1mMenu de ajuda para usuarios.:\n                                       
            \033[1m\033[31mCriptografia.\033[0;0m
            \033[1m║    \033[0;0mUma das coisas mais importante da segurança é a criptografia,
            \033[1m║    \033[0;0mque é utilizada para controlar a disponibilidade de algo. 
            \033[1m║    \033[0;0mMuitas criptografias possui um caminho reverso, que nos permite
            \033[1m║    \033[0;0mdecodificar aquele codigo, porém, algumas não possui, as chamadas
            \033[1m║    \033[0;0m"Hashs", elas possuem tamanho fixo e não possuem caminho de volta. 
            \033[1m║    \033[0;0mUnica forma de descobrir a senha é criptografando e verificando se
            \033[1m║    \033[0;0ma hash que foi gerada é igual a hash que está procurando. Este módulo
            \033[1m║    \033[0;0mfoi criado pensando na quebra dessas criptografias, que impedem um
            \033[1m║    \033[0;0mprofissional de saber sobre algo, ou alguma coisa.
            \033[1m╠══  \033[1m\033[31mHash linux\033[0;0m
            \033[1m║    \033[0;0mO linux possui uma segurança em que a senha dos usuarios é criptografadas
            \033[1m║    \033[0;0mutilizando algoritimos hashs, para conseguir a senha, o programa só necessita
            \033[1m║    \033[0;0mda hash que vai ser descriptografada e uma wordlist.
            \033[1m║    \033[31m    Uso: $1$CLDZNZCB$PbOINV7W3sMIvlaTsrkLi1\033[0;0m
            \033[1m║    \033[0;0mO programa ira perguntar se você quer gerar uma wordlist, ou
            \033[1m║    \033[0;0mse quer usar uma wordlist já existente, em ambos os casos, o
            \033[1m║    \033[0;0mprograma ira pedir para informar o local/nome onde a wordlist
            \033[1m║    \033[0;0mestá localizada.
            \033[1m║    \033[31m    Uso: /home/user/Documentos/wordlist.txt\033[0;0m
            \033[1m║    \033[0;0mApós isso, o programa já irá procurar a senha equivalente a hash informada.
            \033[1m║    \033[0;0m\n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            print("""
            \033[1m╠══  \033[1m\033[31mHashs.\033[0;0m
            \033[1m║    \033[0;0mTodas hashs a seguir é necessario as mesmas coisas, a hash alvo e
            \033[1m║    \033[0;0muma wordlist para a quebra da hash, porém existe diversos algoritmos.
            \033[1m║    \033[31m   1- MD5\033[0;0m
            \033[1m║    \033[31m    Uso: 63a9f0ea7bb98050796b649e85481845\033[0;0m
            \033[1m║    \033[31m   2- SHA1\033[0;0m
            \033[1m║    \033[31m    Uso: dc76e9f0c0006e8f919e0c515c66dbba3982f785\033[0;0m
            \033[1m║    \033[31m   3- SHA224\033[0;0m
            \033[1m║    \033[31m    Uso: 871ce144069ea0816545f52f09cd135d1182262c3b235808fa5a3281\033[0;0m
            \033[1m║    \033[31m   4- SHA256\033[0;0m
            \033[1m║    \033[31m    Uso: 4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2\033[0;0m
            \033[1m║    \033[31m   5- SHA384\033[0;0m
            \033[1m║    \033[31m    Uso: 7ed8c2c790aa83d6c3e404b5368f6832c18d46a0e98b9c7a7a5e3ef823e2c9f0\033[0;0m
            \033[1m║    \033[31m    ...  e310abbf6f7ea9d9d883ccb64ec2736a\033[0;0m
            \033[1m║    \033[31m   6- SHA512\033[0;0m
            \033[1m║    \033[31m    Uso: 99adc231b045331e514a516b4b7680f588e3823213abe901738bc3ad67b2f6fc\033[0;0m
            \033[1m║    \033[31m    ...  b3c64efb93d18002588d3ccc1a49efbae1ce20cb43df36b38651f11fa75678e8\033[0;0m
            \033[1m║    \033[0;0m
            \033[1m╠══  \033[1m\033[31mBase64.\033[0;0m
            \033[1m║    \033[0;0mBase64 é uma criptografia que possui um caminho de volta, logo, é facil
            \033[1m║    \033[0;0mdescriptografar, só precisamos do texto criptografado.
            \033[1m║    \033[0;0mTemos dois tipos de utilizar:
            \033[1m║    \033[31m   1) Encode\033[0;0m 
            \033[1m║    \033[31m    Uso: Texto\033[0;0m
            \033[1m║    \033[0;0mÉ aonde você criptografa um texto.
            \033[1m║    \033[31m   2) Decode\033[0;0m 
            \033[1m║    \033[31m    Uso: VGV4dG8=\033[0;0m
            \033[1m║    \033[0;0mÉ aonde você descriptografa um texto.
            \033[1m╚════════════════════════════════════════════════════════════════════════\033[0;0m
            \n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║ Aperte CRTL+C para sair da ajuda             Aperte ENTER para ler mais ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            banner()
            print(""" \033[1mMenu de ajuda para usuarios.:\n                                       
            \033[1m\033[31mAtualizar o everyuse.\033[0;0m
            \033[1m║    \033[0;0mQuando o desenvolvedor lança mais uma versão do everyuse o
            \033[1m║    \033[0;0mprograma avisa que existe uma atualização a ser feita, dando
            \033[1m║    \033[0;0mconforto e automoção para atualizações, logo você nunca irá
            \033[1m║    \033[0;0mperder uma versão do everyuse.
            \033[1m║    \033[0;0mCada versão procuramos melhorar cada vez mais o everyuse, para
            \033[1m║    \033[0;0mdar segurança e eficiencia em seus pentests.
            \033[1m║    \033[0;0mEncontrou algum erro, tem dicas ou quer ajudar no desenvolvimento?
            \033[1m║    \033[0;0mMande um email para:
            \033[1m║    \033[0;0m         \033[36mlucas.simoni10@gmail.com\033[0;0m
            \033[1m║    \033[0;0m\033[33m\033[1mA liberdade foi confundida com a democracia.\033[0;0m
            \033[1m╚════════════════════════════════════════════════════════════════════════\033[0;0m
            \n""")
            print('    ╔═════════════════════════════════════════════════════════════════════════╗')
            print('    ║                         Aperte ENTER para sair                          ║')
            print('    ╚═════════════════════════════════════════════════════════════════════════╝')
            input()
            sairmenu = True
        except KeyboardInterrupt:
            sairmenu = True

#Menu INICIAL
try:
    while sair == False:
        banner()
        print("""  \033[1mSelecione uma opção:
        
        \033[1m1)\033[0;0m Engenharia social
        \033[1m2)\033[0;0m Scanners
        \033[1m3)\033[0;0m Brute Force
        \033[1m4)\033[0;0m Criptografia
        \033[1m5)\033[0;0m Atualizar o everyuse."""+ndatl+"""
        \033[1m6)\033[0;0m Ajuda
        
        \033[1m0)\033[0;0m Sair
        """)
        opt = str(input(cm))
        if opt == '0':
            sairprograma()
        elif opt == '1':
            engenhariasocial()
        elif opt == '2':
            scanners()
        elif opt == '3':
            bruteforce()
        elif opt == '4':
            criptografia()
        elif opt == '5':
            atualizacao()
        elif opt == '6':
            ajuda()
        else:
            continue
except KeyboardInterrupt:
    print('');sairprograma()
except EOFError:
    sairprograma()
