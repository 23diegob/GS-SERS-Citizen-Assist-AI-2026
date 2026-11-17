"""Interface web do Citizen Assist AI com o módulo da disciplina SERS."""
import streamlit as st
from energia import FONTES, Parametros, calcular
from assistente import responder_pergunta, verificar_cin

st.set_page_config(page_title="Citizen Assist AI | Energia", page_icon="🌱", layout="wide")
st.markdown("""
<style>
.block-container {padding-top: 2rem; max-width: 1250px;}
h1, h2, h3 {letter-spacing: -.035em;}
[data-testid="stMetric"] {border:1px solid #34465333; border-radius:14px; padding:13px 16px;}
small, .stCaption {line-height: 1.5;}
</style>
""", unsafe_allow_html=True)

st.title("🌱 Citizen Assist AI")
st.caption("Global Solution 2026.2 • Módulo de energia e sustentabilidade • FIAP")
st.info("SIMULAÇÃO ACADÊMICA — Valores padrão são ilustrativos, não dados medidos, tarifas oficiais nem propostas comerciais.")

with st.sidebar:
    st.header("⚙️ Personalizar cenário")
    st.caption("Mesma necessidade: iluminação de uma residência em São Paulo, com uso constante nos três cenários.")
    lampadas = st.slider("Quantidade de lâmpadas", 1, 30, 10)
    potencia_atual = st.slider("Potência atual (W por lâmpada)", 20, 120, 60, 5)
    potencia_led = st.slider("Potência LED (W por lâmpada)", 3, 19, 9, 1)
    horas = st.slider("Horas de uso por dia", 1.0, 16.0, 5.0, 0.5)
    dias = st.slider("Dias de uso por mês", 1, 31, 30)
    tarifa = st.number_input("Tarifa didática (R$/kWh)", 0.01, 5.00, 0.90, 0.05)
    preco_led = st.number_input("Preço didático por LED (R$)", 1.0, 100.0, 15.0, 1.0)
    st.divider()
    st.subheader("☀️ Hipóteses solares")
    potencia_pv = st.number_input("Potência do sistema (kWp)", 0.10, 30.0, 1.0, 0.1)
    sol = st.number_input("Sol pleno equivalente (h/dia)", 0.5, 10.0, 4.0, 0.1)
    desempenho = st.slider("Desempenho global (%)", 40, 95, 75) / 100
    custo_pv = st.number_input("Investimento didático (R$)", 100.0, 200000.0, 5000.0, 100.0)

p = Parametros(lampadas=lampadas, potencia_atual_w=potencia_atual,
               potencia_led_w=potencia_led, horas_dia=horas, dias_mes=dias,
               tarifa_rs_kwh=tarifa, preco_led_unit_rs=preco_led,
               potencia_solar_kwp=potencia_pv, sol_pleno_h_dia=sol,
               desempenho_solar=desempenho, custo_solar_rs=custo_pv)
r = calcular(p)


def dinheiro(valor: float) -> str:
    return "R$ " + f"{valor:,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")


def num(valor: float, dec=1) -> str:
    return f"{valor:,.{dec}f}".replace(",", "x").replace(".", ",").replace("x", ".")

aba_energia, aba_assistente, aba_cin, aba_referencias = st.tabs(
    ["⚡ Análise energética", "💬 Assistente", "🪪 Integração CIN", "📚 Fontes e limites"]
)

