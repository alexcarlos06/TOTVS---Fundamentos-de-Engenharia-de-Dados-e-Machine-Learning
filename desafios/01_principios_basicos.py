"""Desafio  Cálculo Inteligente De Descontos Para Pedidos Empresariais
Você faz parte de uma equipe de tecnologia responsável por desenvolver soluções inteligentes para a gestão de negócios em larga escala. Em um dos projetos, sua missão é criar um módulo que automatize o cálculo de descontos em pedidos, tornando o processo mais eficiente e menos sujeito a erros humanos. O sistema recebe o valor total de um pedido e o percentual de desconto a ser aplicado. Sua tarefa é calcular o valor final do pedido após o desconto, garantindo precisão e agilidade para que milhares de empresas possam escalar suas operações sem preocupações.

Implemente um programa que leia dois valores em uma única linha: o valor total do pedido (um número decimal positivo) e o percentual de desconto (um número inteiro entre 0 e 100). O programa deve calcular o valor final do pedido após aplicar o desconto e exibir o resultado com duas casas decimais. Não utilize bibliotecas externas para o cálculo ou formatação.

Entrada
Uma única linha contendo dois valores separados por espaço: o valor total do pedido (decimal positivo) e o percentual de desconto (inteiro entre 0 e 100).

Saída
Uma única linha contendo o valor final do pedido após o desconto, com exatamente duas casas decimais.

Exemplos
A tabela abaixo apresenta exemplos de entrada e saída:

Entrada	    Saída
150.00 10	135.00
200.50 25	150.38
99.99 0	    99.99
80.00 100	0.00

"""
# Lê a linha de entrada e separa os valores
entrada = input().strip().split()
valor_total = float(entrada[0])
percentual_desconto = int(entrada[1])

# TODO: Calcule o valor final do pedido após aplicar o desconto percentual
valor_final = valor_total  - (valor_total * (percentual_desconto /100))

# Imprima o valor final com duas casas decimais
print(f"{valor_final:.2f}")