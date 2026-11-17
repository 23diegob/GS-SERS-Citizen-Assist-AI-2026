# Estudo técnico — consumo residencial e alternativas sustentáveis

**Citizen Assist AI · Soluções em Energias Renováveis e Sustentáveis · Novembro de 2026**

## 1. Objeto do estudo

O estudo avalia duas abordagens distintas para o atendimento de uma mesma necessidade energética: iluminação residencial durante 150 horas por mês. A primeira alternativa reduz a demanda elétrica por meio de lâmpadas mais eficientes. A segunda introduz geração própria de energia solar fotovoltaica mantendo a demanda original. O escopo corresponde aos dez pontos de iluminação do cenário e não à residência inteira.

O público de referência são cidadãos adultos do estado de São Paulo que procuram informações acessíveis para interpretar gastos elétricos. O modelo não utiliza consumo real de um endereço, conta de concessionária ou orçamento comercial.

## 2. Fundamentação e hipóteses

Potência (W) representa a taxa instantânea de utilização da energia; consumo (kWh) incorpora potência e tempo. A distinção é apresentada pelo Ministério de Minas e Energia. Para a escolha de lâmpadas aproximadamente equivalentes em iluminação, o U.S. Department of Energy apresenta 60 W incandescentes e de 5,9 W a 10,5 W em LED para uma saída luminosa de aproximadamente 800 lúmens. Selecionou-se 9 W como ponto ilustrativo nessa faixa.

| Variável | Símbolo | Valor | Classificação |
|---|---|---:|---|
| Pontos de iluminação | n | 10 | Hipótese de domicílio-modelo |
| Potência existente | P0 | 60 W/lâmpada | Hipótese de produto, equivalência luminosa fundamentada |
| Potência LED | P1 | 9 W/lâmpada | Potência ilustrativa dentro da faixa de referência |
| Tempo de uso | h | 5 h/dia | Hipótese comportamental |
| Período | d | 30 dias/mês | Convenção de cálculo |
| Tarifa da parcela variável | t | R$ 0,90/kWh | Hipótese econômica |
| Custo de cada LED | c1 | R$ 15,00 | Hipótese econômica |
| Potência solar de pico | PFV | 1,0 kWp | Hipótese técnica |
| Sol pleno equivalente | HSP | 4,0 h/dia | Hipótese; sem consulta por coordenadas |
| Fator de desempenho | PR | 0,75 | Hipótese agregada de perdas |
| Custo do sistema FV | cFV | R$ 5.000,00 | Hipótese econômica |

Os registros detalhados constam em `dados/premissas.csv`. **Nenhuma das hipóteses monetárias corresponde a tarifa oficial ou orçamento obtido em fornecedores.**

## 3. Consumo da situação de referência

Fórmula: `E = n × P × h × d / 1000`.

- Potência total: `10 × 60 = 600 W = 0,60 kW`.
- Horas mensais: `5 × 30 = 150 h`.
- Consumo mensal: `0,60 × 150 = 90,00 kWh`.
- Parcela variável ilustrativa: `90,00 × R$ 0,90 = R$ 81,00`.
- Projeção linear anual: `90 × 12 = 1.080 kWh`, supondo doze meses idênticos.

O custo de R$ 81,00 representa apenas uma conta simplificada da eletricidade usada na iluminação analisada. Não reproduz a fatura de uma unidade consumidora.

## 4. Alternativa A — eficiência energética com LED

A substituição dos dez equipamentos incandescentes de 60 W por dez equipamentos LED de 9 W foi considerada com permanência das mesmas horas de uso e luminosidade aproximada de 800 lúmens por ponto de luz.

- Nova potência instalada: `10 × 9 = 90 W = 0,09 kW`.
- Consumo mensal: `0,09 × 150 = 13,50 kWh`.
- Redução de consumo: `90,00 – 13,50 = 76,50 kWh/mês`.
- Redução percentual: `76,50 / 90 × 100 = 85,00%`.
- Parcela variável com LED: `13,50 × 0,90 = R$ 12,15/mês`.
- Economia ilustrativa: `76,50 × 0,90 = R$ 68,85/mês`.
- Custo inicial: `10 × R$ 15,00 = R$ 150,00`.
- Retorno simples: `150 / 68,85 = 2,18 meses`.
- Projeção de energia anual evitada: `76,5 × 12 = 918 kWh`.

**Viabilidade:** depende da condição prévia das lâmpadas, compatibilidade de instalação, fluxo luminoso, temperatura de cor e tempo real de uso. O retorno seria menor se a base já tivesse lâmpadas eficientes. A troca evita parte do consumo elétrico, mas gera resíduos e requer descarte adequado dos equipamentos substituídos.

## 5. Alternativa B — geração solar fotovoltaica

A alternativa renovável considera a instalação hipotética de um sistema fotovoltaico conectado à rede, conservando as dez lâmpadas existentes. A geração é calculada por `G = PFV × HSP × PR × d`.

