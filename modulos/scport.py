#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.
import socket

portas = {21: 'FTP',
          22: 'SSH',
          23: 'TELNET',
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