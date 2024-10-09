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
        csv_writer.writerow(['Data', 'Hora', 'Incidencia_Luz', 'Umidade_Solo', 'Temperatura', 'Umidade_Ar', 'Chuva', 'Pressao_Atmosferica', 'Altitude'])
    return csv_file, csv_writer

# Inicializa o arquivo CSV
csv_file, csv_writer = abrir_csv()

# Listas para dados do gráfico
tempos, valores_ldr, umid_solo, temperatura, umid_ar, chuva, press_atm, altitude = [], [], [], [], [], [], [], []

# Carrega dados existentes do CSV
with open('csv-files/' + time.strftime('%Y-%m-%d') + '.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader, None)  # Pula cabeçalho
    for row in reader:
        data, hora, val_ldr, um_solo, temp, um_ar, chv, pres_atm, alt = row
        timestamp = time.mktime(time.strptime(f"{data} {hora}", '%Y-%m-%d %H:%M:%S'))
        tempos.append(timestamp)
        valores_ldr.append(float(val_ldr))
        umid_solo.append(float(um_solo))
        temperatura.append(float(temp))
        umid_ar.append(float(um_ar))
        chuva.append(float(chv))
        press_atm.append(float(pres_atm))
        altitude.append(float(alt))

ultimo_tempo = time.time()

# Função para coletar dados do Arduino e armazená-los no CSV
def coletar_dados():
    global ultimo_tempo, csv_file, csv_writer
    while True:
        try:
            data = arduino.readline().decode('utf-8').strip().split(", ")
            if len(data) == 7:  # Verifica se há sete valores
                val_ldr, um_solo, temp, um_ar, chv, pres_atm, alt = map(float, data)

                # Verifica se a data mudou
                current_day = time.strftime('%Y-%m-%d')
                if current_day != csv_file.name[-14:-4]:  # Compara com o nome do arquivo atual
                    csv_file.close()  # Fecha o arquivo atual
                    csv_file, csv_writer = abrir_csv()  # Abre um novo arquivo

                # Armazena a data e hora
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                data_row = [current_time.split()[0], current_time.split()[1], val_ldr, um_solo, temp, um_ar, chv, pres_atm, alt]
                csv_writer.writerow(data_row)
                csv_file.flush()  # Garante que os dados sejam gravados

                # Atualiza os dados do gráfico
                tempo_atual = time.time()
                tempos.append(tempo_atual)
                valores_ldr.append(val_ldr)
                umid_solo.append(um_solo)
                temperatura.append(temp)
                umid_ar.append(um_ar)
                chuva.append(chv)
                press_atm.append(pres_atm)
                altitude.append(alt)

                ultimo_tempo = tempo_atual

        except Exception as e:
            print(f"Erro na coleta de dados: {e}")
            break

# Thread para coletar dados
thread_dados = threading.Thread(target=coletar_dados, daemon=True)
thread_dados.start()
print("Atualizando o arquivo CSV em segundo plano...")

try:
    # Mantém o programa em execução enquanto coleta dados
    input("Aperte enter para encerrar o programa.\n")
    csv_file.close()
    arduino.close()

except KeyboardInterrupt:
    print("Forçando encerramento do programa...")
    csv_file.close()
    arduino.close()
