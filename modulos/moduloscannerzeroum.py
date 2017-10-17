#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.

#Importar as bibliotecas necessarias
import socket, requests, re
from bs4 import BeautifulSoup

def porta(site, tipo, v):
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

def portaespecificada(site, v, portasesp):
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

def whois(alvo):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("200.160.2.3",43))
    s.send(alvo.encode())
    resp = s.recv(2048)
    infos = str(resp.decode('ISO-8859-1'))
    for linha in infos.splitlines():
        if linha.startswith('%'):
            continue
        else:
            info = linha.split(':')
            if linha.startswith('domain'):
                print('» \033[1mDominio:\033[0;0m'+info[1])
            elif linha.startswith('ownerid'):
                print('» \033[1mCNPJ:\033[0;0m    '+info[1])
            elif linha.startswith('owner-c'):
                print('» \033[1mDono:\033[0;0m    '+info[1])
            elif linha.startswith('owner'):
                print('» \033[1mDono:\033[0;0m  '+info[1])
            elif linha.startswith('responsible'):
                print('» \033[1mResponsavel:\033[0;0m '+info[1])
            elif linha.startswith('country'):
                print('» \033[1mPais:\033[0;0m    '+info[1])
            elif linha.startswith('admin'):
                print('» \033[1mAdmin:\033[0;0m   '+info[1])
            elif linha.startswith('tech'):
                print('» \033[1mTech:\033[0;0m   '+info[1])
            elif linha.startswith('nse'):
                print('» \033[1mNserver:\033[0;0m '+info[1])
            elif linha.startswith('status'):
                print('» \033[1mStatus:\033[0;0m '+info[1])
            elif linha.startswith('person'):
                print('» \033[1mPessoa:\033[0;0m '+info[1])
            elif linha.startswith('e-mail'):
                print('» \033[1mEmail:\033[0;0m  '+info[1])
            elif linha.startswith('cre'):
                print('» \033[1mCriado:\033[0;0m  '+info[1])
            elif linha.startswith('cha'):
                print('» \033[1mModif:\033[0;0m   '+info[1])
            elif linha.startswith('exp'):
                print('» \033[1mExpira:\033[0;0m  '+info[1])
            elif linha.startswith('n') or linha.startswith('b'):
                print("» \033[1m"+info[0]+":\033[0;0m "+info[1])
            else:
                print('+--------------------------------------+')

