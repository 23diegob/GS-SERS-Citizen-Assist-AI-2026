import unittest
from energia import Parametros, calcular
from assistente import normalizar, responder_pergunta, verificar_cin


class TesteCalculosEnergeticos(unittest.TestCase):
    def setUp(self):
        self.p = Parametros()
        self.r = calcular(self.p)

    def test_consumo_base(self):
        self.assertAlmostEqual(self.r["referencia_kwh_mes"], 90)
        self.assertAlmostEqual(self.r["referencia_custo_rs_mes"], 81)

    def test_led(self):
        self.assertAlmostEqual(self.r["led_kwh_mes"], 13.5)
        self.assertAlmostEqual(self.r["led_reducao_kwh_mes"], 76.5)
        self.assertAlmostEqual(self.r["led_reducao_percentual"], 85)
        self.assertAlmostEqual(self.r["led_economia_rs_mes"], 68.85)
        self.assertAlmostEqual(self.r["led_investimento_rs"], 150)
        self.assertAlmostEqual(self.r["led_retorno_meses"], 150/68.85)

    def test_solar(self):
        self.assertAlmostEqual(self.r["solar_geracao_potencial_kwh_mes"], 90)
        self.assertAlmostEqual(self.r["solar_economia_teto_rs_mes"], 81)
        self.assertAlmostEqual(self.r["solar_retorno_teto_meses"], 5000/81)

    def test_solar_compensacao_limitada_ao_servico(self):
        p = Parametros(potencia_solar_kwp=5)
        r = calcular(p)
        self.assertEqual(r["solar_compensacao_potencial_kwh_mes"], 90)
        self.assertEqual(r["solar_economia_teto_rs_mes"], 81)
        self.assertGreater(r["solar_excedente_fora_escopo_kwh_mes"], 0)

    def test_cenarios_escalonam(self):
        p = Parametros(lampadas=5, horas_dia=2, dias_mes=20)
        r = calcular(p)
        self.assertAlmostEqual(r["referencia_kwh_mes"], 12)
        self.assertAlmostEqual(r["led_kwh_mes"], 1.8)

    def test_rejeita_potencias_incompativeis(self):
        with self.assertRaises(ValueError): calcular(Parametros(potencia_led_w=60))

    def test_rejeita_uso_exagerado(self):
        with self.assertRaises(ValueError): calcular(Parametros(horas_dia=25))

    def test_rejeita_valor_nao_finito(self):
        with self.assertRaises(ValueError): calcular(Parametros(tarifa_rs_kwh=float('nan')))

    def test_rejeita_quantidade_fracionada(self):
        with self.assertRaises(ValueError): calcular(Parametros(lampadas=3.3))


class TesteRespostas(unittest.TestCase):
    def test_normalizacao(self):
        self.assertEqual(normalizar('  LÂMPADAS  SOLARES  '), 'lampadas solares')

    def test_pergunta_led_contém_resultado(self):
        t = responder_pergunta('Quero trocar por LED')
        self.assertIn('76,5', t)
        self.assertIn('energy.gov', t)

    def test_pergunta_solar_tem_ressalva(self):
        t = responder_pergunta('Vale a pena usar energia solar?')
        self.assertIn('não equivale', t)
        self.assertIn('aneel', t)

    def test_pergunta_gasto(self):
        t = responder_pergunta('Quanto gasto de energia?')
        self.assertIn('90,0', t)
        self.assertIn('81,00', t)

    def test_resposta_comparacao_usa_duas_alternativas(self):
        t = responder_pergunta('Compare as alternativas')
        self.assertIn('LED:', t)
        self.assertIn('Solar fotovoltaica:', t)

    def test_entrada_desconhecida(self):
        self.assertIn('posso ajudar', responder_pergunta('Oi, tudo bem?'))

    def test_cin_8_combinacoes(self):
        for a in (False,True):
            for b in (False,True):
                for c in (False,True):
                    r=verificar_cin(a,b,c)
                    self.assertEqual(r["s"], 0 if a and b and c else 1)
                    self.assertEqual(len(r["pendencias"]), 3-int(a)-int(b)-int(c))


if __name__ == '__main__':
    unittest.main()
