#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Codado por: Lucas Simoni <lucas.simoni10@gmail.com>
#
# Programa com finalidade de aprendizado.
# Todas as suas ações utilizando o everyuse são responsabilidades SUA.
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

def envio(remetente, senha, de, destinatario, assunto, corpo, servidor, porta, anexo, tipoanexo, nomearq, quantidade):

    msg = MIMEMultipart()
    msg['From'] = de
    msg['Subject'] = assunto
    texto = MIMEText(corpo, 'plain')
    msg.attach(texto)

    #Se o tipo de anexo for uma imagem
    if tipoanexo == 1:
        aa = open(anexo, 'rb')
        img = MIMEImage(aa.read())
        img.add_header('Content-Disposition', 'attachment; filename="%s"' % nomearq)
        aa.close()

    #Se o tipo de anexo for um audio
    elif tipoanexo == 2:
        aa = open(anexo, 'rb')
        if anexo.lower().endswith('.mp3'):
            mp3 = MIMEAudio(aa.read(), 'mp3')
            print(' Anexando', anexo, 'ao email.')
            mp3.add_header('Content-Disposition', 'attachment; filename="%s"' % nomearq + '.mp3')
            msg.attach(mp3)
        elif anexo.lower().endswith('.ogg'):
            ogg = MIMEAudio(aa.read(), 'ogg')
            print(' Anexando', anexo, 'ao email.')
            ogg.add_header('Content-Disposition', 'attachment; filename="%s"' % nomearq + '.ogg')
            msg.attach(ogg)
        else:
            print(' Formato de anexo inválido!')
        aa.close()

    #Se o tipo de anexo for um documento
    elif tipoanexo == 3:
        aa = open(anexo, 'rb')
        if anexo.lower().endswith('.pdf'):
            lerdoc = aa.read()
            doc = MIMEBase('application', 'pdf')
            doc.set_payload(lerdoc)
            encoders.encode_base64(doc)
            print(' Anexando', anexo, 'ao email.')
            doc.add_header('Content-Disposition', 'attachment; filename="%s"' % nomearq + '.pdf')
            msg.attach(doc)
        elif anexo.lower().endswith('.docx'):
            lerdoc = aa.read()
            doc = MIMEBase('application', 'docx')
            doc.set_payload(lerdoc)
            encoders.encode_base64(doc)
            print(' Anexando', anexo, 'ao email.')
            doc.add_header('Content-Disposition', 'attachment; filename="%s"' % nomearq + '.docx')
            msg.attach(doc)
        aa.close()
    else:
        tipoanexo = 0

    server = smtplib.SMTP(servidor, porta)
    server.starttls()
    server.login(remetente,senha)
    rng = range(0, quantidade)
    for i in rng:
        server.sendmail(remetente, destinatario, str(msg))
        qt = i+1
        print(' \033[1m➤\033[32m'+str(qt) + 'º email enviado...\033[0;0m')
    server.quit()