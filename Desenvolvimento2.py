rodas = int(input("Digite a quantidade de rodas do veículo: "))
peso = float(input("Digite o peso bruto do veículo (em kg): "))
pessoas = int(input("Digite a quantidade de pessoas que o veículo acomoda: "))

print("-" * 40)

if rodas == 2 or rodas == 3:
    categoria = "A"
elif rodas >= 4:
    if pessoas > 8:
        categoria = "D"
    elif peso > 6000:
        categoria = "E"
    elif 3500 <= peso <= 6000:
        categoria = "C"
    elif pessoas <= 8 and peso <= 3500:
        categoria = "B"
    else:
        categoria = "Não foi possível determinar (dados fora dos padrões listados)"
else:
    categoria = "Inválida (Quantidade de rodas insuficiente)"

print(f"A melhor categoria de habilitação para este veículo é: {categoria}")
print("-" * 40)