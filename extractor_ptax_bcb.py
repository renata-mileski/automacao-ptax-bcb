import pandas as pd
import requests
from datetime import datetime, timedelta

def obter_cotacao_dolar(data):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json&dataInicial={data}&dataFinal={data}"
    print(f"Consultando cotação para: {data}")
    response = requests.get(url)
    try:
        data_json = response.json()
        print(f"Resposta da API: {data_json}")
        if data_json and isinstance(data_json, list):
            return float(data_json[-1]['valor'])
    except (ValueError, IndexError, KeyError) as e:
        print(f"Erro ao obter dados para {data}: {e}")
    return None

def ultimo_dia_util_mes(ano, mes):
    if mes == 12:
        ultimo_dia = datetime(ano + 1, 1, 1) - timedelta(days=1)
    else:
        ultimo_dia = datetime(ano, mes + 1, 1) - timedelta(days=1)
    while ultimo_dia.weekday() > 4:
        ultimo_dia -= timedelta(days=1)
    return ultimo_dia

dados = []
anos = [2023,2024,2025,2026]  # Ajuste conforme necessário
meses = range(1, 13)

# Data atual
hoje = datetime.now()

for ano in anos:
    for mes in meses:
        ultimo_dia = ultimo_dia_util_mes(ano, mes)
        
        # Se a data for no futuro, não tenta buscar
        if ultimo_dia > hoje:
            continue
        
        data_str = ultimo_dia.strftime("%d/%m/%Y")
        cotacao = obter_cotacao_dolar(data_str)
        if cotacao is not None:
            dados.append({'Data': data_str, 'Cotação': cotacao})
        else:
            print(f"Sem dados de cotação para {data_str}.")

df = pd.DataFrame(dados)
df.to_excel('cotacoes_dolar_ptax.xlsx', index=False)
print("Cotação do dólar PTAX salva com sucesso!")