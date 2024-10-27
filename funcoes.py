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