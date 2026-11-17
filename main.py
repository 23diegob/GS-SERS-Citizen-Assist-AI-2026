"""Interface de linha de comando para consulta ao Citizen Assist AI."""
from energia import Parametros, calcular
from assistente import responder_pergunta, verificar_cin


def consulta_cin():
    print("\nCIN — conferência preliminar (SIM ou NAO)")
    perguntas = ["Confirmou agendamento?", "Possui informação do CPF?", "Possui certidão aplicável?"]
    respostas = []
    for pergunta in perguntas:
        while True:
            resposta = input(pergunta + " [s/n]: ").strip().lower()
            if resposta in ("s", "sim", "n", "nao", "não"):
                respostas.append(resposta in ("s", "sim"))
                break
            print("Entrada inválida. Digite s ou n.")
    r = verificar_cin(*respostas)
    if r["s"]:
        print("Pendências a conferir:")
        for pend in r["pendencias"]:
            print("  - " + pend)
    else:
        print("As três condições iniciais foram confirmadas; consulte todas as demais exigências.")
    print("Fonte: https://www.poupatempo.sp.gov.br/carta/D97C3844-A2D9-4C9E-B364-CB4FEB26A1FB")
    print("A ferramenta não verifica documentos nem garante atendimento.")


def consulta_energia():
    p = Parametros()
    while True:
        print("\nMÓDULO SERS — cenário didático: 10 lâmpadas antigas de 60W por 5h/dia.")
        pergunta = input("Pergunte sobre energia (ou ENTER para voltar): ").strip()
        if not pergunta:
            break
        print("\n" + responder_pergunta(pergunta, p).replace('**', ''))


def resumo_energia():
    r = calcular(Parametros())
    print("\nCOMPARAÇÃO DE ENERGIA: ILUMINAÇÃO RESIDENCIAL")
    print(f"Situação atual: {r['referencia_kwh_mes']:.1f} kWh/mês")
    print(f"LED: {r['led_kwh_mes']:.1f} kWh/mês | economia {r['led_economia_rs_mes']:.2f} R$/mês")
    print(f"Solar (estimativa): {r['solar_geracao_potencial_kwh_mes']:.1f} kWh/mês")
    print(f"Solar: teto teórico de economia {r['solar_economia_teto_rs_mes']:.2f} R$/mês")
    print("Tarifa, custos e insolação são HIPÓTESES editáveis — não são medições locais.")
    print("A energia solar pode reduzir gastos, mas sua economia financeira não é garantida.")
    print("Leia as referências e limitações em documentacao/ANALISE_TECNICA.md.")


def main():
    while True:
        print("\n=== CITIZEN ASSIST AI | GS 2026.2 ===")
        print("1 - Orientação preliminar CIN (demonstração)")
        print("2 - Análise técnica de energia (SERS)")
        print("3 - Perguntar ao assistente de energia")
        print("0 - Sair")
        op = input("Escolha: ").strip()
        if op == "0":
            print("Encerrado.")
            return
        if op == "1":
            consulta_cin()
        elif op == "2":
            resumo_energia()
        elif op == "3":
            consulta_energia()
        else:
            print("Opção inválida; escolha 0, 1, 2 ou 3.")


if __name__ == "__main__":
    main()
