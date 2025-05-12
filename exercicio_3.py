import json

with open("dados.json", "r") as f:
    dados = json.load(f)

valores = [d["valor"] for d in dados if d["valor"] > 0]
media = sum(valores) / len(valores)
maior = max(valores)
menor = min(valores)
dias_acima_media = sum(1 for v in valores if v > media)

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Dias com faturamento acima da média:", dias_acima_media)
