import csv
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Função para obter o nome do arquivo com base na escolha do usuário
def obter_nome_arquivo():
    escolha = input("Deseja abrir o arquivo do dia atual (1) ou de outra data (2)? \nDigite 1 ou 2: ")

    if escolha == '1':
        # Usa a data atual
        return 'csv-files/' + time.strftime('%Y-%m-%d') + '.csv'
    elif escolha == '2':
        # Solicita a data ao usuário
        data_escolhida = input("Digite a data no formato YYYY-MM-DD: ")
        return 'csv-files/' + data_escolhida + '.csv'
    else:
        print("Escolha inválida! Tente novamente.")
        return obter_nome_arquivo()

# Obter o nome do arquivo CSV
nome_arquivo = obter_nome_arquivo()

# Listas para armazenar os dados para os gráficos
tempos = []
valores_ldr = []
valores_umid = []

def converter_para_porcentagem(valor):
    porcentagem = (valor / 1023) * 100
    return porcentagem

# Carrega os dados existentes do arquivo CSV
try:
    with open(nome_arquivo, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        ultimo_tempo = None
        for row in reader:
            data, hora, ldr_value, umid_value = row
            timestamp = datetime.strptime(data + ' ' + hora, '%Y-%m-%d %H:%M:%S')
            
            # Verifica se há uma lacuna maior que 10 segundos
            if ultimo_tempo and (timestamp - ultimo_tempo).total_seconds() > 11:
                tempos.append(None)
                valores_ldr.append(None)
                valores_umid.append(None)
            
            tempos.append(timestamp)
            valores_ldr.append(int(ldr_value))
            valores_umid.append(converter_para_porcentagem(int(umid_value)))
            ultimo_tempo = timestamp
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    exit()

# Filtra os valores None antes de calcular o mínimo e o máximo
valores_ldr_filtrados = [v for v in valores_ldr if v is not None]
valores_umid_filtrados = [v for v in valores_umid if v is not None]

# Configura os gráficos
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# Formatação do eixo X para mostrar horas e minutos
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax1.xaxis.set_minor_locator(mdates.MinuteLocator(interval=15))

ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax2.xaxis.set_major_locator(mdates.HourLocator(interval=1))
ax2.xaxis.set_minor_locator(mdates.MinuteLocator(interval=15))

# Plota os dados no gráfico do LDR
ax1.plot(tempos, valores_ldr, label='Valor LDR')
ax1.set_xlabel('Hora')
ax1.set_ylabel('Intensidade de Luz (LDR)')
ax1.set_title('Gráfico - LDR')
ax1.legend()

# Plota os dados no gráfico de umidade
ax2.plot(tempos, valores_umid, label='Valor Umidade', color='orange')
ax2.set_xlabel('Hora')
ax2.set_ylabel('Umidade (Definir Unidade)')
ax2.set_title('Gráfico - Umidade')
ax2.legend()

# Ajusta a diferença mínima no eixo Y para 400 unidades
ldr_min = min(valores_ldr_filtrados)
ldr_max = max(valores_ldr_filtrados)
if ldr_max - ldr_min < 400:
    ax1.set_ylim(ldr_min, ldr_min + 400)

ax2.set_ylim(0, 100)

# Ajusta a formatação do eixo X
fig1.autofmt_xdate()
fig2.autofmt_xdate()

# Mostra os gráficos
plt.show()
