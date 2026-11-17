# Citizen Assist AI — Energia e Sustentabilidade

**FIAP · Global Solution 2026.2 · Bacharelado em Ciência da Computação**  
**Disciplina:** Soluções em Energias Renováveis e Sustentáveis  
**Tema:** Citizen Assist AI — orientação cidadã fundamentada em dados

**Integrantes:** Diego de Oliveira Brandão (RM 569773) e Cristhian Henrique Clementino (RM 574117).

## Resumo

O Citizen Assist AI é um protótipo de assistência digital que reúne orientações objetivas sobre necessidades do cotidiano. O módulo de Energia e Sustentabilidade examina o consumo elétrico da iluminação residencial e oferece uma comparação fundamentada entre duas estratégias: substituição de lâmpadas incandescentes por LED e geração distribuída de eletricidade por sistema solar fotovoltaico.

A solução integra **cálculos reproduzíveis**, uma **interface interativa** e um **assistente de respostas orientadas por regras**. O usuário pode modificar hipóteses de consumo, custo e geração, obtendo resultados atualizados. O sistema não depende de APIs de inteligência artificial generativa nem utiliza dados pessoais para executar o estudo.

## Contexto e público

O público-alvo compreende cidadãos adultos de São Paulo interessados em consumo consciente e decisões energéticas residenciais. O problema observado é a dificuldade de interpretar potência elétrica, tempo de funcionamento, energia consumida e custo relativo de alternativas tecnológicas.

O estudo utiliza uma **residência-modelo hipotética** com dez pontos de luz em funcionamento por cinco horas diárias durante trinta dias. Não foram utilizadas medições de uma casa específica. As alternativas são comparadas para a **mesma necessidade de iluminação e o mesmo período mensal**.

## Cenário de análise

| Parâmetro | Valor utilizado | Natureza |
|---|---:|---|
| Quantidade de lâmpadas | 10 | Hipótese do cenário |
| Potência das lâmpadas atuais | 60 W cada | Hipótese com equivalência luminosa referenciada |
| Potência das lâmpadas LED | 9 W cada | Escolha ilustrativa, compatível com faixa do DOE |
| Tempo de utilização | 5 h/dia por 30 dias | Hipótese de uso |
| Tarifa para a parcela variável | R$ 0,90/kWh | Hipótese financeira, não tarifa oficial |
| Preço unitário do LED | R$ 15,00 | Hipótese financeira |
| Sistema fotovoltaico | 1,0 kWp | Hipótese técnica |
| Horas equivalentes de sol pleno | 4,0 h/dia | Hipótese, não aferição local |
| Fator de desempenho solar | 75% | Hipótese de perdas |
| Investimento fotovoltaico | R$ 5.000,00 | Hipótese financeira |

A distinção entre watts (potência) e kWh (energia) é fundamentada pelo Ministério de Minas e Energia. A correspondência aproximada de luminosidade entre 60 W incandescentes e LEDs na faixa de 5,9 a 10,5 W, para cerca de 800 lúmens, consta em material do U.S. Department of Energy. Os valores monetários e solares não derivam dessas fontes; são hipóteses explicitadas no conjunto de dados.

## Método

Consumo mensal de eletricidade:

`E (kWh/mês) = quantidade × potência (W) × horas/dia × dias/mês ÷ 1.000`

Geração fotovoltaica mensal aproximada:

`G (kWh/mês) = potência instalada (kWp) × horas de sol pleno (h/dia) × fator de desempenho × dias/mês`

Os cálculos de economia monetária usam uma parcela variável simplificada de consumo, sem componentes fixos da fatura, tributos, encargos, condições específicas de compensação ou variações climáticas.

## Resultados calculados

| Indicador | Situação atual | Troca por LED | Solar fotovoltaica |
|---|---:|---:|---:|
| Demanda da iluminação | 90,0 kWh/mês | 13,5 kWh/mês | 90,0 kWh/mês |
| Redução física de consumo | — | 76,5 kWh/mês (85%) | 0 kWh/mês |
| Geração local estimada | — | — | 90,0 kWh/mês |
| Benefício financeiro ilustrativo | — | R$ 68,85/mês | Até R$ 81,00/mês (teto ideal) |
| Investimento hipotético | — | R$ 150,00 | R$ 5.000,00 |
| Retorno simples ilustrativo | — | 2,18 meses | 61,73 meses (teto otimista) |

