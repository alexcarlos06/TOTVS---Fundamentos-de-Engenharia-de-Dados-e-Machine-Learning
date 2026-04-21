# 📊 Introdução à Ciência de Dados e Python

## 📌 Visão Geral
Este módulo apresenta os fundamentos da linguagem Python aplicados à Ciência de Dados, abordando estruturas básicas, manipulação de dados e organização de código. Esses conceitos são essenciais para análise, automação e construção de soluções mais avançadas.

---

## 🔢 Tipos de Operadores em Python

Os operadores permitem realizar operações com variáveis e valores.

### Tipos principais:
- **Aritméticos**: +, -, *, /, //, %, **
- **Comparação**: ==, !=, >, <, >=, <=
- **Lógicos**: and, or, not
- **Atribuição**: =, +=, -=, *=, etc.

### Exemplo:
```python
a = 10
b = 5
resultado = (a + b) > 10 and b < a
```

---

## 🔁 Estruturas Condicionais e de Repetição

Controlam o fluxo de execução do código.

### Condicionais:
- if, elif, else

```python
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### Repetição:
- for: iteração controlada
- while: repetição com condição

```python
for i in range(5):
    print(i)

while contador < 5:
    contador += 1
```

---

## 🔤 Manipulação de Strings

Strings são usadas para trabalhar com textos.

### Operações comuns:
- Concatenação: "Olá" + " Mundo"
- Repetição: "A" * 3
- Métodos úteis:
  - .upper(), .lower()
  - .strip()
  - .replace()
  - .split()

```python
texto = "  Python é poderoso  "
print(texto.strip().upper())
```

---

## 📋 Trabalhando com Listas

Listas armazenam coleções ordenadas e mutáveis.

### Características:
- Permitem duplicados
- Podem ser alteradas

### Operações:
- append(), remove(), pop(), sort()

```python
lista = [1, 2, 3]
lista.append(4)
```

---

## 📦 Conhecendo Tuplas

Tuplas são semelhantes às listas, porém imutáveis.

### Características:
- Não podem ser alteradas após criação
- Mais seguras e performáticas em alguns casos

```python
tupla = (1, 2, 3)
```

---

## 🔗 Explorando Conjuntos (Set)

Conjuntos armazenam elementos únicos e não ordenados.

### Características:
- Não permitem duplicidade
- Suportam operações matemáticas

### Operações:
- União: |
- Interseção: &
- Diferença: -

```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # {3}
```

---

## 🗂️ Dicionários em Python

Estrutura de dados baseada em chave-valor.

### Características:
- Mutáveis
- Acesso rápido por chave

```python
pessoa = {
    "nome": "Alex",
    "idade": 33
}
print(pessoa["nome"])
```

---

## ⚙️ Dominando Funções em Python

Funções permitem reutilizar código e organizar lógica.

### Estrutura:
```python
def saudacao(nome):
    return f"Olá, {nome}"
```

### Conceitos importantes:
- Parâmetros e retorno
- Funções anônimas (lambda)
- Escopo de variáveis

---

## 🎯 Conclusão

Este módulo estabelece a base para trabalhar com Python em Ciência de Dados, permitindo:
- Manipular dados de diferentes formatos
- Controlar fluxos de execução
- Criar estruturas reutilizáveis

Esses conceitos são fundamentais para avançar em análise de dados, automação e Machine Learning.
