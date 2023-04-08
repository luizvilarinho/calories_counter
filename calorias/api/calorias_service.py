from decimal import Decimal

def calcular_calorias(data):
    print(data)
    alimento = data['alimento']
    quantidade = round(Decimal(data['quantidade']))

    alimento.cal = (round(Decimal(alimento.cal)) / 100) * quantidade
    alimento.p = (Decimal(alimento.p) / 100) * quantidade
    alimento.c = (Decimal(alimento.c) / 100) * quantidade
    alimento.g = (Decimal(alimento.g) / 100) * quantidade
    alimento.f = (Decimal(alimento.f) / 100) * quantidade

    return alimento
