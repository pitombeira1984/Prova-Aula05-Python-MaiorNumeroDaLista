
def MaiorNumeroDaLista():
    from functools import reduce
    lista_numeros = [20,30,2]
    maiorNumero = reduce(lambda x, y: x if x > y else y, lista_numeros)
    return maiorNumero
print(f'O maior número da lista é: {MaiorNumeroDaLista()}')
    