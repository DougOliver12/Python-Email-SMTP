"""
Envio de email simples utilizando o protocolo SMTP por Douglas Magalhães de Oliveira

PASSO A PASSO DAS TAREFAS A SEREM EXECUTADAS:

Criar um objeto SMTP para conexão com o servidor.
Realizar o login na sua conta.
Definir o cabeçalho da sua mensagem e as suas credenciais para a realização do login.
Criar um objeto MIMEMultipart e associar a ele o cabeçalho relevante - exemplo: De:, Para:, e Assunto.
Associar uma mensagem ao objeto de mensagem MIMEMultipart.
Finalmente, enviar a mensagem.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# create message object instance
msg = MIMEMultipart()
message = input("Digite sua mensagem:\n")
# setup the parameters of the message
password = "senha email "
msg['From'] = "email remetente"
msg['To'] = "email destinatario"
msg['Subject'] = "Teste envio smtp"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.mail.yahoo.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("Email enviado para %s:" % (msg['To']))



