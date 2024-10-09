#include <DHT.h>    // Para sensor de temperatura do ar e umidade
#include <DHT_U.h>  // Para sensor de temperatura do ar e umidade

#include <Wire.h>             // Para sensor de pressão atmosferica
#include <Adafruit_BMP085.h>  // Para sensor de pressão atmosferica

// Definição dos Pinos:
const int ldrPin = A0;   // Pino onde o LDR está conectado
const int umidPin = A1;  // Pino onde o Sensor de Umidade do solo está conectado
const int div_tens = 2;  // Pino que fornecerá 5v para as medições apenas quando necessário
const int dhtPin = 3;    // Pino onde o sensor de temperatura e umidade do ar está conectado
const int chuvaPin = A2; // Pino onde o sensor de chuva está conectado

DHT dht(dhtPin, DHT11);
Adafruit_BMP085 bmp;

//Definição dos tempos de operação
#define delay_sensores 200
#define delay_leitura 1000 // Defina o tempo desejado entre as leituras, a diferença será feita automaticamete

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial
  dht.begin();
  bmp.begin();

  // Configuração dos Pinos do Arduino:
  pinMode(ldrPin, INPUT);
  pinMode(umidPin, INPUT);
  pinMode(div_tens, OUTPUT);
}

void loop() {
  // Setup dos Sensores:
  digitalWrite(div_tens, HIGH); // Liga os sensores e divisor de tensão
  delay(delay_sensores); // Evita qualquer demora de incialização

  // Leitura dos Dados:
  int ldrValue = analogRead(ldrPin);
  int umidValue = analogRead(umidPin);
  float dhtTemp = dht.readTemperature();
  int dhtUmid = dht.readHumidity();
  int chuvaValue = analogRead(chuvaPin);
  float bmpTemp = bmp.readTemperature();
  float bmpPress = bmp.readPressure();
  int bmpAlt = bmp.readAltitude();
  
  // Interpretação dos Dados:
  umidValue = map(umidValue, 0, 1023, 1023, 0); // Inverte o lógico do sensor de umidade
  chuvaValue = map(chuvaValue, 0, 1023, 1023, 0); // Inverte o lógico do sensor de chuva
  float tempMed = (dhtTemp + bmpTemp) / 2;

  // Envio dos Dados pela Serial:
  Serial.print(ldrValue);
  Serial.print(", ");
  Serial.print(umidValue);
  Serial.print(", ");
  Serial.print(tempMed);
  Serial.print(", ");
  Serial.print(dhtUmid);
  Serial.print(", ");
  Serial.print(chuvaValue);
  Serial.print(", ");
  Serial.print(bmpPress);
  Serial.print(", ");
  Serial.println(bmpAlt);

  // Finalização do Ciclo
  digitalWrite(div_tens, LOW); // Desliga os sensores e divisor de tensão
  delay(delay_leitura - delay_sensores); // Aguarda antes de ler novamente
}
