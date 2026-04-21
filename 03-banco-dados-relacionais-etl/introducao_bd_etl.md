# 🗄️ Introdução a Banco de Dados Relacionais e ETL

## 📌 Visão Geral
Este módulo apresenta os conceitos fundamentais de bancos de dados (relacionais e NoSQL) e o processo de ETL (Extract, Transform, Load) utilizando Python. Esses conhecimentos são essenciais para armazenamento, processamento e integração de dados.

---

## 🧱 Introdução a Banco de Dados Relacionais

Bancos relacionais organizam dados em **tabelas** com relações entre si.

### Conceitos principais:
- **Tabela**: estrutura de dados em linhas e colunas
- **Chave primária (PK)**: identifica unicamente um registro
- **Chave estrangeira (FK)**: cria relacionamento entre tabelas
- **SQL**: linguagem para manipulação de dados

### Operações básicas:
```sql
SELECT * FROM clientes;
INSERT INTO clientes (nome) VALUES ('Alex');
UPDATE clientes SET nome = 'João' WHERE id = 1;
DELETE FROM clientes WHERE id = 1;
```

### Vantagens:
- Integridade dos dados
- Consistência
- Estrutura bem definida

---

## 🌐 Introdução a Banco de Dados NoSQL

Bancos NoSQL são flexíveis e não utilizam modelo relacional tradicional.

### Tipos comuns:
- **Documento** (MongoDB)
- **Chave-valor** (Redis)
- **Colunar** (Cassandra)
- **Grafos** (Neo4j)

### Características:
- Alta escalabilidade
- Estrutura flexível (schema-less)
- Ideal para grandes volumes de dados

### Exemplo (documento JSON):
```json
{
  "nome": "Alex",
  "idade": 33
}
```

---

## 🔄 Fundamentos de ETL (Extract, Transform, Load) com Python

ETL é o processo de integração de dados entre sistemas.

### Etapas:

#### 1. Extract (Extração)
Coleta dados de fontes:
- APIs
- Arquivos (CSV, Excel)
- Bancos de dados

```python
import pandas as pd
df = pd.read_csv("dados.csv")
```

#### 2. Transform (Transformação)
Limpeza e tratamento dos dados:
- Remover duplicidades
- Ajustar formatos
- Criar novas colunas

```python
df = df.dropna()
df["total"] = df["quantidade"] * df["preco"]
```

#### 3. Load (Carga)
Inserção dos dados em destino:
- Banco de dados
- Data warehouse

```python
from sqlalchemy import create_engine
engine = create_engine("sqlite:///banco.db")
df.to_sql("tabela", engine, if_exists="replace")
```

---

## 🎯 Conclusão

Este módulo permite:
- Entender estruturas de bancos relacionais e NoSQL
- Diferenciar cenários de uso
- Implementar pipelines básicos de ETL com Python

Esses conceitos são fundamentais para projetos de engenharia de dados e análise.

---
