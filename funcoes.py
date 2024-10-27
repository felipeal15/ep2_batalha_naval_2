def define_posicoes(linha, coluna, ori, tamanho):
    posicoes = []
    for i in range(tamanho):
        if ori == "vertical":
            posicoes.append([linha + i, coluna])
        elif ori == "horizontal":
            posicoes.append([linha, coluna + i])
    return posicoes


def preenche_frota(frota, navio, linha, coluna, ori, tamanho):
    posicao = define_posicoes(linha, coluna, ori, tamanho)
    if navio not in frota:
        frota[navio] = []
    frota[navio].append(posicao)
    
    return frota

def faz_jogada(tab, linha, coluna):
    if tab[linha][coluna] == 1:
        tab[linha][coluna] = 'X'
    elif tab[linha][coluna] == 0:
        tab[linha][coluna] = '-'
    return tab

def posiciona_frota(f):
    tab = []
    for lin in range(10):
        linha = []
        for col in range(10):
            linha.append(0)
        tab.append(linha)
    for ps in f.values():
        for pos in ps:
            for linha, colu in pos:
                tab[linha][colu] = 1
    return tab