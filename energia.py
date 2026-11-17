"""Núcleo de cálculos do módulo SERS — Citizen Assist AI.

Nenhum preço, irradiação ou custo inicial aqui é uma cotação real.
São parâmetros ilustrativos, ajustáveis na simulação, sem correspondência garantida com tarifas ou orçamentos.
"""
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass(frozen=True)
class Parametros:
    lampadas: int = 10
    potencia_atual_w: float = 60.0
    potencia_led_w: float = 9.0
    horas_dia: float = 5.0
    dias_mes: int = 30
    tarifa_rs_kwh: float = 0.90
    preco_led_unit_rs: float = 15.0
    potencia_solar_kwp: float = 1.0
    sol_pleno_h_dia: float = 4.0
    desempenho_solar: float = 0.75
    custo_solar_rs: float = 5000.0

    def validar(self) -> None:
        if not isinstance(self.lampadas, int) or isinstance(self.lampadas, bool) or self.lampadas <= 0:
            raise ValueError("A quantidade de lâmpadas deve ser um inteiro positivo.")
        if not isinstance(self.dias_mes, int) or isinstance(self.dias_mes, bool) or not 1 <= self.dias_mes <= 31:
            raise ValueError("Os dias do mês devem estar entre 1 e 31.")
        for nome in (
            "potencia_atual_w", "potencia_led_w", "horas_dia", "tarifa_rs_kwh",
            "preco_led_unit_rs", "potencia_solar_kwp", "sol_pleno_h_dia", "custo_solar_rs"
        ):
            valor = getattr(self, nome)
            if not isinstance(valor, (int, float)) or not (0 < valor < float('inf')):
                raise ValueError(f"{nome} deve ser um valor positivo e finito.")
        if self.potencia_led_w >= self.potencia_atual_w:
            raise ValueError("No cenário de eficiência, LED deve ter potência inferior à lâmpada atual.")
        if self.horas_dia > 24:
            raise ValueError("O uso não pode exceder 24 horas por dia.")
        if self.sol_pleno_h_dia > 24:
            raise ValueError("As horas equivalentes de sol pleno não podem exceder 24.")
        if not 0 < self.desempenho_solar <= 1:
            raise ValueError("O fator de desempenho solar deve estar entre 0 e 1.")


def _retorno_meses(investimento: float, economia_mensal: float) -> Optional[float]:
    return investimento / economia_mensal if economia_mensal > 0 else None


def calcular(p: Parametros) -> dict:
    """Compara alternativas para o MESMO serviço: horas de iluminação/mês.

    Solar simula a compensação EQUIVALENTE apenas da iluminação analisada;
    NÃO simula conta real, disponibilidade instantânea, autoconsumo ou SCEE.
    """
    p.validar()
    referencia_kwh = p.lampadas * p.potencia_atual_w * p.horas_dia * p.dias_mes / 1000
    led_kwh = p.lampadas * p.potencia_led_w * p.horas_dia * p.dias_mes / 1000
    led_poupanca_kwh = referencia_kwh - led_kwh
    geracao_solar_kwh = p.potencia_solar_kwp * p.sol_pleno_h_dia * p.desempenho_solar * p.dias_mes
    energia_potencial_compensavel_kwh = min(referencia_kwh, geracao_solar_kwh)
    # Modelo limite superior: não considera componentes fixas/não compensáveis.
    economia_solar_teto_rs = energia_potencial_compensavel_kwh * p.tarifa_rs_kwh
    economia_led_rs = led_poupanca_kwh * p.tarifa_rs_kwh
    custo_led_rs = p.lampadas * p.preco_led_unit_rs
    custo_referencia_rs = referencia_kwh * p.tarifa_rs_kwh
    custo_led_energia_rs = led_kwh * p.tarifa_rs_kwh
    pv_resto_led_kwh = min(led_kwh, geracao_solar_kwh)

    return {
        "cenario": asdict(p),
        "servico": f"Iluminação com {p.lampadas} pontos por {p.horas_dia:g} h/dia durante {p.dias_mes} dias",
        "referencia_kwh_mes": referencia_kwh,
        "referencia_custo_rs_mes": custo_referencia_rs,
        "led_kwh_mes": led_kwh,
        "led_reducao_kwh_mes": led_poupanca_kwh,
        "led_reducao_percentual": led_poupanca_kwh / referencia_kwh * 100,
        "led_economia_rs_mes": economia_led_rs,
        "led_custo_energia_rs_mes": custo_led_energia_rs,
        "led_investimento_rs": custo_led_rs,
        "led_retorno_meses": _retorno_meses(custo_led_rs, economia_led_rs),
        "solar_geracao_potencial_kwh_mes": geracao_solar_kwh,
        "solar_compensacao_potencial_kwh_mes": energia_potencial_compensavel_kwh,
        "solar_economia_teto_rs_mes": economia_solar_teto_rs,
        "solar_investimento_rs": p.custo_solar_rs,
        "solar_retorno_teto_meses": _retorno_meses(p.custo_solar_rs, economia_solar_teto_rs),
        "solar_excedente_fora_escopo_kwh_mes": max(0, geracao_solar_kwh - referencia_kwh),
        "solar_potencial_sobre_consumo_led_kwh_mes": pv_resto_led_kwh,
        "observacao_solar": (
            "A economia e o retorno solar são limites teóricos favoráveis, não previsão de fatura. "
            "Sistema conectado à rede não fornece energia à noite em caso de falta de luz sem "
            "armazenamento/inversor compatível. A conta depende do SCEE, tarifa, impostos, "
            "custo de disponibilidade, horários de consumo e conexão."
        ),
    }


FONTES = {
    "mme": "https://www.gov.br/mme/pt-br/assuntos/noticias/julho-26/potencia-e-consumo-de-energia-o-que-sao-e-como-impactam-na-conta-de-luz",
    "doe": "https://www.energy.gov/cmei/femp/purchasing-energy-efficient-light-bulbs",
    "cresesb": "https://www.cresesb.cepel.br/index.php?section=sundata",
    "aneel": "https://www.gov.br/aneel/pt-br/assuntos/geracao-distribuida",
    "lei14300": "https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm",
}