with aba_energia:
    st.subheader("Comparação técnica de duas alternativas")
    st.write("**Público:** cidadãos adultos de São Paulo que buscam orientações práticas e acessíveis. "
             "**Necessidade:** manter a mesma iluminação gastando menos energia da rede. "
             "**Alternativas:** trocar lâmpadas antigas por LED e instalar geração solar fotovoltaica.")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Consumo atual", f"{num(r['referencia_kwh_mes'])} kWh/mês")
    c2.metric("Consumo com LED", f"{num(r['led_kwh_mes'])} kWh/mês",
              f"-{num(r['led_reducao_percentual'])}%")
    c3.metric("Geração solar estimada", f"{num(r['solar_geracao_potencial_kwh_mes'])} kWh/mês")
    c4.metric("Economia LED na energia", f"{dinheiro(r['led_economia_rs_mes'])}/mês")

    st.markdown("#### Resultado sob o mesmo período de referência")
    st.dataframe([
        {"Alternativa": "Situação atual", "Consumo da iluminação (kWh/mês)": round(r['referencia_kwh_mes'],2),
         "Energia poupada/compensável (kWh/mês)": 0.0,
         "Benefício monetário teórico (R$/mês)": 0.0, "Investimento suposto (R$)": 0.0},
        {"Alternativa": "Trocar por LED", "Consumo da iluminação (kWh/mês)": round(r['led_kwh_mes'],2),
         "Energia poupada/compensável (kWh/mês)": round(r['led_reducao_kwh_mes'],2),
         "Benefício monetário teórico (R$/mês)": round(r['led_economia_rs_mes'],2),
         "Investimento suposto (R$)": round(r['led_investimento_rs'],2)},
        {"Alternativa": "Solar fotovoltaica (mantém lâmpadas)", "Consumo da iluminação (kWh/mês)": round(r['referencia_kwh_mes'],2),
         "Energia poupada/compensável (kWh/mês)": round(r['solar_compensacao_potencial_kwh_mes'],2),
         "Benefício monetário teórico (R$/mês)": round(r['solar_economia_teto_rs_mes'],2),
         "Investimento suposto (R$)": round(r['solar_investimento_rs'],2)},
    ], hide_index=True, use_container_width=True)
    st.caption("Para LED, o kWh diminui fisicamente; para solar, o consumo das lâmpadas não cai: a "
               "geração pode compensar energia de rede apenas nas condições legais e operacionais aplicáveis.")
    col_led, col_sol = st.columns(2)
    with col_led:
        st.markdown("#### 💡 Eficiência: lâmpadas LED")
        st.write(f"Redução do uso de eletricidade: **{num(r['led_reducao_kwh_mes'])} kWh/mês** "
                 f"(**{num(r['led_reducao_percentual'])}%**).")
        st.write(f"Investimento didático: **{dinheiro(r['led_investimento_rs'])}**. "
                 f"Retorno simples: **{num(r['led_retorno_meses'])} meses**.")
        st.write("**Viabilidade:** menor custo inicial e implantação rápida; validar equivalência de luminosidade "
                 "(lúmens), base e compatibilidade da luminária.")
        st.write("**Ambiental:** menor consumo de energia; descartar lâmpadas substituídas corretamente.")
    with col_sol:
        st.markdown("#### ☀️ Renovável: sistema fotovoltaico")
        st.write(f"Geração calculada: **{num(r['solar_geracao_potencial_kwh_mes'])} kWh/mês**. "
                 f"Parcela potencialmente compensável na iluminação: **{num(r['solar_compensacao_potencial_kwh_mes'])} kWh/mês**.")
        st.write(f"Investimento didático: **{dinheiro(r['solar_investimento_rs'])}**. "
                 f"Retorno simples favorável (não real): **{num(r['solar_retorno_teto_meses'])} meses**.")
        st.write("**Viabilidade:** requer telhado/área, baixa sombra, conexão, projeto elétrico e investimento maior.")
        st.write("**Ambiental:** fonte renovável em operação; fabricação e descarte dos módulos/inversor têm impactos.")
    st.warning("O retorno solar exibido é apenas um LIMITE OTIMISTA baseado em tarifa integral e "
               "compensação integral da parcela estudada. Não representa faturamento real. "
               "NÃO some a economia LED à economia solar do cenário original: trocar por LED "
               "reduz o consumo que o sistema solar poderia compensar.")
    st.success("**Conclusão para o cenário didático:** priorizar a substituição por LED pelo menor "
               "investimento e retorno estimado mais curto; avaliar solar após estudar o consumo total "
               "do imóvel, a irradiação local, as regras da distribuidora e orçamentos reais.")

