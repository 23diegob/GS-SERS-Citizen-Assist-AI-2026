"""Respostas em linguagem natural a partir de cálculos reproduzíveis — sem API paga."""
import unicodedata
from energia import FONTES, Parametros, calcular


def normalizar(texto: str) -> str:
    sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', texto.lower()) if unicodedata.category(c) != 'Mn')
    return ' '.join(sem_acentos.strip().split())


def _moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def _numero(valor: float, casas: int = 1) -> str:
    return f"{valor:,.{casas}f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def responder_pergunta(pergunta: str, p: Parametros = Parametros()) -> str:
    dados = calcular(p)
    t = normalizar(pergunta)
    if not t:
        return "Digite uma dúvida como: 'Quanto gasto?', 'Vale trocar por LED?' ou 'Energia solar vale a pena?'."

    limite = "Valores simulados, não são promessas de economia ou valores reais de fatura."
    if any(termo in t for termo in ("fonte", "referencia", "onde tirou", "confiavel")):
        return (
            "**Referências utilizadas:**\n"
            f"- MME (potência e kWh): {FONTES['mme']}\n"
            f"- DOE (lâmpadas e luminosidade equivalente): {FONTES['doe']}\n"
            f"- CRESESB/SunData (consultar irradiação local): {FONTES['cresesb']}\n"
            f"- ANEEL (regras e custos de geração distribuída): {FONTES['aneel']}\n"
            "Os preços, a tarifa, a irradiação e o rendimento são premissas didáticas editáveis, não dados dessas fontes."
        )
    if any(termo in t for termo in ("ambient", "sustent", "carbono", "polu")):
        return (
            f"A troca para LED reduz o consumo estudado em **{_numero(dados['led_reducao_kwh_mes'])} kWh/mês**. "
            "Isso reduz a necessidade de geração elétrica. A geração solar utiliza fonte renovável, mas "
            "painéis e inversores exigem materiais, fabricação e descarte responsável. Não estimamos "
            "CO₂ evitado porque não foi adotado um fator de emissão local verificado. "
            f"Base de consumo: {FONTES['mme']}. {limite}"
        )
    if any(termo in t for termo in ("limita", "garant", "cuidado", "noite", "chuva", "bateria")):
        return (
            "**Limitações:** o exemplo pressupõe iluminação equivalente em lúmens, mesmas horas de uso, "
            "preços informados e instalações compatíveis. Sombra, orientação do telhado, clima e "
            "equipamentos influenciam a energia solar. Em sistemas conectados à rede, solar não "
            "substitui automaticamente o fornecimento noturno em falta de energia; baterias não "
            "estão incluídas. O valor da conta também inclui itens não compensáveis. "
            f"Confira: {FONTES['aneel']}. {limite}"
        )
    if any(termo in t for termo in ("compar", "melhor", "alternativa", "recomend", "qual escol")):
        return (
            f"Para {dados['servico'].lower()}, o cenário atual consome **{_numero(dados['referencia_kwh_mes'])} kWh/mês**. "
            f"**LED:** reduz **{_numero(dados['led_reducao_kwh_mes'])} kWh/mês** e economizaria "
            f"**{_moeda(dados['led_economia_rs_mes'])}/mês** na parcela variável simulada; "
            f"custo das lâmpadas **{_moeda(dados['led_investimento_rs'])}**. "
            f"**Solar fotovoltaica:** geração ilustrativa de **{_numero(dados['solar_geracao_potencial_kwh_mes'])} kWh/mês**, "
            f"com economia financeira teórica de até **{_moeda(dados['solar_economia_teto_rs_mes'])}/mês**, "
            f"investimento suposto de **{_moeda(dados['solar_investimento_rs'])}**. "
            "**Recomendação neste cenário:** começar pela eficiência LED, de investimento menor; "
            "avaliar solar somente após verificar consumo total da residência, telhado e regras da distribuidora. "
            f"{limite} Fontes: {FONTES['mme']} | {FONTES['aneel']}"
        )
    if any(termo in t for termo in ("solar", "painel", "fotovolta", "renovavel", "sol pleno", "irradi")):
        return (
            f"Um sistema didático de **{_numero(p.potencia_solar_kwp, 2)} kWp**, com "
            f"**{_numero(p.sol_pleno_h_dia)} h de sol pleno/dia** e "
            f"**{_numero(p.desempenho_solar * 100, 0)}% de desempenho**, "
            f"produziria aproximadamente **{_numero(dados['solar_geracao_potencial_kwh_mes'])} kWh/mês**. "
            "Esse valor não equivale à economia garantida na fatura. "
            f"O teto teórico para o serviço estudado seria **{_moeda(dados['solar_economia_teto_rs_mes'])}/mês**. "
            f"Consulte irradiação por coordenadas em {FONTES['cresesb']} e regras locais em {FONTES['aneel']}. {limite}"
        )
    if any(termo in t for termo in ("led", "lampada", "trocar", "economiz", "reduzir")):
        return (
            f"Ao substituir **{p.lampadas} lâmpadas de {p.potencia_atual_w:g} W** por "
            f"**{p.lampadas} LED de {p.potencia_led_w:g} W** mantendo o uso, o consumo cairia "
            f"de **{_numero(dados['referencia_kwh_mes'])}** para **{_numero(dados['led_kwh_mes'])} kWh/mês** "
            f"(economia de **{_numero(dados['led_reducao_kwh_mes'])} kWh/mês**, "
            f"ou **{_numero(dados['led_reducao_percentual'])}%**). "
            f"Economia de **{_moeda(dados['led_economia_rs_mes'])}/mês** na parcela variável simulada; "
            f"investimento **{_moeda(dados['led_investimento_rs'])}** e retorno simples **{_numero(dados['led_retorno_meses'])} meses**. "
            f"Confirme luminosidade equivalente em lúmens. Fonte: {FONTES['doe']}. {limite}"
        )
    if any(termo in t for termo in ("gasto", "consumo", "conta", "kwh", "potencia", "quanto custa")):
        return (
            f"O consumo das lâmpadas no cenário atual é **{_numero(dados['referencia_kwh_mes'])} kWh/mês**, "
            f"calculado como {p.lampadas} × {p.potencia_atual_w:g} W × {p.horas_dia:g} h/dia × "
            f"{p.dias_mes} dias ÷ 1000. Com tarifa didática de {_moeda(p.tarifa_rs_kwh)}/kWh, "
            f"essa iluminação representa **{_moeda(dados['referencia_custo_rs_mes'])}/mês** na "
            "parcela de energia simulada — não é a conta inteira. "
            f"Fórmula: {FONTES['mme']}. {limite}"
        )
    return (
        "Eu posso ajudar com **consumo de energia**, **troca por LED**, **energia solar**, "
        "**comparação das alternativas**, **impactos ambientais**, **fontes** e **limitações**. "
        "Faça uma dessas perguntas; os cálculos são atualizados conforme os parâmetros informados."
    )


def verificar_cin(agendamento: bool, cpf_confirmado: bool, certidao_confirmada: bool) -> dict:
    """Demonstração da regra lógica do projeto Computer Science; sem acesso a bases oficiais."""
    pendencias = []
    if not agendamento:
        pendencias.append("verificar a necessidade de agendamento no canal oficial")
    if not cpf_confirmado:
        pendencias.append("conferir a informação do número do CPF")
    if not certidao_confirmada:
        pendencias.append("conferir a certidão compatível com o estado civil")
    return {"s": int(not (agendamento and cpf_confirmado and certidao_confirmada)), "pendencias": pendencias}
