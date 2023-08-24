import datetime
import time
import logging


def time_conversion(segundos):
    if segundos < 60:
        return f"{segundos} segundos"
    elif segundos < 3600:
        minutos = segundos // 60
        return f"{minutos} minutos"
    else:
        horas = segundos // 3600
        minutos = (segundos % 3600) // 60
        return f"{horas} horas e {minutos} minutos"


def agendar_verificacao_ate_as_sete(horario_atual):
    # Definir o horário alvo para as 7 horas da manhã
    horario_alvo = horario_atual.replace(hour=7, minute=0, second=0, microsecond=0)
    
    # Se o horário atual já for 7 horas ou posterior, aguardar até o próximo dia
    if horario_atual >= horario_alvo:
        horario_alvo += datetime.timedelta(days=1)
    
    # Calcular o tempo de espera até as 7 horas da manhã
    tempo_de_espera = (horario_alvo - horario_atual).total_seconds()
    logging.info("tempo_de_espera: " + str(time_conversion(tempo_de_espera)))
    # Esperar até as 7 horas da manhã
    time.sleep(tempo_de_espera)
    logging.info("Voltando a contabilizar")
    return True