# Relatório de Implementação de Serviços AWS

**Data:** 07/05/2026  
**Empresa:** Abstergo Industries  
**Responsável:** Alex Carlos de Sousa  

---

## Introdução

Este relatório apresenta uma proposta de implementação de serviços AWS na empresa **Abstergo Industries**, com foco na **redução imediata de custos operacionais em nuvem**, melhoria da governança financeira e otimização do uso de recursos computacionais.

O objetivo do projeto é selecionar e aplicar **3 serviços AWS** capazes de apoiar a empresa na identificação de desperdícios, controle de orçamento e melhor aproveitamento dos recursos contratados.

A proposta considera um cenário corporativo em que a empresa utiliza serviços em nuvem para armazenamento de arquivos, execução de aplicações e ambientes de desenvolvimento, homologação e produção.

---

## Objetivo do Projeto

Implementar ferramentas AWS que auxiliem na redução de custos por meio de:

- Monitoramento e controle de gastos;
- Identificação de recursos subutilizados;
- Otimização automática de armazenamento;
- Apoio à tomada de decisão baseada em dados;
- Criação de uma cultura de FinOps e governança em nuvem.

---

## Descrição do Projeto

O projeto foi dividido em 3 etapas principais, cada uma relacionada a um serviço AWS específico.

---

## Etapa 1: AWS Budgets

### Nome da ferramenta

**AWS Budgets**

### Foco da ferramenta

Controle de orçamento, alertas de custos e prevenção de gastos acima do planejado.

### Descrição do caso de uso

A empresa Abstergo Industries possui diferentes times utilizando recursos em nuvem, como ambientes de testes, aplicações internas e armazenamento de arquivos. Sem um controle adequado, os custos podem crescer de forma inesperada.

Com o **AWS Budgets**, será possível criar orçamentos mensais por conta, projeto, ambiente ou serviço. A ferramenta permite configurar alertas quando os gastos ultrapassarem determinados percentuais do orçamento, por exemplo:

- 50% do orçamento consumido;
- 80% do orçamento consumido;
- 100% do orçamento consumido;
- previsão de estouro do orçamento antes do fechamento do mês.

Segundo a documentação oficial da AWS, o AWS Budgets permite configurar notificações quando os custos ou uso excedem, ou têm previsão de exceder, os valores definidos no orçamento. As notificações podem ser enviadas por e-mail ou Amazon SNS.  
Fonte: AWS Budgets :contentReference[oaicite:0]{index=0}

### Benefícios esperados

- Maior previsibilidade dos custos;
- Redução de gastos inesperados;
- Monitoramento preventivo;
- Apoio à gestão financeira da nuvem;
- Maior responsabilidade dos times sobre o consumo de recursos.

### Exemplo prático

Criar um orçamento mensal de R$ 5.000,00 para ambientes de desenvolvimento e homologação, com alertas automáticos para os responsáveis quando o consumo atingir 50%, 80% e 100% do valor definido.

---

## Etapa 2: AWS Compute Optimizer

### Nome da ferramenta

**AWS Compute Optimizer**

### Foco da ferramenta

Otimização de recursos computacionais e identificação de instâncias superdimensionadas ou ociosas.

### Descrição do caso de uso

A empresa utiliza recursos computacionais, como instâncias EC2, volumes EBS e serviços relacionados. Em muitos cenários, esses recursos podem estar superdimensionados, ou seja, contratados com capacidade maior do que a real necessidade da aplicação.

O **AWS Compute Optimizer** utiliza análise de métricas históricas para gerar recomendações de otimização. A ferramenta pode indicar, por exemplo:

- Instâncias EC2 com capacidade acima do necessário;
- Recursos ociosos;
- Melhor tipo de instância para determinada carga de trabalho;
- Possibilidades de redução de custo sem perda de desempenho.

A AWS informa que o Compute Optimizer recomenda recursos mais eficientes para reduzir custos e melhorar performance, além de identificar recursos não utilizados e recomendar configurações ideais para workloads superdimensionados. :contentReference[oaicite:1]{index=1}

### Benefícios esperados

- Redução de custos com recursos computacionais;
- Melhor aproveitamento da infraestrutura;
- Identificação de desperdícios;
- Apoio à modernização de ambientes;
- Melhoria contínua da performance.

### Exemplo prático

Analisar instâncias EC2 utilizadas em ambientes de homologação e identificar servidores com baixo uso de CPU e memória, recomendando a troca por instâncias menores ou o desligamento de recursos ociosos fora do horário comercial.

