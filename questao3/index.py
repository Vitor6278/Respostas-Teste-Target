import json

faturamento_json = '''
{
    "2024-08-01": 1000,
    "2024-08-02": 1500,
    "2024-08-03": 0,
    "2024-08-04": 2000,
    "2024-08-05": 1700
}
'''

faturamento_diario = json.loads(faturamento_json)
valores = list(faturamento_diario.values())
total_faturamento = sum(valores)
dias_com_faturamento = len(valores) 
media_mensal = total_faturamento / dias_com_faturamento

menor_faturamento = min(valores)
maior_faturamento = max(valores)
dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")