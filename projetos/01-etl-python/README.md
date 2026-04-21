# 🚀 Explorando IA Generativa em um projeto de pipeline de ETL com Python

## 📌 Visão Geral
Este projeto implementa um pipeline de ETL (Extract, Transform, Load) em Python para coleta, tratamento e enriquecimento de dados cambiais utilizando a API Frankfurter.

Além disso, o projeto explora o uso de **IA Generativa como apoio no desenvolvimento**, auxiliando na construção da arquitetura, código e boas práticas de engenharia de dados.

---

## 🎯 Objetivo
- Consumir dados reais de câmbio
- Aplicar transformações analíticas
- Enriquecer dados com metadados de moedas
- Gerar uma base estruturada para análise
- Demonstrar o uso de IA Generativa como acelerador de desenvolvimento

---

## 🤖 Onde a IA Generativa foi utilizada

A IA Generativa foi utilizada como um **copiloto de desenvolvimento**, apoiando nas seguintes etapas:

### 🔹 Arquitetura do Pipeline
- Definição das camadas: extract, transform, load
- Separação de responsabilidades (Clean Architecture)

### 🔹 Desenvolvimento de Código
- Criação das funções de extração com requests
- Implementação das regras de transformação (variação %, média móvel)
- Construção do processo de enriquecimento (join em memória)

### 🔹 Boas Práticas
- Uso de typing para definição de contratos de dados
- Estrutura modular e desacoplada
- Tratamento de erros com `raise_for_status`

### 🔹 Evolução do Projeto
- Identificação de melhorias (agrupamento por moeda)
- Correção de bugs de lógica
- Sugestões de arquitetura mais escalável

👉 A IA não substituiu o desenvolvimento, mas atuou como **acelerador de aprendizado e produtividade**.

---

## 🧱 Arquitetura do Projeto

01-etl-python/
│
├── extract.py     # Extração de dados (API)
├── transform.py   # Regras de negócio e enriquecimento
├── load.py        # Persistência em CSV
├── main.py        # Orquestração do pipeline

---

## 🔄 Fluxo do Pipeline

### 🔹 1. Extract
Responsável por consumir dados da API Frankfurter:

- Taxas de câmbio
- Metadados das moedas

Endpoints utilizados:
- /v2/rates
- /v2/currencies

---

### 🔹 2. Transform
Camada responsável por aplicar regras de negócio:

#### 📊 Processamentos realizados:
- Agrupamento por moeda
- Ordenação temporal
- Cálculo de variação percentual (%)
- Cálculo de média móvel (7 dias)

#### 🔗 Enriquecimento de dados:
- Nome da moeda (currency_name)
- Símbolo da moeda (symbol)
- Nome da moeda base (base_name)
- Símbolo da moeda base (base_symbol)

👉 Implementa um join em memória entre:
- dados transacionais (taxas)
- dados de referência (moedas)

---

### 🔹 3. Load
Responsável por salvar os dados em CSV:

- Estrutura dinâmica
- Encoding UTF-8
- Pronto para consumo em BI / Excel

---

## ⚙️ Tecnologias Utilizadas
- Python 3.x
- requests (API)
- csv (persistência)
- typing (tipagem)
- IA Generativa (ChatGPT)

---

## ▶️ Como Executar

git clone <seu-repositorio>
cd 01-etl-python
python main.py

---

## 📊 Exemplo de Saída

| date | base | base_name | currency | currency_name | value | variation |
|------|------|----------|----------|---------------|-------|----------|
| 2026-01-01 | USD | United States Dollar | BRL | Brazilian Real | 5.50 | - |

---

## 🧠 Conceitos Aplicados

- ETL Pipeline
- Data Enrichment
- Clean Architecture
- Separação de responsabilidades
- Processamento de séries temporais
- Uso de IA Generativa no desenvolvimento

---

## 🚀 Possíveis Evoluções

- Persistência em banco (PostgreSQL)
- Agendamento (Airflow / Cron)
- Dashboard (Power BI)
- API para exposição dos dados
- Testes automatizados

---

## 👨‍💻 Autor
Projeto desenvolvido para estudo e portfólio em Engenharia de Dados, explorando o uso de IA Generativa no processo de desenvolvimento.