---

## Etapa 3: Amazon S3 Intelligent-Tiering

### Nome da ferramenta

**Amazon S3 Intelligent-Tiering**

### Foco da ferramenta

Redução de custos de armazenamento por movimentação automática de dados entre camadas de acesso.

### Descrição do caso de uso

A empresa armazena documentos, backups, relatórios e arquivos históricos em buckets Amazon S3. Nem todos esses arquivos são acessados com frequência. Alguns são usados diariamente, enquanto outros ficam armazenados apenas para consulta eventual ou obrigação legal.

O **Amazon S3 Intelligent-Tiering** permite otimizar os custos de armazenamento ao mover automaticamente objetos entre diferentes camadas, de acordo com o padrão de acesso. A AWS informa que essa classe de armazenamento monitora os padrões de acesso e move automaticamente os objetos para camadas de menor custo quando eles não são acessados por determinado período.

### Benefícios esperados

- Redução automática dos custos de armazenamento;
- Menor necessidade de administração manual;
- Manutenção da performance para dados acessados com frequência;
- Adequação para arquivos com padrão de acesso desconhecido ou variável;
- Melhor organização da estratégia de armazenamento.

### Exemplo prático

Aplicar S3 Intelligent-Tiering em buckets utilizados para armazenar relatórios fiscais, documentos antigos, arquivos de backup e evidências de auditoria, permitindo que arquivos pouco acessados sejam automaticamente movidos para camadas de menor custo.

---

## Resumo das Soluções Propostas

| Etapa | Serviço AWS | Objetivo | Benefício Principal |
|------|-------------|----------|---------------------|
| 1 | AWS Budgets | Controlar custos e gerar alertas | Evitar estouro de orçamento |
| 2 | AWS Compute Optimizer | Otimizar recursos computacionais | Reduzir desperdícios com recursos superdimensionados |
| 3 | Amazon S3 Intelligent-Tiering | Otimizar armazenamento | Reduzir custos com arquivos pouco acessados |

---

## Plano de Implementação

| Fase | Atividade | Resultado Esperado |
|-----|-----------|-------------------|
| 1 | Levantamento dos custos atuais | Identificação dos principais serviços que geram custo |
| 2 | Configuração do AWS Budgets | Alertas de orçamento ativos |
| 3 | Ativação do AWS Compute Optimizer | Recomendações de otimização disponíveis |
| 4 | Análise das recomendações | Plano de ajuste dos recursos |
| 5 | Aplicação do S3 Intelligent-Tiering | Otimização automática de armazenamento |
| 6 | Monitoramento contínuo | Acompanhamento da economia gerada |

---

## Resultados Esperados

Com a implementação das ferramentas propostas, espera-se que a Abstergo Industries obtenha:

- Redução de custos com recursos ociosos ou superdimensionados;
- Melhor controle financeiro dos serviços em nuvem;
- Maior previsibilidade de gastos mensais;
- Otimização do armazenamento de arquivos;
- Maior maturidade em governança de custos;
- Apoio à cultura FinOps dentro da organização.

---

## Conclusão

A implementação dos serviços **AWS Budgets**, **AWS Compute Optimizer** e **Amazon S3 Intelligent-Tiering** representa uma estratégia prática e eficiente para redução de custos imediatos na Abstergo Industries.

Essas ferramentas permitem controlar o orçamento, identificar desperdícios e automatizar a otimização de armazenamento, contribuindo para uma operação em nuvem mais econômica, escalável e governada.

Recomenda-se que a empresa mantenha um processo contínuo de análise dos custos em nuvem, revisando periodicamente os relatórios, alertas e recomendações geradas pelas ferramentas AWS.

---

## Anexos

- Documentação oficial do AWS Budgets;
- Documentação oficial do AWS Compute Optimizer;
- Documentação oficial do Amazon S3 Intelligent-Tiering;
- Evidências de configuração dos serviços;
- Prints do console AWS;
- Planilha de acompanhamento de custos;
- Relatório comparativo antes e depois da implementação.

---

## Referências

- AWS Budgets: https://aws.amazon.com/aws-cost-management/aws-budgets/
- AWS Compute Optimizer: https://aws.amazon.com/compute-optimizer/
- Amazon S3 Intelligent-Tiering: https://aws.amazon.com/s3/storage-classes/intelligent-tiering/
- Documentação Amazon S3 Intelligent-Tiering: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering-overview.html

---