- Potência de pico: `1,0 kWp`.
- Sol pleno equivalente: `4,0 h/dia`, escolhido como premissa, sem consulta de irradiação local.
- Desempenho global: `0,75`, parâmetro hipotético de perdas.
- Geração mensal: `1,0 × 4,0 × 0,75 × 30 = 90,00 kWh`.
- Parcela atribuída à iluminação no modelo: `min(90, 90) = 90,00 kWh/mês`.
- **Teto monetário puramente ilustrativo:** `90 × R$ 0,90 = R$ 81,00/mês`.
- Investimento hipotético: `R$ 5.000,00`.
- Retorno simples sob teto idealizado: `5.000 / 81 = 61,73 meses`.

As lâmpadas continuariam consumindo 90 kWh/mês. A geração adicional não constitui redução física de demanda. A conta final é influenciada por autoconsumo, energia injetada e compensada, enquadramento no Sistema de Compensação de Energia Elétrica (SCEE), tarifas, encargos, impostos e custos de disponibilidade. A Lei nº 14.300/2022 e as orientações da ANEEL fundamentam a existência dessas condições, **não os valores monetários hipotéticos do exemplo**.

**Viabilidade:** depende de local de implantação, sombreamento, orientação, estrutura, conexão e condições de acesso. O sistema requer análise técnica específica. **Impactos:** utiliza uma fonte renovável na operação, mas fabricação, transporte, manutenção e destinação dos equipamentos possuem custos ambientais. Não se estima CO₂ evitado sem parâmetros adicionais.

## 6. Comparação no mesmo período e necessidade

| Critério | Referência | A — LED | B — Fotovoltaica |
|---|---:|---:|---:|
| Consumo elétrico da iluminação | 90,0 kWh/mês | 13,5 kWh/mês | 90,0 kWh/mês |
| Redução física de consumo | 0 | 76,5 kWh/mês | 0 |
| Geração elétrica local | 0 | 0 | 90,0 kWh/mês |
| Economia variável, simulação | 0 | R$ 68,85/mês | Até R$ 81,00/mês, apenas teto |
| Custo inicial, simulação | 0 | R$ 150,00 | R$ 5.000,00 |
| Retorno simples, simulação | — | 2,18 meses | 61,73 meses, apenas teto |

A soma direta das economias máximas das duas alternativas é inválida: a troca por LED diminui o consumo energético que um sistema fotovoltaico dimensionado para a situação original poderia suprir. Para analisar a combinação, seria necessário recalcular a demanda e o uso de energia da residência como um todo.

## 7. Sensibilidade financeira

A economia solar de R$ 81,00/mês equivale a um cenário ideal de aproveitamento integral do teto monetário. A influência da realização de uma fração desse teto pode ser observada sem representar regras legais:

| Fração hipotética do teto | Economia mensal | Retorno simples |
|---|---:|---:|
| 100% | R$ 81,00 | 61,73 meses |
| 70% | R$ 56,70 | 88,18 meses |
| 50% | R$ 40,50 | 123,46 meses |

As frações de 70% e 50% são exercícios matemáticos de sensibilidade, **não alíquotas ou parâmetros oficiais do SCEE**. Não se modelaram deterioração, custo do capital, financiamento, manutenção ou variação mensal do clima.

## 8. Aplicação às respostas do assistente

Os dados são processados em `energia.py` e consumidos por `assistente.py`. Assim, a resposta de consumo, a comparação entre alternativas e a explicação de custos são obtidas dos mesmos cálculos usados na interface. A simulação web pode variar quantitativos, potências, horas, tarifa, custos, capacidade fotovoltaica, horas solares e desempenho.

**Consulta:** “Quanto economizo com LED?”  
**Resposta de referência:** “A troca de dez lâmpadas de 60 W por dez LED de 9 W, com uso de 5 horas/dia durante 30 dias, reduz o consumo de 90,0 para 13,5 kWh/mês. A economia é de 76,5 kWh/mês, ou 85%. Com uma tarifa hipotética de R$ 0,90/kWh, a parcela variável simulada diminui R$ 68,85/mês. Os valores dependem das condições reais de uso e da equivalência luminosa.”

O assistente utiliza regras linguísticas determinísticas e não produz previsão individualizada de custos sem que as premissas fornecidas sejam verificadas.

## 9. Validação e alcance dos resultados

A suíte automatizada contém 16 testes que verificam fórmulas, cenário-padrão, limites de compensação do modelo, tratamento de parâmetros inválidos, respostas do assistente e oito estados do demonstrador CIN. A avaliação com participantes utiliza o protocolo descrito em `documentacao/AVALIACAO_USABILIDADE.md`. Na versão documentada, não há registros efetivos de participantes e, portanto, não são declarados resultados de usabilidade coletados.

O resultado central é a capacidade de fornecer uma comparação **auditável e reproduzível** entre redução de consumo e geração renovável, com ressalvas explícitas. O exemplo apoia educação energética, não substitui diagnóstico de consumo, estudo de viabilidade ou orçamento para instalação.

## 10. Fontes

As referências e a associação de cada dado à respectiva fonte estão detalhadas em `documentacao/FONTES_E_PREMISSAS.md`, incluindo Ministério de Minas e Energia, U.S. Department of Energy, CRESESB, ANEEL e Lei nº 14.300/2022.
