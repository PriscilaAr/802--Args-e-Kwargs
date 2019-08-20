def imprimir_qualquer_coisa(*args):
    for number, item in enumerate(args):
        print(str(number + '.' + item))

imprimir_qualquer_coisa('Maça', 'Natação', 'Pastel')