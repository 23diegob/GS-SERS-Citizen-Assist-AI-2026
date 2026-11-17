# Protocolo de avaliação com usuários — Citizen Assist AI

## Finalidade

O protocolo foi elaborado para avaliar clareza, utilidade e compreensão das recomendações energéticas apresentadas pelo módulo de Soluções em Energias Renováveis e Sustentáveis.

## Público e privacidade

A população de referência é formada por cidadãos adultos com interesse em consumo residencial de energia. A coleta, quando realizada, identifica participantes somente por códigos anônimos, sem armazenar CPF, endereço, telefone, contas de energia ou outros identificadores pessoais.

## Situações de interação

| Caso | Interação com o protótipo | Questão de avaliação |
|---|---|---|
| U1 | Consultar o consumo inicial e a alternativa LED | A diferença entre potência e consumo foi compreendida? |
| U2 | Modificar horas de utilização e repetir a comparação | Foi identificado que os resultados mudam com as premissas? |
| U3 | Consultar a alternativa fotovoltaica e seu retorno | Ficou claro que o retorno solar é um limite idealizado? |
| U4 | Abrir a área de fontes e limitações | A origem das informações e as hipóteses são identificáveis? |

## Registro e análise

As avaliações podem ser documentadas em `dados/testes_com_usuarios.csv`, contendo código anônimo, data, situação, percepção de compreensão, clareza (escala de 1 a 5), utilidade (escala de 1 a 5), comentário efetivamente recebido, alteração registrada e observações de reteste.

Uma análise de usabilidade fundamentada exige apresentar as observações efetivamente coletadas e relacioná-las às modificações feitas no protótipo. Não se consideram testes de unidade ou perguntas simuladas como substitutos da avaliação humana.

## Situação dos registros

**Nesta versão, a avaliação com participantes não possui resultados documentados.** O arquivo CSV apresenta a estrutura de registro, sem linhas de participantes. Os 16 testes automatizados documentados em outro arquivo verificam cálculos e lógica de software, não compreensão de pessoas.
