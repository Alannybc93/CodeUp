# utils.py - Utilitários para o sistema CodeUp

import random
from datetime import datetime, timedelta

def gerar_codigo_convite():
    """Gera código de convite aleatório"""
    caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(caracteres) for _ in range(8))

def calcular_tempo_estudo(tempo_inicio, tempo_fim):
    """Calcula tempo total de estudo em minutos"""
    diferenca = tempo_fim - tempo_inicio
    return int(diferenca.total_seconds() / 60)

def formatar_tempo(minutos):
    """Formata minutos para formato legível"""
    if minutos < 60:
        return f"{minutos}min"
    horas = minutos // 60
    mins = minutos % 60
    if mins == 0:
        return f"{horas}h"
    return f"{horas}h{mins}min"

