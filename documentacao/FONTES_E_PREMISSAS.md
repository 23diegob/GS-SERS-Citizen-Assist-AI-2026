# Fontes públicas e rastreabilidade de parâmetros

**Data de consulta:** 17 de novembro de 2026.

## Referências

**[1] Ministério de Minas e Energia (MME).** *Potência e consumo de energia: o que são e como impactam na conta de luz.* Publicado em 07 ago. 2026; atualizado em 26 out. 2026. Distingue potência instantânea em W de energia consumida em kWh ao longo do tempo.  
https://www.gov.br/mme/pt-br/assuntos/noticias/julho-26/potencia-e-consumo-de-energia-o-que-sao-e-como-impactam-na-conta-de-luz

**[2] U.S. Department of Energy (DOE).** *Purchasing Energy-Efficient Light Bulbs*, tabela 2, comparação de fluxo luminoso e potência. Para aproximadamente 800 lúmens, apresenta 60 W para incandescente e 5,9 a 10,5 W para LED.  
https://www.energy.gov/cmei/femp/purchasing-energy-efficient-light-bulbs

**[3] CRESESB/CEPEL.** *SunData v. 3.0 — potencial solar.* Recurso de consulta de irradiação solar por coordenadas geográficas. A pesquisa não executou consulta geográfica específica; a entrada de 4 h/dia é apenas hipótese.  
https://www.cresesb.cepel.br/index.php?section=sundata

**[4] Agência Nacional de Energia Elétrica (ANEEL).** *Micro e Minigeração Distribuída.* Informações sobre compensação da geração distribuída e custo de disponibilidade; esclarece que a agência não fixa preços de equipamentos solares.  
https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida

**[5] Brasil.** *Lei nº 14.300, de 6 de janeiro de 2022.* Marco legal da microgeração, minigeração e do Sistema de Compensação de Energia Elétrica.  
https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm

**[6] Governo do Estado de São Paulo / Poupatempo.** *Obter Carteira de Identidade Nacional (CIN).* Fonte contextual do módulo de orientação documental, distinto do módulo de energia.  
https://www.poupatempo.sp.gov.br/carta/D97C3844-A2D9-4C9E-B364-CB4FEB26A1FB

## Correspondência entre fontes e modelo

| Componente | Informação sustentada | Natureza dos valores numéricos do protótipo |
|---|---|---|
| Fórmula de consumo | [1] fundamenta W, kWh e tempo | Aplicação matemática às hipóteses de uso |
| Eficiência de iluminação | [2] fundamenta aproximação em lúmens entre 60 W e LED | Escolha de 9 W dentro da faixa citada |
| Irradiação solar | [3] indica método para consultar dados geográficos | 4 h/dia é hipótese, sem consulta por coordenadas |
| Compensação solar | [4] e [5] fundamentam limites regulatórios | Economia de R$ 81/mês é teto didático, não projeção de fatura |
| Custo LED e instalação FV | Nenhuma fonte usada como pesquisa de preço | R$ 15/LED e R$ 5.000/FV são hipóteses |
| Tarifa | Nenhuma fatura ou concessionária consultada | R$ 0,90/kWh é hipótese |
| Contexto documental | [6] fundamenta orientação preliminar sobre CIN | Não integra os cálculos de energia |

Os dados de referência e suas unidades estão documentados em `dados/premissas.csv`. A tabela de resultados `dados/comparacao_exemplo.csv` pode ser reproduzida pelas funções em `energia.py` com os parâmetros padrão.
