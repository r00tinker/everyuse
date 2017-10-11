#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.
import os

cminst = '\033[1m\033[33meveryuse\033[0;0m» '
if os.getuid() != 0:
    print(cminst+'Erro!')
    print(cminst+'Execute como administrador.')
    exit(0)

if os.path.exists('/usr/bin/everyuse'):
    print(cminst+'Você já possui o everyuse!\n Tente executar: sudo everyuse')
else:
    yorn = input(cminst+'Deseja fazer a instalação do programa? [S/n] ')
    if yorn.lower() == 's' or yorn.lower() != 's' and yorn.lower() != 'n':
        print(cminst+'Executando a instalação...')
        if os.path.exists('everyuse.py') and os.path.exists('modulos/'):
            try:
                print(cminst+'Deseja mover o programa para poder utilizar ele com apenas o comando:')
                print('    sudo everyuse')
                desejamover = input(cminst+'? [S/n]')
                if desejamover.lower() == 's' or desejamover.lower() != 's' and desejamover.lower() != 'n':
                    os.system('sudo mv everyuse.py /usr/bin/everyuse')
                    os.system('sudo chmod +x /usr/bin/everyuse')
                    os.system('sudo mv modulos/ /usr/bin/modulos')
                    print(' [*] Arquivos movido com sucesso para /usr/bin/')
                    print(' [*] Para executar, digite: sudo everyuse')
                elif desejamover.lower() == 'n':
                    os.system('sudo mv everyuse.py everyuse')
                    print(' [*] Arquivo renomeado para everyuse')
            except:
                print('Algum erro aconteceu!\n Tente usar o comando: git clone https://github.com/r00tinker/everyuse')

print(cminst+'Fazendo update...')
os.system('sudo apt-get update > /dev/null')
print(cminst+'Instalando módulos...')
os.system('sudo apt-get install python3-bs4 > /dev/null')
os.system('sudo apt-get install python3-requests > /dev/null')
print(cminst+'Instalação de módulos finalizadas...')
