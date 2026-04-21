"""Desafio Cálculo Inteligente De Descontos Para Pedidos Empresariais
Você faz parte de uma equipe de tecnologia responsável por criar soluções inteligentes para a gestão de empresas de diversos setores. Seu time está desenvolvendo um sistema que automatiza decisões simples do dia a dia empresarial, tornando processos mais eficientes e escaláveis. Um dos módulos do sistema precisa analisar rapidamente pedidos de compra e decidir se eles devem ser aprovados, rejeitados ou encaminhados para revisão, com base em regras claras de valor e prioridade. Sua missão é implementar a lógica que tornará esse processo automático, ajudando empresas a economizar tempo e evitar erros humanos.

Implemente um programa que receba como entrada uma string contendo dois valores separados por espaço: o valor do pedido (um número inteiro) e a prioridade do pedido (uma palavra, podendo ser "alta", "media" ou "baixa"). O sistema deve aprovar automaticamente pedidos de valor até 1000 com prioridade "alta" ou "media". Pedidos acima de 1000 com prioridade "alta" devem ser encaminhados para revisão. Todos os demais pedidos devem ser rejeitados. Use estruturas condicionais para tomar a decisão correta e imprima a resposta exata conforme as regras.

Entrada 
Uma única linha contendo dois valores separados por espaço: um número inteiro representando o valor do pedido e uma palavra representando a prioridade ("alta", "media" ou "baixa").

Saída
Uma única palavra: "aprovado", "revisao" ou "rejeitado", de acordo com as regras de decisão.

Exemplos
A tabela abaixo apresenta exemplos de entrada e saída:

Entrada	    Saída
800 alta	aprovado
1200 alta	revisao
500 baixa	rejeitado
1500 media	aprovado
"""

# Recebe a entrada do usuário (valor e prioridade)
entrada = input().strip()
valor_str, prioridade = entrada.split()
valor = int(valor_str)

# TODO: Implemente a lógica condicional para decidir entre "aprovado", "revisao" ou "rejeitado" conforme as regras do desafio.
if valor <= 1000 and (prioridade.upper() == "ALTA" or prioridade.upper() == "MEDIA"):
    saida = "aprovado"
elif valor > 1000 and prioridade.upper() == "ALTA":
    saida = "revisao"
else:
    saida = "rejeitado"
print(saida)