**Interpretação:** LED reduz efetivamente a demanda por eletricidade. A alternativa fotovoltaica produz eletricidade, mas não altera o consumo das lâmpadas originalmente utilizadas. A equivalência entre geração mensal e consumo mensal **não significa conta de energia igual a zero**. O benefício solar indicado constitui um limite teórico simplificado; compensação, disponibilidade, encargos e tributos não foram modelados.

O investimento inicial da substituição por LED é substancialmente inferior no exemplo. A análise recomenda avaliar primeiro a eficiência da iluminação, preservando a opção fotovoltaica como alternativa renovável a ser dimensionada de acordo com o consumo integral da residência.

## Funcionamento do protótipo

A interface oferece as seguintes áreas:

- **Análise energética:** resultados mensais, comparação lado a lado, investimento, viabilidade e impactos ambientais.
- **Assistente:** respostas sobre consumo, LED, geração solar, comparação, fontes e limitações, calculadas com os parâmetros ativos.
- **Orientação CIN:** demonstração contextual do Citizen Assist AI, voltada à conferência preliminar de condições do serviço documental; não representa verificação em sistemas oficiais.
- **Fontes e limites:** fórmulas, instituições de referência e premissas não verificadas empiricamente.

A arquitetura mantém os cálculos no arquivo `energia.py`, as regras de resposta no arquivo `assistente.py` e as interfaces em `app.py` e `main.py`. A contribuição principal da disciplina é o módulo energético.

## Estrutura do repositório

```text
Citizen_Assist_AI_SERS_2026_2_FINAL/
├── README.md
├── app.py
├── assistente.py
├── energia.py
├── main.py
├── INICIAR_WINDOWS.bat
├── requirements.txt
├── .gitignore
├── dados/
│   ├── premissas.csv
│   ├── comparacao_exemplo.csv
│   └── testes_com_usuarios.csv
├── documentacao/
│   ├── ESTUDO_ENERGETICO.md
│   ├── FONTES_E_PREMISSAS.md
│   ├── ARQUITETURA_E_VALIDACAO.md
│   ├── AVALIACAO_USABILIDADE.md
│   ├── TESTES_AUTOMATIZADOS.txt
│   └── RELATORIO_TECNICO_SERS.pdf
└── tests/
    └── test_energia.py
```

## Ambiente e reprodução

O projeto utiliza **Python 3.10+**. A interface gráfica é implementada com Streamlit e os cálculos são executados localmente.

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

A interface de linha de comando funciona sem bibliotecas externas:

```bash
python main.py
```

A suíte de verificação automatizada utiliza `unittest`:

```bash
python -m unittest discover -s tests -v
```

## Verificação e limitações

Foram executados **16 testes automatizados**, cobrindo cálculos de energia, consistência das alternativas, tratamento de parâmetros e respostas do assistente. O relatório de execução consta em [`documentacao/TESTES_AUTOMATIZADOS.txt`](documentacao/TESTES_AUTOMATIZADOS.txt).

O protocolo de avaliação de compreensibilidade com participantes está descrito em [`documentacao/AVALIACAO_USABILIDADE.md`](documentacao/AVALIACAO_USABILIDADE.md). **Não existem registros de avaliações com participantes nesta versão**; o CSV correspondente contém exclusivamente o cabeçalho, sem resultados atribuídos a pessoas.

Os resultados são **simulações didáticas**, não medições de campo, orçamento de fornecedores, dimensionamento fotovoltaico ou previsão de fatura. O impacto ambiental é discutido qualitativamente, sem estimativas numéricas de emissões evitadas por ausência de fator de emissão aplicado e validado ao caso.

## Documentação e referências

O detalhamento dos procedimentos, fórmulas e análise crítica está em [`documentacao/ESTUDO_ENERGETICO.md`](documentacao/ESTUDO_ENERGETICO.md) e no [`relatório técnico em PDF`](documentacao/RELATORIO_TECNICO_SERS.pdf). As referências oficiais e a rastreabilidade dos parâmetros estão organizadas em [`documentacao/FONTES_E_PREMISSAS.md`](documentacao/FONTES_E_PREMISSAS.md).

São utilizados materiais do **Ministério de Minas e Energia**, **U.S. Department of Energy**, **CRESESB/SunData**, **ANEEL** e **Lei nº 14.300/2022**, respeitando o alcance e as limitações de cada fonte.
