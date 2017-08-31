#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
try:
    import os
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage
    from email.mime.text import MIMEText
    import getpass
    import socket
    from socket import gaierror
except ImportError:
    print('Erro ao importar as bibliotecas.')

########################################################################################################################
#                                               ENVIO DE EMAIL                                                         #
########################################################################################################################
def envio(remetente, senha, de, destinatario, assunto, corpo, servidor, porta, anexo, tipoanexo):

    msg = MIMEMultipart()
    msg['From'] = de
    msg['Subject'] = assunto
    texto = MIMEText(corpo, 'plain')
    msg.attach(texto)

    if tipoanexo == 1:
        aa = open(anexo, 'rb')
        img = MIMEImage(aa.read())
        msg.attach(img)
        aa.close()
    else:
        tipoanexo = 0


    server = smtplib.SMTP(servidor, porta)
    server.starttls()
    server.login(remetente,senha)
    server.sendmail(remetente, destinatario, str(msg))
    server.quit()
########################################################################################################################
#                                               ENVIO DE EMAIL                                                         #
########################################################################################################################
'''------------------------------------------------------------------------------------------------------------------'''
########################################################################################################################
#                                               SCANNER DE PORTAS                                                      #
########################################################################################################################

portas = {21: 'FTP',
          22: 'SSH',
          25: 'SMTP',
          26: 'RSFTP',
          53: 'DOMAIN',
          80: 'HTTP',
          106: 'POP3PW',
          110: 'POP3',
          113: 'IDENT',
          139: 'NETBIOS-SSN',
          143: 'IMAP',
          256: 'FW1-SECUREREMOTE',
          443: 'HTTPS',
          465: 'SMTPS',
          554: 'RTSP',
          587: 'SMTP',
          993: 'IMAPS',
          995: 'POP3S',
          1720: 'H323Q931',
          1723: 'PPTP',
          2022: 'DOWN',
          2525: 'MS-V-WORLDS',
          3306: 'MYSQL',
          5222: 'XMPP-CLIENT',
          8080: 'HTTP-PROXY',
          9090: 'ZEUS-ADMIN',
          8443: 'HTTPS-ALT',
          9102: 'JETDIRECT'
          }

porta_aberta = []

def scport(site, tipo, v):
    if str(tipo) == '1':
        ip = socket.gethostbyname(site)
        #Para cada porta, saber se ela esta aberta e printar
        print('\n Iniciado o scanner.\n')
        print('    PORTA  |  STATUS  |  SERVIÇO  ')
        for porta in portas:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(v)
            c = s.connect_ex((ip, porta))
            servico = portas[porta]
            #Se ela estiver aberta
            if c == 0:
                porta_aberta.append(porta)
                #lista_servico.append(servico)
                if len(str(porta)) == 3:
                    print(' \033[0;0m>   ', porta, '    \033[32mABERTA    \033[34m', servico )
                elif len(str(porta)) == 4:
                    print(' \033[0;0m>   ', porta, '   \033[32mABERTA    \033[34m', servico )
                else:
                    print(' \033[0;0m>   ', porta, '     \033[32mABERTA    \033[34m', servico )
        if porta_aberta == []:
            print('\n Nenhuma porta aberta. Tente regular a velocidade.')

def scportespe(site, v, portasesp):
    ip = socket.gethostbyname(site)
    print('\n Iniciado o scanner.\n')
    print('    PORTA  |  STATUS  |  SERVIÇO  ')
    for porta in portasesp:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(v)
        c = s.connect_ex((ip, int(porta)))
        if int(porta) in portas:
            servico = portas[int(porta)]
        else:
            servico = '----'
        if c == 0:
            porta_aberta.append(int(porta))
            # lista_servico.append(servico)
            if len(str(porta)) == 3:
                print(' \033[0;0m>   ', porta, '    \033[32mABERTA    \033[34m', servico)
            elif len(str(porta)) == 4:
                print(' \033[0;0m>   ', porta, '   \033[32mABERTA    \033[34m', servico)
            elif len(str(porta)) == 1:
                print(' \033[0;0m>   ', porta, '      \033[32mABERTA      \033[34m', servico)
            else:
                print(' \033[0;0m>   ', porta, '     \033[32mABERTA      \033[34m', servico)
        else:
            porta_aberta.append(int(porta))
            if len(str(porta)) == 3:
                print(' \033[0;0m>   ', porta, '    \033[31mFECHADA     \033[34m', servico)
            elif len(str(porta)) == 4:
                print(' \033[0;0m>   ', porta, '   \033[31mFECHADA     \033[34m', servico)
            elif len(str(porta)) == 1:
                print(' \033[0;0m>   ', porta, '      \033[31mFECHADA     \033[34m', servico)
            else:
                print(' \033[0;0m>   ', porta, '     \033[31mFECHADA     \033[34m', servico)
    if porta_aberta == []:
        print('\n Nenhuma porta aberta. Tente regular a velocidade.')
