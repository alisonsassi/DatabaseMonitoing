import urllib
import urllib.request
import time
from email_sender import send_email
import logging
import datetime
import time
from convert_time import time_conversion, agendar_verificacao_ate_as_sete



# Configurar o sistema de log
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


logging.info("--------------------INICIALIZANDO O SISTEMA ----------------")
send_email("INICIALIZANDO O SISTEMA DE MONITORAMENTO","O sistema de monitoramento da base está inciando.")


base = 'https://srv-dev-tsy03.whebdc.com.br:9115/'

def check_website(url):
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.request.URLError:
        return False

def time_offline():
    offline_start = None

    while True:
        try:
            urllib.request.urlopen(base)
            if offline_start is not None:
                offline_duration = time.time() - offline_start
                logging.info(f"O site {base} ficou offline por {offline_duration:.2f} segundos")
                break
        except urllib.request.URLError:
            if offline_start is None:
                offline_start = time.time()
                # adicionar o método de "ficou fora X tempo"
        time.sleep(6) # 60 - A cada 1 min verifica a base

while True:

    agora = datetime.datetime.now()
    hora_atual = agora.time()

    if agora.hour >= 7 and agora.hour < 18:

        if check_website(base):
           if agora.hour == 8:
               logging.info("BASE ON-LINE")
               
        else:
            logging.critical("CAIU A BASE, VAI PASSAR PELA VERIFICAÇÃO DA INTERNET.")
            if check_website('https://www.google.com/'):
                logging.info("VERIFICA SITE GOOGLE - PASS")
                send_email("CAIU a base Interoperabilidade!","A base da interoperabilidade não está acessível.")
                logging.warning('ENVIOU E-MAIL - CAIU A BASE')
                tempo_inicio = time.time()
                #Método para verificar quanto tempo ficou fora. 
                time_offline()
                tempo_fim = time.time()
                elapsed_time = time_conversion (tempo_fim - tempo_inicio)
                #send_email("VOLTOU a base Interoperabilidade!","A base da interoperabilidade está de volta, ficou off-line: "+ elapsed_time)
                logging.warning("ENVIAR E-MAIL - VOLTOU A BASE , ficou off-line: "+ elapsed_time)
            else:
                logging.info("CAIU INTERNET DO SERVIDOR: SITE GOOGLE OFF-LINE")

    else:
        logging.info("Está fora do horário de trabalho")
        agendar_verificacao_ate_as_sete(datetime.datetime.now())
