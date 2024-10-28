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

def afundados(frota, tabuleiro):
    navios_afundados = 0

    for posicoes in frota.values():
        for posicao in posicoes:
            if all(tabuleiro[linha][coluna] == 'X' for linha, coluna in posicao):
                navios_afundados += 1

    return navios_afundados


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_novas = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao_nova in posicoes_novas:
        if not (0 <= posicao_nova[0] < 10 and 0 <= posicao_nova[1] < 10):
            return False
        
    for tipos_navios in frota.values():
        for navio in tipos_navios:
            if any(posicao in posicoes_novas for posicao in navio):
                return False
                
    return True