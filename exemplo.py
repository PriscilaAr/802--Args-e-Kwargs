def item(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

item(nome='Priscila', id='1')