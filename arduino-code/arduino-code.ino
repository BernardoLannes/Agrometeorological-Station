//Definição dos tempos de operação
#define delay_sensores 200
#define delay_leitura 10000 // Defina o tempo desejado entre as leituras, a diferença será feita automaticamete

const int ldrPin = A0; // Pino onde o LDR está conectado
const int umidPin = A1; // Pino onde o Sensor de Umidade está conectado
const int div_tens = 2; // Pino que fornecerá 5v para as medições apenas quando necessário


void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial

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
  int ldrValue = analogRead(ldrPin); // Lê o valor do LDR
  int umidValue = analogRead(umidPin); // Lê o valor da umidade

  // Interpretação dos Dados:
  umidValue = map(umidValue, 0, 1023, 1023, 0); // Inverte o lógico do sensor de umidade
  
  // Envio dos Dados pela Serial:
  Serial.print(ldrValue);
  Serial.print(", ");
  Serial.println(umidValue);

  // Finalização do Ciclo
  digitalWrite(div_tens, LOW); // Desliga os sensores e divisor de tensão
  delay(delay_leitura - delay_sensores); // Aguarda antes de ler novamente
}
