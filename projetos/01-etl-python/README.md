# 🚀 Explorando IA Generativa em um projeto de Engenharia de Software com Python

## 📌 Visão Geral
Este projeto implementa um **serviço backend em Python** responsável pela ingestão, processamento e enriquecimento de dados cambiais a partir de APIs externas.

A solução foi estruturada utilizando princípios de **Engenharia de Software**, com foco em:
- arquitetura desacoplada
- separação de responsabilidades
- integração com APIs REST
- processamento de dados orientado a regras de negócio

Além disso, o projeto explora o uso de **IA Generativa como apoio no desenvolvimento**, atuando como acelerador na construção da solução.

---

## 🎯 Objetivo
- Consumir dados reais via API REST
- Implementar regras de negócio para processamento de dados
- Enriquecer dados com informações externas
- Construir uma aplicação modular e escalável
- Demonstrar o uso de IA Generativa no ciclo de desenvolvimento

---

## 🤖 Uso de IA Generativa no Projeto

A IA Generativa foi utilizada como um **copiloto de desenvolvimento**, apoiando:

### 🔹 Arquitetura de Software
- Definição da arquitetura em camadas (extract, transform, load)
- Aplicação de princípios de separação de responsabilidades

### 🔹 Implementação Backend
- Desenvolvimento de integrações com APIs REST (requests)
- Estruturação de funções reutilizáveis
- Modelagem de fluxo de dados entre camadas

### 🔹 Qualidade de Código
- Uso de typing para definição de contratos
- Padronização de estrutura de código
- Tratamento de erros com `raise_for_status`

### 🔹 Evolução Técnica
- Refatoração para suportar múltiplas moedas
- Correção de bugs de lógica
- Sugestões de melhorias arquiteturais

👉 A IA foi utilizada como ferramenta de apoio, mantendo o controle técnico das decisões no desenvolvimento.

---

## 🧱 Arquitetura do Projeto

01-etl-python/
│
├── extract.py     # Integração com APIs externas
├── transform.py   # Regras de negócio e processamento
├── load.py        # Persistência de dados
├── main.py        # Orquestração da aplicação

---

## 🔄 Fluxo da Aplicação

### 🔹 1. Extract (Integração)
Responsável por consumir APIs externas:

- Taxas de câmbio
- Metadados das moedas

Endpoints utilizados:
- /v2/rates
- /v2/currencies

---

### 🔹 2. Transform (Regra de Negócio)

Camada responsável pelo processamento dos dados:

#### 📊 Processamentos:
- Agrupamento por entidade (moeda)
- Ordenação temporal
- Cálculo de variação percentual (%)
- Cálculo de média móvel (7 dias)

#### 🔗 Enriquecimento:
- Nome da moeda (currency_name)
- Símbolo da moeda (symbol)
- Nome da moeda base (base_name)
- Símbolo da moeda base (base_symbol)

👉 Implementação de **join em memória** entre dados transacionais e dados de referência.

---

### 🔹 3. Load (Persistência)

Responsável por exportar os dados:

- Geração de arquivo CSV
- Estrutura dinâmica
- Compatível com ferramentas analíticas (Excel, BI)

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- requests (integração com APIs)
- csv (persistência)
- typing (contratos de dados)
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

- Engenharia de Software aplicada a dados
- Arquitetura em camadas
- Integração com APIs REST
- Processamento de séries temporais
- Data Enrichment
- Separação de responsabilidades
- Uso de IA Generativa no desenvolvimento

---

## 🚀 Possíveis Evoluções

- Exposição via API (FastAPI)
- Persistência em banco de dados (PostgreSQL)
- Containerização com Docker
- Implementação de testes automatizados (pytest)
- Logging estruturado
- Orquestração (Airflow)

---

## 👨‍💻 Autor

Alex Carlos de Sousa  
Engenharia de Software | Backend | Integrações | Automação  

Projeto desenvolvido para estudo e portfólio, com foco em aplicação de conceitos de Engenharia de Software e uso de IA Generativa no processo de desenvolvimento.
