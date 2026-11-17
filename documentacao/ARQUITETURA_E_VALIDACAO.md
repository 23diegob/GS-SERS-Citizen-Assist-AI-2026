# Arquitetura, funcionamento e verificação

## Visão arquitetural

O Citizen Assist AI separa o núcleo matemático da apresentação. A abordagem mantém consistentes os valores fornecidos pelo assistente e os valores apresentados na análise interativa.

```text
                  +--------------------------+
                  | Interface web (app.py)   |
                  | Terminal (main.py)       |
                  +------------+-------------+
                               |
                 +-------------v--------------+
                 | Respostas (assistente.py)  |
                 +-------------+--------------+
                               |
                 +-------------v--------------+
                 | Modelo energético          |
                 | (energia.py)               |
                 +-------------+--------------+
                               |
              +----------------v----------------+
              | Parâmetros / resultados         |
              | dados/*.csv / testes automáticos|
              +---------------------------------+
```

## Componentes principais

| Arquivo | Responsabilidade |
|---|---|
| `energia.py` | Classe `Parametros`, validação das entradas, fórmulas de consumo e geração, custos e retornos |
| `assistente.py` | Identificação de temas em perguntas e composição de respostas a partir de resultados calculados; demonstrador CIN |
| `app.py` | Interface Streamlit com cenários editáveis, comparação tabular, respostas e referências |
| `main.py` | Acesso alternativo via terminal e demonstração de cálculos e do assistente |
| `dados/premissas.csv` | Parâmetros, unidades, classificação e justificativas |
| `dados/comparacao_exemplo.csv` | Resultado numérico do cenário-padrão |
| `tests/test_energia.py` | Testes automatizados com `unittest` |

## Fluxo funcional

A entrada dos parâmetros ocorre na interface web, que instancia `Parametros`, executa `calcular` e apresenta resultados. As consultas ao assistente passam por `responder_pergunta`, que utiliza o mesmo objeto `Parametros` e executa os mesmos cálculos. A atualização dos parâmetros altera imediatamente as respostas, preservando a rastreabilidade do modelo.

O sistema é um **assistente de regras e cálculos**, não um modelo generativo. Essa arquitetura permite reproduzir resultados sem chave de API ou acesso à internet. O demonstrador CIN representa outro tema de assistência cidadã e não modifica as hipóteses ou resultados energéticos.

## Verificações automatizadas

Os testes de unidade contemplam: situação inicial, economia com LED, cálculo fotovoltaico, limitação da compensação ao serviço analisado, alteração de parâmetros, rejeição de configurações inválidas, normalização e classificação de perguntas, coerência numérica das respostas e estados de verificação do módulo CIN.

O relatório de execução está registrado em `TESTES_AUTOMATIZADOS.txt`. Os testes são executados com a biblioteca padrão do Python:

```bash
python -m unittest discover -s tests -v
```

## Limitações técnicas

A projeção solar representa produção energética média aproximada; não incorpora produção horária, autoconsumo, excedentes da unidade consumidora, fatura real, impostos, tarifas de compensação, degradação fotovoltaica ou financiamento. O módulo LED pressupõe mesma iluminação útil. Os parâmetros do cenário são ilustrativos. Nenhuma informação de CPF ou documento é solicitada ou armazenada pelo sistema.
