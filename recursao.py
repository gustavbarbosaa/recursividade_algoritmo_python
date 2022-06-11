import random

criarLista = random.sample(range(1001), 100)
print(criarLista)

lista = sorted(criarLista)
print(lista)

sortearValor = random.choice(lista)

for i in range(len(lista)):
    print(f'Posição -> {i}: {lista[i]}')


def salvarLista(objeto):
    with open('listaFull.txt', 'w') as arquivo:
        for x in objeto:
            arquivo.write('[' + str(x) + ']')
        arquivo.close()


salvarLista(lista)


def acharInidice(listaOrdenada, posInicial, posFinal, valorSorteado):
    condicao = posInicial <= posFinal

    while condicao:

        meiolista = (posInicial + posFinal) // 2

        if listaOrdenada[meiolista] < valorSorteado:
            return acharInidice(listaOrdenada, meiolista + 1, posFinal, valorSorteado)
        elif listaOrdenada[meiolista] > valorSorteado:
            return acharInidice(listaOrdenada, posInicial, meiolista - 1, valorSorteado)
        else:
            return f'O número {valorSorteado} está no indice -> {meiolista}\n'

    return 'Valor não encontrado'


def salvarRes(objeto):
    with open('resultado.txt', 'w') as arquivo:
        for x in objeto:
            arquivo.write(str(x))
        arquivo.close()


print(acharInidice(lista, 0, len(lista) - 1, sortearValor))
salvarRes(acharInidice(lista, 0, len(lista) - 1, sortearValor))
