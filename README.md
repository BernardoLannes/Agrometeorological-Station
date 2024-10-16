## 1. Project Overview

The "Agrometeorological Station" project aims to develop a low-cost system for collecting accurate data related to agrometeorology. Through this, we intend to generate interpretations and create databases that support modeling and scientific studies in various fields, such as climate and agribusiness. The project seeks to democratize access to essential meteorological information for agriculture.

---

## 2. Possibility and Orientation of the Project

The project is made possible and guided by Professor Fábio Gonçalves from the Department of Natural Sciences at Universidade Federal Fluminense (UFF).

---

## 3. System Components

Currently, the circuit includes the following sensors:
- *Light Sensor (LDR)*: Measures light intensity.
- *Rain Sensor*: Detects the amount of precipitation.
- *Soil Moisture Sensor*: Assesses soil moisture.
- *Air Humidity Sensor*: Measures relative humidity in the air.
- *Atmospheric Pressure Sensor*: Monitors air pressure.
- *Altitude Sensor*: Monitors altitude relative to sea level.
- *Temperature Sensor*: Measures ambient temperature.

The system is developed using *Arduino* for sensor control and *Python* for graph generation and analysis.

---

## 4. Data Collection and Processing

Data is collected by sensors connected to the Arduino, which sends it via the serial port. A Python program collects the data in the background, allowing for real-time visualization or continuous collection. The data is saved in CSV files that are not overwritten, generating a new file at midnight.

---

## 5. Current Stage

Currently, the system is being developed to use an SD card module to save the CSV files directly from the Arduino, eliminating the need for an external program.

---

## 6. Future Implementation

The project aims to integrate an *ESP8266* for sending data to an internet server and use an *SD card module* for local data storage. The system will be powered by a battery that will send information about its charge level and emit an alert when it reaches 20%. If necessary, the system may also use a radio module for communication between Arduinos, depending on the implementation location.

---

## 7. Challenges

The main challenges of the project include:
- *Energy Optimization*: Ensuring the system consumes minimal power, especially in rural areas.
- *Resistance to Climatic Conditions*: Protecting circuit components from harsh weather.
- *Sensor Accuracy and Calibration*: Maintaining accurate readings over time.
- *Connectivity and Latency*: Ensuring stable data transmission in areas with limited connectivity.
- *Data Security*: Protecting the integrity of data during transmission.
- *Analog Signal Conversion*: Converting analog signals into conventional measurement units.

---

## 8. Applications

The data and analyses generated by the "Agrometeorological Station" can benefit:
- *Small and Medium Farms*: Providing accessible data for agricultural planning.
- *Environmental Monitoring*: Helping to predict extreme weather events.
- *Scientific Research*: Supporting studies on climate change.
- *Local Weather Forecasting*: Improving forecast accuracy in rural areas.


---

## Versão em Português

---

## 1. Visão Geral do Projeto

O projeto "Estação Agrometeorológica" visa desenvolver um sistema de baixo custo para a coleta de dados precisos relacionados à agrometeorologia. Com isso, pretendemos gerar interpretações e criar bases de dados que suportem modelagens e estudos científicos em várias áreas, como clima e agronegócio. O projeto busca democratizar o acesso a informações meteorológicas essenciais para a agricultura.

---

## 2. Possibilidade e Orientação do Projeto

O projeto é possibilitado e ministrado pelo professor Fábio Gonçalves, do Departamento de Ciências da Natureza da Universidade Federal Fluminense (UFF).

---

## 3. Componentes do Sistema

Atualmente, o circuito inclui os seguintes sensores:
- *Sensor de luminosidade (LDR)*: Mede a intensidade da luz.
- *Sensor de chuva*: Detecta a quantidade de precipitação.
- *Sensor de umidade do solo*: Avalia a umidade presente no solo.
- *Sensor de umidade do ar*: Mede a umidade relativa do ar.
- *Sensor de pressão atmosférica*: Monitora a pressão do ar.
- *Sensor de altitude*: Monitora a altura em relação ao nível do mar.
- *Sensor de temperatura*: Mede a temperatura ambiente.

O sistema é desenvolvido utilizando *Arduino* para controle dos sensores e *Python* para geração de gráficos e análises.

---

## 4. Coleta e Processamento de Dados

Os dados são coletados pelos sensores conectados ao Arduino, que os envia pela porta serial. Um programa em Python coleta os dados em segundo plano, com a possibilidade de visualização em tempo real ou coleta contínua. Os dados são salvos em arquivos CSV que não são sobrescritos, gerando um novo arquivo a cada meia-noite.

---

## 5. Estágio Atual

No presente momento está sendo desenvolvido o uso de um módulo de cartão sd para salvar o arquivo csv pelo arduino, sem precisar de um programa externo.

---

## 6. Implementação Futura

O projeto pretende integrar um *ESP8266* para o envio de dados para um servidor na internet e utilizar um módulo de *cartão SD* para armazenamento local dos dados. O sistema será alimentado por bateria, que enviará informações sobre o nível de carga e emitirá um alerta quando atingir 20%. Caso haja necessidade há a possibilidade de uso de um módulo de rádio para comunicação entre arduinos a depender do local da implementação do circuito.

---

## 7. Desafios

Os principais desafios do projeto incluem:
- *Otimização Energética*: Garantir que o sistema consuma pouca energia, especialmente em áreas rurais.
- *Resistência às Condições Climáticas*: Proteger os componentes do circuito de intempéries.
- *Precisão e Calibração dos Sensores*: Manter a precisão das leituras ao longo do tempo.
- *Conectividade e Latência*: Assegurar a transmissão de dados estável em áreas com conectividade limitada.
- *Segurança dos Dados*: Proteger a integridade dos dados durante a transmissão.
- *Conversão de Sinais Analógicos*: Transformar sinais analógicos em unidades de medida convencionais.

---

## 8. Aplicações

Os dados e análises gerados pela "Estação Agrometeorológica" podem beneficiar:
- *Pequenas e Médias Fazendas*: Fornecendo dados acessíveis para planejamento agrícola.
- *Monitoramento Ambiental*: Ajudando a prever eventos climáticos extremos.
- *Pesquisa Científica*: Suportando estudos sobre mudanças climáticas.
- *Previsão do Tempo Local*: Melhorando a precisão das previsões em áreas rurais.
