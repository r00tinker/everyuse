#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.
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
\033[0;0m\033[1m8888888888     Y8P     8888888888 888   T88b    888     \033[33m\033[1m"Y88888P"   "Y8888P"  8888888888
\033[0;0m\033[1m\033[31m                                        ᶠᶸᶜᵏ ˢᵒᶜᶤᵉᵗʸ\033[0;0m
    """)

#Importar os modulos.
try:
    from modulos import enviodeemail
    from modulos import scport
    from modulos import wordlistgnt
    from modulos import bfftp
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
cmwl = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33mwordlist\033[0;0m» '
cmwlbc = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33mwordlist\033[0;0m/\033[1m\033[33mbasica\033[0;0m» '
cmegsc = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m» '
cmscs = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m» '
cmbfs = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m» '
btftp = '\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mbruteforce\033[0;0m/\033[1m\033[33mftp\033[0;0m» '
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

if os.path.exists('.tmpup/'):
    banner()
    print(' O everyuse foi atualizado com sucesso !')
    os.system('rm -rf .tmpup/')
    os.system('rm -rf updeve.sh')
    complett()

if 'v0.5-08/09' not in verif.text:
    ndatl = '(Versão nova disponivel.)'
else:
    ndatl = ''

def atualizacao():
    banner()
    if 'v0.5-08/09' not in verif.text:
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
                os.system('rm -rf modulos/')
                os.system('mkdir modulos/')
                os.system('mkdir .tmpup/')
                for linha in upmodulos.text.split():
                    os.system('cd modulos/ && wget -q ' + linha)
                os.system('echo "#!/bin/bash" > updeve.sh')
                os.system('echo "rm -rf everyuse" >> updeve.sh')
                os.system('echo "mv everyuse.py everyuse" >> updeve.sh')
                os.system('echo "chmod +x everyuse" >> updeve.sh')
                os.system('echo "exit" >> updeve.sh')
                os.system('chmod +x updeve.sh')
                print(' Abra novamente o everyuse para concluir a atualização.')
                complett()
                os.system('./updeve.sh')
                exit(0)
            elif sorn.lower() == 'n':
                sairmenu = True
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
        try:
            host = input(btftp + 'Alvo: ')
            try:
                ip = socket.gethostbyname(host)
            except:
                print('Site inválido.')
                continue
            user = input(btftp + 'Usuario: ')
            print("""  \033[1mSelecione uma opção:

                \033[1m1)\033[0;0m Gerar uma wordlist
                \033[1m2)\033[0;0m Usar uma wordlist

                \033[1m0)\033[0;0m Voltar
                        """)
            opt = int(input(btftp))
            if opt == 0:
                sairmenu = True

            # Gerar uma wordlist e selecionar ela
            elif opt == 1:
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
            elif opt == 2:
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
                bfftp.bruteforce(wl, user, ip)
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
        wordlistgnt.gerarwl(adicional, caracincl, taman, nomearq)
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
            opt = int(input(cmptsc))
            if opt == 0:
                sairmenu = True
            elif opt == 1 or opt == 2 or opt == 3:
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
                if opt == 3:
                    cmc = int(input(cmptsc+'Porta inicio: '))
                    fip = int(input(cmptsc+'Porta final: '))
                    fi = fip + 1
                    scport.scportespe(site, velocidade, range(cmc, fi))
                    complett()
                if opt == 2:
                    print(' Separe as portas por virgulas e sem espaço.')
                    ports = str(input(cmptsc+'Portas: '))
                    portas = ports.split(',')
                    scport.scportespe(site, velocidade, portas)
                    complett()
                if opt == 1:
                    scport.scport(site, 1, velocidade)
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
                opx = int(input(cmevem))
                if opx == 0:
                    sairmenu = True
                    tipoanx = 0
                    nomearq = ''
                    anexar = 'sem'
                    break
                elif opx == 1:
                    print('Exemplo.: /home/user/Documentos/arquivo.png')
                    tipoanx = 1
                    anexar = str(input(cmevem + 'Arquivo: '))
                    nomearq = str(input(cmevem + 'Nome do arquivo: '))
                    if os.path.exists(anexar):
                        sairmenu = True
                    else:
                        print('Arquivo não encontrado.')
                elif opx == 2:
                    print('Exemplo.: /home/user/Documentos/arquivo.mp3')
                    tipoanx = 2
                    anexar = str(input(cmevem + 'Arquivo: '))
                    nomearq = str(input(cmevem + 'Nome do arquivo: '))
                    if os.path.exists(anexar) and anexar.endswith('.mp3') or anexar.endswith('.ogg'):
                        sairmenu = True
                    else:
                        print(' Arquivo não encontrado.')
                        print(' Apenas arquivos .mp3 ou .ogg')
                elif opx == 3:
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
            enviodeemail.envio(de, passw, nomeex, para, assunto, corpocom, servidor, porta, anexar, tipoanx, nomearq, qtd)
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
            opt = int(input(cmevem))
            if opt == 0:
                sairmenu = True
            elif opt == 1:
                enviaremail('smtp.gmail.com', 587)
            elif opt == 2:
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
            opt = int(input(cmegsc))
            if opt == 0:
                sairmenu = True
            elif opt == 1:
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
    
            \033[1m0)\033[0;0m Voltar
                """)
            opt = int(input(cmscs))
            if opt == 0:
                sairmenu = True
            elif opt == 1:
                portpref()
    except KeyboardInterrupt:
        sairmenu = True
    except ValueError:
        scanners()
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
            \033[1m9)\033[0;0m Gerador de wordlist
    
            \033[1m0)\033[0;0m Voltar
                """)
            opt = int(input(cmbfs))
            if opt == 0:
                sairmenu = True
                break
            elif opt == 9:
                gerarwordlist()
            elif opt == 1:
                bruteftp()
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
            opt = int(input(cmwl))
            if opt == 0:
                sairmenu = True
            elif opt == 1:
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
            \033[1m╚════════════════════════════════════════════════════════════════════════\033[0;0m
            \n""")
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

try:
    while sair == False:
        banner()
        print("""  \033[1mSelecione uma opção:
        
        \033[1m1)\033[0;0m Engenharia social
        \033[1m2)\033[0;0m Scanners
        \033[1m3)\033[0;0m Brute Force
        \033[1m4)\033[0;0m Atualizar o everyuse."""+ndatl+"""
        \033[1m5)\033[0;0m Ajuda
        
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
            atualizacao()
        elif opt == '5':
            ajuda()
        else:
            continue
except KeyboardInterrupt:
    print('');sairprograma()
except EOFError:
    sairprograma()
