def formata_faturamento(faturamento):

    faturamento_final = [valor for valor in faturamento if valor > 0]

    return faturamento_final

def maior_faturamento(faturamento):
    maior = faturamento[0]

    for valor in faturamento:
        if valor > maior:
            maior = valor

    return maior

def menor_faturamento(faturamento):
    menor = faturamento[0]

    for valor in faturamento:
        if valor < menor:
            menor = valor

    return menor

def media_faturamento(faturamento):
     media_mensal = sum(faturamento) / len(faturamento)
     print(media_mensal)
     dias_acima_da_media = len([valor for valor in faturamento if valor > media_mensal])
     return dias_acima_da_media

def main():
    faturamento_diario = [
    0, 1500, 2200, 0, 5000, 0, 3400, 0, 2500, 2700, 0, 2100, 3200, 0, 
    0, 2900, 0, 4300, 1200, 0, 0, 2000, 500, 0, 0, 4800, 0, 0, 0, 3200, 0
]
    faturamento_diario = formata_faturamento(faturamento_diario)
    maior_valor = maior_faturamento(faturamento_diario)
    menor_valor = menor_faturamento(faturamento_diario)
    dias_acima_media = media_faturamento(faturamento_diario)

    print(f"Menor faturamento: {menor_valor}")
    print(f"Maior faturamento: {maior_valor}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")


main()