def href(alvo, ip):
    try:
        site = requests.get('http://' + alvo)
    except requests.exceptions.ConnectionError:
        print(' \033[31m\033[1mErro na conexão.\033[0;0m')
        exit()
    print('\n\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
    print('\033[1mIP do alvo:\033[0;0m', ip)
    print('\033[1mDominio alvo:\033[0;0m', alvo)
    print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m\n')
    print('\033[32m\033[1m» Executando o programa...\033[0;0m')
    html = BeautifulSoup(site.text, 'lxml')
    i = 0
    urlsencontrada = []
    urlsencontrada2 = []
    redesocial = []
    print('\033[32m\033[1m» Procurando por hrefs no site principal...\033[0;0m')
    for item in html.find_all('a'):
        try:
            link = item.attrs['href']
        except:
            continue

        if link.startswith('http'):
            if link in urlsencontrada:
                continue
            else:
                if link == 'http://' + alvo or link == 'http://' + alvo + '/':
                    continue
                else:
                    i += 1
                    urlsencontrada.append(link)
        else:
            if link.endswith('.php') or link.endswith('html') or link.endswith('htm'):
                urlformatada = 'http://' + alvo + '/' + link
                testesite = requests.get(urlformatada)
                if testesite.ok == True:
                    i += 1
                    urlsencontrada.append(urlformatada)
                else:
                    continue
            else:
                continue
    if i == 0:
        print(' Não encontramos nenhum href :c')
    else:
        ii = 0
        print('\n\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
        print('\033[1m» Scanner finalizado com sucesso...\033[0;0m')
        print('\033[1m» Encontramos', str(i), 'hrefs.\033[0;0m')
        yorn = input('\033[1m» Deseja visualizar apenas hrefs do site informado? [S/n]\033[0;0m')
        print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m\n')
        if yorn.lower() == 's' or yorn.lower() != 'n' and yorn.lower() != 's':
            for url in urlsencontrada:
                if url.startswith("http://" + alvo) or url.startswith("https://" + alvo):
                    ii +=1
                    print('»', url)
                else:
                    continue
            for url in urlsencontrada2:
                if url.startswith("http://" + alvo) or url.startswith("https://" + alvo):
                    ii +=1
                    print('»', url)
                else:
                    continue
        elif yorn.lower() == 'n':
            for url in urlsencontrada:
                print('»', url)
            for url in urlsencontrada2:
                print('»', url)
            for url in redesocial:
                print('»', url, '[REDE SOCIAL]')

        if ii < 1:
            print(' \033[31mNão conseguimos encontrar sites exatamente como informado :c\033[0;0m')
            print(' \033[1mExibindo todos:\033[0;0m\n')
            for url in urlsencontrada:
                print('»', url)
            for url in urlsencontrada2:
                print('»', url)
            for url in redesocial:
                print('»', url, '[REDE SOCIAL]')

def emailsc(alvo, ip):
    try:
        site = requests.get('http://' + alvo)
    except requests.exceptions.ConnectionError:
        print(' \033[31m\033[1mErro na conexão.\033[0;0m')
        exit()
    print('\n\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m')
    print('\033[1mIP do alvo:\033[0;0m', ip)
    print('\033[1mDominio alvo:\033[0;0m', alvo)
    print('\033[32m+\033[0;1m--------------------------\033[32m+\033[0;0m\n')
    html = BeautifulSoup(site.text, 'lxml')
    urlsencontrada = []
    listaemails = []
    urlsencontrada.append('http://'+alvo)
    for item in html.find_all('a'):
        try:
            link = item.attrs['href']
        except:
            continue

        if link.startswith('http'):
            if link in urlsencontrada:
                continue
            else:
                urlsencontrada.append(link)
        else:
            if link.endswith('.php'):
                formatando_url = alvo + '/' + link
                testeSite = requests.get(formatando_url)
                if testeSite.ok == True:
                    urlsencontrada.append(formatando_url)
                else:
                    continue
            else:
                continue

    for i in urlsencontrada:
        try:
            req = requests.get(i)
        except:
            continue
        novoemail = list(re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z0-9\.-]+', req.text, re.I))
        for email in novoemail:
            if not email in listaemails:
                if email.endswith('.png'):
                    continue
                elif email.endswith('.jpg'):
                    continue
                else:
                    print('»',email)
                    listaemails.append(email)
            else:
                continue

def ipinfo(ipz, opt):
    if opt == '1':
        req = requests.get('https://api.infoip.io')
    elif opt == '2' or opt == '3':
        req = requests.get('https://api.infoip.io/'+ipz)
    conte = req.text.split(':')
    ip = conte[1].split('"')
    if ip[1] == '188.24.183.216':
        print('\n[!] Algo deu errado! As informações exibidas não são reais.')
    cs = conte[2].split('"')
    cl = conte[3].split('"')
    reg = conte[4].split('"')
    city = conte[5].split('"')
    ltd = conte[6].split('"')
    ltd = ltd[0].split(',')
    lgd = conte[7].split('"')
    lgd = lgd[0].split(',')
    cp = conte[8].split('"')
    fh = conte[9].split('"')
    print('\n\033[32m+\033[0;1m------------------------------\033[32m+\033[0;0m')
    print('\033[1m» IP:\033[0;0m',ip[1])
    print('\033[1m» Sigla país:\033[0;0m',cs[1])
    print('\033[1m» País:\033[0;0m',cl[1])
    print('\033[1m» Região:\033[0;0m',reg[1])
    print('\033[1m» Cidade:\033[0;0m',city[1])
    print('\033[1m» Latitude:\033[0;0m',ltd[0])
    print('\033[1m» Longitude:\033[0;0m',lgd[0])
    if cp[1] == 'timezone':
        print('\033[1m» Código postal:\033[0;0m Não encontrado.')
    else:
        print('\033[1m» Código postal:\033[0;0m',cp[1])
    print('\033[1m» Fuso horário:\033[0;0m',fh[1])
    print('\033[1m» Google Maps:\033[0;0m https://www.google.com.br/maps/place/'+ltd[0]+','+lgd[0])
    print('\033[32m+\033[0;1m------------------------------\033[32m+\033[0;0m')
