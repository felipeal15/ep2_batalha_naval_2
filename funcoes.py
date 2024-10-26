def define_posicoes(linha, coluna, ori, tamanho):
    posicoes = []
    for i in range(tamanho):
        if ori == "vertical":
            posicoes.append([linha + i, coluna])
        elif ori == "horizontal":
            posicoes.append([linha, coluna + i])
    return posicoes