########################################################################################################################
#                                               SCANNER DE PORTAS                                                      #
########################################################################################################################

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

#Variaveis de menu
sair = False
sairmenuum = False
sairmenudois = False
sairmenutres = False
sairmenuquatro = False

#Mensagem ao sair do programa
def sairprograma():
    print('\n Obrigado por utilizar o \033[1m\033[33meveryuse\033[0;0m para suas tarefas.')
    print('\n    A liberdade foi confundida com a democracia. \n')
    global sair
    sair = True

#Mensagem ao completar uma tarefa
def complett():
    print('\n     \033[0;0mAperte \033[1m\033[33m[ENTER]\033[0;0m para voltar.')
    complettt = input('')


#########################################################################################################################
#                                         INICIO - MENU - PORT SCAN                                                     #
#########################################################################################################################
def portpref():
    sairport = False
    try:
        while sairport == False:
            banner()
            print("""  \033[1mSelecione um tipo:
    
        \033[1m1)\033[0;0m Portas padroes
        \033[1m2)\033[0;0m Portas especificas
        \033[1m3)\033[0;0m Alcance de portas
    
        \033[1m0)\033[0;0m Voltar
                """)
            opt = int(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mportscan\033[0;0m» '))
            if opt == 0:
                sairport = True
            elif opt == 1 or opt == 2 or opt == 3:
                velo = 0
                velocm = False
                print(' Ex.: www.siteteste.com')
                site = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mportscan\033[0;0m» Site: '))
                while velocm == False:
                    print("""  \033[1mSelecione uma velocidade:
        
        \033[1m1)\033[0;0m Rapido (Menos preciso)
        \033[1m2)\033[0;0m Medio (Preciso)
        \033[1m3)\033[0;0m Lento (Mais preciso)
                        """)
                    velo = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mportscan\033[0;0m» Velocidade: '))
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
                    cmc = int(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mportscan\033[0;0m» Porta inicio: '))
                    fip = int(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mportscan\033[0;0m» Porta final: '))
                    fi = fip + 1
                    scportespe(site, velocidade, range(cmc, fi))
                    complett()
                if opt == 2:
                    print(' Separe as portas por virgulas e sem espaço.')
                    ports = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m/\033[1m\033[33mportscan\033[0;0m» Portas: '))
                    portas = ports.split(',')
                    scportespe(site, velocidade, portas)
                    complett()
                if opt == 1:
                    scport(site, 1, velocidade)
                    complett()
    except gaierror:
        print('\n O site informado esta incorreto')
        complett()
    except KeyboardInterrupt:
        complett()
        sairport = True
    except ValueError:
        portpref()


#########################################################################################################################
#                                            FIM - MENU - PORT SCAN                                                     #
#########################################################################################################################
'''------------------------------------------------------------------------------------------------------------------'''
#########################################################################################################################
#                                            INICIO - ENVIAR EMAIL                                                      #
#########################################################################################################################
def enviaremail(servidor, porta):
    de = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Seu email: '))
    passw = getpass.getpass('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Sua senha: ')
    nomeex = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Nome exibido: '))
    print('Obs.: Utilize "," para determinar o fim de um email.')
    para = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Enviar para: '))
    tolist = para.split(',')
    assunto = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Assunto: '))
    soun = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Deseja anexar um arquivo ? [s/n]: '))
    if soun == 's' or soun == 'S':
        sbxok = False
        while sbxok == False:
            print("""  \033[1mSelecione um tipo de anexo:

        \033[1m1)\033[0;0m Imagem

        \033[1m0)\033[0;0m Voltar
            """)
            opx = int(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» '))
            if opx == 0:
                sbxok = True
                tipoanx = 0
                anexar = 'sem'
                break
            elif opx == 1:
                print('Exemplo.: /home/user/Documentos/arquivo.png')
                tipoanx = 1
                anexar = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Arquivo: '))
                if os.path.exists(anexar):
                    sbxok = True
                else:
                    print('Arquivo nao encontrado.')
            #elif opx == 2:
                #print('Exemplo.: /home/user/Documentos/arquivo.pdf')
                #tipoanx = 2
                #anexar = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Arquivo: '))
                #sbxok = True
    else:
        anexar = 'sem'
        tipoanx = 0
    print('Obs.: Utilize "</fim>" para terminar o texto.')
    corpocom = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Texto: '))
    corpolinha = str('')
    i = 1
    while corpolinha != '</fim>':
        i += 1
        corpolinha = str(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» '+ str(i) + 'º Linha: '))
        if corpolinha != '</fim>':
            corpocom += '\n' + corpolinha
        else:
            break

    qtd = int(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» Quantidade de envios: '))
    qtdc = range(0, qtd)
    try:
        for i in qtdc:
            envio(de, passw, nomeex, tolist, assunto, corpocom, servidor, porta, anexar, tipoanx)
            qt = i+1
            print(str(qt) + 'º email enviado...')
        print('\nTodos os emails foram enviados corretamente !')
        complett()
    except smtplib.SMTPAuthenticationError:
        print('\nNão foi possivel enviar os emails pois você inseriu o seu email e/ou senha errados.')
        complett()

    except smtplib.SMTPRecipientsRefused:
        print('\nNão foi possivel enviar os emails pois você inseriu um destinatario inexistente.')
        complett()
#########################################################################################################################
#                                               FIM - ENVIAR EMAIL                                                      #
#########################################################################################################################


#Menu para saber o servidor de email usado pela pessoa.
def seuservidor():
    global sairp
    sairp = False
    try:
        while sairp == False:
            banner()
            print("""  \033[1mSelecione seu servidor:
    
        \033[1m1)\033[0;0m Gmail
        \033[1m2)\033[0;0m Outlook
    
        \033[1m0)\033[0;0m Voltar
            """)
            opt = int(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m/\033[1m\033[33memails\033[0;0m» '))
            if opt == 0:
                sairp = True
            elif opt == 1:
                enviaremail('smtp.gmail.com', 587)
            elif opt == 2:
                enviaremail('smtp.live.com', 587)
    except KeyboardInterrupt:
        sairp = True
    except ValueError:
        seuservidor()

#MENU DE ENGENHARIA SOCIAL
def engenhariasocial():
    try:
        global sairmenuum
        sairmenuum = False
        while sairmenuum == False:
            banner()
            print("""  \033[1mSelecione uma opçao:
    
        \033[1m1)\033[0;0m Envio de emails
    
        \033[1m0)\033[0;0m Voltar
            """)
            opt = int(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mengsocial\033[0;0m» '))
            if opt == 0:
                sairmenuum = True
            elif opt == 1:
                seuservidor()
    except KeyboardInterrupt:
        sairmenuum = True
    except ValueError:
        engenhariasocial()

#MENU DE SCANNERS
def scanners():
    global sairmenudois
    sairmenudois = False
    try:
        while sairmenudois == False:
            banner()
            print("""  \033[1mSelecione um scanner:
    
            \033[1m1)\033[0;0m Porta
    
            \033[1m0)\033[0;0m Voltar
                """)
            opt = int(input('\033[1m\033[33meveryuse\033[0;0m/\033[1m\033[33mscanners\033[0;0m» '))
            if opt == 0:
                sairmenudois = True
            elif opt == 1:
                portpref()
    except KeyboardInterrupt:
        sairmenudois = True
    except ValueError:
        scanners()


#MENU DE BRUTE FORCES
#def bruteforce():
#    while sairmenutres == False:
#        banner()
#        complett()


#AJUDA
def ajuda():
    global sairmenuquatro
    sairmenuquatro = False
    while sairmenuquatro == False:
        banner()
        print(""" \033[1mMenu de ajuda para usuarios.: (Versao de testes)
        
        \033[1m1-\033[0;0m Engenharia social
        | Para anexar um arquivo(imagem), basta informar o caminho da imagem ao pedir.
        |_Caso o programa nao encontre tal arquivo, ele vai pedir o caminho novamente.
        |
        | Para enviar para mais de uma pessoa, basta informar os emails delimitando com uma 
        | virgula.
        |_Exemplo.: testedeemail@gmail.com,testedeemail@outlook.com,testedeemail@hotmail.com
        \033[1m2)\033[0;0m Scanners
        | Sao diversos tipos de scanners
        |_No momento, apenas com portscan.
        \033[1m3)\033[0;0m Brute Force [Em breve]
        |_Em novas versoes.
        \033[1m4)\033[0;0m Ajuda
        |_Sem muito detalhes, novas versoes com tudo atualizado em breve.
        \033[1m5)\033[0;0m Sobre
        |_Versao.: 0.1-30/08 (versao de teste)
            
        """)
        complett()
        sairmenuquatro = True

try:
    while sair == False:
        banner()
        print("""  \033[1mSelecione uma opçao:
        
        \033[1m1)\033[0;0m Engenharia social
        \033[1m2)\033[0;0m Scanners
        \033[1m3)\033[0;0m Brute Force [Em breve]
        \033[1m4)\033[0;0m Ajuda
        
        \033[1m0)\033[0;0m Sair
        """)
        opt = str(input('\033[1m\033[33meveryuse\033[0;0m» '))
        if opt == '0':
            sairprograma()
        elif opt == '1':
            engenhariasocial()
        elif opt == '2':
            scanners()
        #elif opt == '3':
            #bruteforce()
        elif opt == '4':
            ajuda()
        else:
            continue
except KeyboardInterrupt:
    print('');sairprograma()
