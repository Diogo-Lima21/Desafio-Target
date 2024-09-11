def calcular_percentual_faturamento(faturamento_inicial):

    faturamento_total = sum(faturamento_inicial.values())

    faturamento_percentual_estado = {}
    for estado, faturamento in faturamento_inicial.items():
        percentual = (faturamento / faturamento_total) * 100
        faturamento_percentual_estado[estado] = percentual
    
    return faturamento_percentual_estado




def main():
    faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

    # Calcula o percentual de cada estado
    percentual_resultado = calcular_percentual_faturamento(faturamento_por_estado)

    # Exibe o resultado
    for estado, percentual in percentual_resultado.items():
        print(f"{estado}: {percentual:.2f}%")

main()