with aba_assistente:
    st.subheader("Pergunte ao assistente sobre energia")
    st.caption("Respostas fundamentadas nos cálculos atualizados da barra lateral; sem coleta de dados pessoais.")
    perguntas = ["Quanto gasto com iluminação?", "Quanto economizo trocando por LED?",
                 "Energia solar vale a pena?", "Compare as alternativas", "Quais são as limitações?", "Quais são as fontes?"]
    col_q1, col_q2 = st.columns(2)
    for i, pergunta in enumerate(perguntas):
        with (col_q1 if i % 2 == 0 else col_q2):
            if st.button(pergunta, use_container_width=True, key=f"ex_{i}"):
                st.session_state["ultima_pergunta"] = pergunta
    texto = st.chat_input("Ex.: quanto custa usar as lâmpadas cinco horas por dia?")
    if texto:
        st.session_state["ultima_pergunta"] = texto
    if "ultima_pergunta" in st.session_state:
        with st.chat_message("user"):
            st.write(st.session_state["ultima_pergunta"])
        with st.chat_message("assistant"):
            st.markdown(responder_pergunta(st.session_state["ultima_pergunta"], p))
    else:
        st.write("Escolha uma pergunta para ver a resposta e seus cálculos.")

with aba_cin:
    st.subheader("Demonstração de integração com o Citizen Assist AI")
    st.caption("Demonstração contextual do Citizen Assist AI voltada à orientação documental. "
               "O módulo de energia constitui a contribuição específica da disciplina SERS.")
    st.write("O assistente também pode orientar, de forma preliminar, sobre três condições "
             "de conferência antes do atendimento da primeira via da CIN.")
    a = st.checkbox("Já confirmei o agendamento necessário")
    b = st.checkbox("Consigo informar o número do CPF ou tenho documento com o número")
    c = st.checkbox("Tenho a certidão aplicável ao meu estado civil")
    if st.button("Conferir condições", type="primary"):
        resposta = verificar_cin(a,b,c)
        if resposta["s"]:
            st.warning("Há itens que você deve conferir antes do atendimento:")
            for pendencia in resposta["pendencias"]:
                st.write("•",pendencia)
        else:
            st.success("As três condições preliminares foram confirmadas. "
                       "Consulte também todos os demais requisitos oficiais.")
    st.link_button("Consultar serviço oficial da CIN (SP)",
                   "https://www.poupatempo.sp.gov.br/carta/D97C3844-A2D9-4C9E-B364-CB4FEB26A1FB")
    st.caption("Esta verificação não acessa sistemas públicos, não valida documentos e não garante atendimento.")

with aba_referencias:
    st.subheader("Método, fontes e limitações")
    st.latex(r'E_{consumo} (kWh/mês) = \frac{n\times P(W)\times h(dia)\times d(mês)}{1000}')
    st.latex(r'E_{solar} (kWh/mês) = P_{FV}(kWp)\times HSP(h/dia)\times PR\times d(mês)')
    st.write("**Fontes verificáveis para conceitos e regras:**")
    st.markdown(f"- [Ministério de Minas e Energia — potência e consumo]({FONTES['mme']})")
    st.markdown(f"- [Department of Energy — LED e comparação por lúmens]({FONTES['doe']})")
    st.markdown(f"- [CRESESB/SunData — consultar irradiação local]({FONTES['cresesb']})")
    st.markdown(f"- [ANEEL — micro e minigeração distribuída]({FONTES['aneel']})")
    st.markdown(f"- [Lei nº 14.300/2022]({FONTES['lei14300']})")
    st.write("**Premissas não oficiais:** tarifas, preços e custos, horas de uso, potência do sistema, "
             "horas de sol pleno e PR são parâmetros do exemplo — NÃO foram extraídos como observações "
             "diretas dessas fontes.")
    st.write("**O modelo ignora:** impostos, custos fixos, fatores horários e tarifas específicas, "
             "economia regulatória parcial, degradação dos módulos, manutenção, juros, financiamento, "
             "desconto financeiro, vida útil, variação mensal do clima e restrições de telhado.")
    st.caption("Ver detalhes completos em documentacao/ANALISE_TECNICA.md e dados/premissas.csv.")
