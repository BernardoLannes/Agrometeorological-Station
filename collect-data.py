import serial
import csv
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading

# Configura a comunicação serial
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

# Função para abrir um novo arquivo CSV com a data atual
def abrir_csv():
    current_day = time.strftime('%Y-%m-%d')
    csv_file = open('csv-files/' + current_day + '.csv', mode='a', newline='')
    csv_writer = csv.writer(csv_file)
    if csv_file.tell() == 0:  # Escreve cabeçalho se o arquivo estiver vazio
        csv_writer.writerow(['Data', 'Hora', 'Valor_LDR', 'Valor_Umidade'])
    return csv_file, csv_writer

# Inicializa o arquivo CSV
csv_file, csv_writer = abrir_csv()

# Listas para dados do gráfico
tempos, valores_ldr, valores_umid = [], [], []

# Carrega dados existentes do CSV
with open('csv-files/' + time.strftime('%Y-%m-%d') + '.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader, None)  # Pula cabeçalho
    for row in reader:
        data, hora, ldr_value, umid_value = row
        timestamp = time.mktime(time.strptime(f"{data} {hora}", '%Y-%m-%d %H:%M:%S'))
        tempos.append(timestamp)
        valores_ldr.append(int(ldr_value))
        valores_umid.append(int(umid_value))

ultimo_tempo = time.time()

# Função para atualizar os gráficos
def update(frame):
    if mostrar_graficos:
        ax1.cla()
        ax2.cla()
        ax1.plot(tempos[-500:], valores_ldr[-500:], label='Valor LDR')
        ax2.plot(tempos[-500:], valores_umid[-500:], label='Valor Umidade', color='orange')
        ax1.set_title('Gráfico LDR')
        ax2.set_title('Gráfico Umidade')
        ax1.legend(), ax2.legend()

# Função para exibir o menu
def menu():
    escolha = input("Abrir gráficos (1) ou atualizar CSV (2)? \nDigite 1 ou 2: ")
    return escolha == '1'

# Escolha do usuário
mostrar_graficos = menu()

# Função para coletar dados do Arduino e armazená-los no CSV
def coletar_dados():
    global ultimo_tempo, csv_file, csv_writer
    while True:
        try:
            data = arduino.readline().decode('utf-8').strip().split(", ")
            if len(data) == 2:  # Verifica se há dois valores (LDR e umidade)
                ldr_value, umid_value = map(int, data)

                # Verifica se a data mudou
                current_day = time.strftime('%Y-%m-%d')
                if current_day != csv_file.name[:-4]:  # Compara com o nome do arquivo atual
                    csv_file.close()  # Fecha o arquivo atual
                    csv_file, csv_writer = abrir_csv()  # Abre um novo arquivo

                # Armazena a data e hora
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                data_row = [current_time.split()[0], current_time.split()[1], ldr_value, umid_value]
                csv_writer.writerow(data_row)
                csv_file.flush()  # Garante que os dados sejam gravados

                # Atualiza os dados do gráfico
                tempo_atual = time.time()
                if tempo_atual - ultimo_tempo > 11:
                    tempos.extend([None, None])
                    valores_ldr.extend([None, None])
                    valores_umid.extend([None, None])

                tempos.append(tempo_atual)
                valores_ldr.append(ldr_value)
                valores_umid.append(umid_value)
                ultimo_tempo = tempo_atual

        except Exception as e:
            print(f"Erro na coleta de dados: {e}")
            break

# Thread para coletar dados
thread_dados = threading.Thread(target=coletar_dados, daemon=True)
thread_dados.start()
print("Atualizando o arquivo CSV em segundo plano...")

if mostrar_graficos:
    # Configura os gráficos
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    ani1 = FuncAnimation(fig1, update, interval=10000, cache_frame_data=False)
    ani2 = FuncAnimation(fig2, update, interval=10000, cache_frame_data=False)

    # Mostra os gráficos
    plt.show()

try:
    # Mantém o programa em execução enquanto coleta dados
    input("Aperte enter para encerrar o programa.\n")
    csv_file.close()
    arduino.close()

except KeyboardInterrupt:
    print("Forçando encerramento do programa...")
    csv_file.close()
    arduino.close()
