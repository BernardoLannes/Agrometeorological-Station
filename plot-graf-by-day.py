import csv
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Função para obter o nome do arquivo com base na escolha do usuário
def obter_nome_arquivo():
    escolha = input("Deseja abrir o arquivo do dia atual (1) ou de outra data (2)? \nDigite 1 ou 2: ")
    if escolha == '1':
        return 'csv-files/' + time.strftime('%Y-%m-%d') + '.csv'
    elif escolha == '2':
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
valores_temp = []
valores_umid_ar = []
valores_chuva = []
valores_pressao = []
valores_altitude = []

def converter_para_porcentagem(valor):
    return (valor / 1023) * 100

# Carrega os dados existentes do arquivo CSV
try:
    with open(nome_arquivo, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        ultimo_tempo = None
        for row in reader:
            data, hora, ldr_value, umid_value, temp_value, umid_ar_value, chuva_value, pressao_value, altitude_value = row
            timestamp = datetime.strptime(data + ' ' + hora, '%Y-%m-%d %H:%M:%S')

            # Verifica se há uma lacuna maior que 10 segundos
            if ultimo_tempo and (timestamp - ultimo_tempo).total_seconds() > 11:
                tempos.append(None)
                valores_ldr.append(None)
                valores_umid.append(None)
                valores_temp.append(None)
                valores_umid_ar.append(None)
                valores_chuva.append(None)
                valores_pressao.append(None)
                valores_altitude.append(None)

            tempos.append(timestamp)
            valores_ldr.append(float(ldr_value))
            valores_umid.append(converter_para_porcentagem(float(umid_value)))
            valores_temp.append(float(temp_value))
            valores_umid_ar.append(float(umid_ar_value))
            valores_chuva.append(float(chuva_value))
            valores_pressao.append(float(pressao_value))
            valores_altitude.append(float(altitude_value))

            ultimo_tempo = timestamp
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    exit()

# Configura os gráficos
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
fig6, ax6 = plt.subplots()
fig7, ax7 = plt.subplots()

# Formatação do eixo X para mostrar horas e minutos
def formatar_eixo_x(ax):
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.xaxis.set_minor_locator(mdates.MinuteLocator(interval=15))

# Formatação do eixo X em todos os gráficos
formatar_eixo_x(ax1)
formatar_eixo_x(ax2)
formatar_eixo_x(ax3)
formatar_eixo_x(ax4)
formatar_eixo_x(ax5)
formatar_eixo_x(ax6)
formatar_eixo_x(ax7)

# Plotando os dados em cada gráfico
ax1.plot(tempos, valores_ldr, label='Valor LDR')
ax1.set_xlabel('Hora')
ax1.set_ylabel('Intensidade de Luz (LDR)')
ax1.set_title('Gráfico - LDR')
ax1.legend()

ax2.plot(tempos, valores_umid, label='Umidade do Solo', color='orange')
ax2.set_xlabel('Hora')
ax2.set_ylabel('Umidade (%)')
ax2.set_title('Gráfico - Umidade do Solo')
ax2.legend()

ax3.plot(tempos, valores_temp, label='Temperatura', color='red')
ax3.set_xlabel('Hora')
ax3.set_ylabel('Temperatura (°C)')
ax3.set_title('Gráfico - Temperatura')
ax3.legend()

ax4.plot(tempos, valores_umid_ar, label='Umidade do Ar', color='green')
ax4.set_xlabel('Hora')
ax4.set_ylabel('Umidade do Ar (%)')
ax4.set_title('Gráfico - Umidade do Ar')
ax4.legend()

ax5.plot(tempos, valores_chuva, label='Chuva', color='blue')
ax5.set_xlabel('Hora')
ax5.set_ylabel('Chuva (mm)')
ax5.set_title('Gráfico - Chuva')
ax5.legend()

ax6.plot(tempos, valores_pressao, label='Pressão Atmosférica', color='gray')
ax6.set_xlabel('Hora')
ax6.set_ylabel('Pressão (hPa)')
ax6.set_title('Gráfico - Pressão Atmosférica')
ax6.legend()

ax7.plot(tempos, valores_altitude, label='Altitude', color='yellow')
ax7.set_xlabel('Hora')
ax7.set_ylabel('Altitude (m)')
ax7.set_title('Gráfico - Altitude')
ax7.legend()

# Ajusta a formatação do eixo X
fig1.autofmt_xdate()
fig2.autofmt_xdate()
fig3.autofmt_xdate()
fig4.autofmt_xdate()
fig5.autofmt_xdate()
fig6.autofmt_xdate()
fig7.autofmt_xdate()

# Mostra os gráficos
plt.show()
