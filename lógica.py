import numpy as np

# Variável global TABULEIRO
TABULEIRO = np.full((3, 3), ' ')

def jogada(jogador, símbolo, linha1, linha2, linha3):
    """
    Executa uma jogada para o jogador atual no jogo da velha.

    Parâmetros:
    jogador (str): Nome do jogador atual.
    símbolo (str): Símbolo ('x' ou 'o') do jogador atual.
    linha1 (str): String formatada da primeira linha do tabuleiro.
    linha2 (str): String formatada da segunda linha do tabuleiro.
    linha3 (str): String formatada da terceira linha do tabuleiro.

    Atualiza o tabuleiro global TABULEIRO com o símbolo na posição escolhida pelo jogador.
    Exibe o tabuleiro atualizado após a jogada.
    """
    global TABULEIRO  # Referenciando a variável global TABULEIRO

    # Dicionários para mapear posição do teclado numérico para índices da matriz TABULEIRO
    idx1 = {"1": 0, "2": 0, "3": 0, "4": 1, "5": 1, "6": 1, "7": 2, "8": 2, "9": 2}
    idx2 = {"1": 0, "2": 1, "3": 2, "4": 0, "5": 1, "6": 2, "7": 0, "8": 1, "9": 2}

    while True:
        try:
            posição = int(input(f"{jogador} - Digite a posição: "))
            posição = str(posição)
            if posição not in idx1 and posição not in idx2:
                raise ValueError
        except ValueError:
            print("\nVocê deve digitar um número de 1 a 9!\n")
            continue
        
        if posição in idx1 and posição in idx2:
            if TABULEIRO[idx1[posição]][idx2[posição]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1[posição]][idx2[posição]] = símbolo
        
        linha1, linha2, linha3 = atualiza_tabuleiro(linha1, linha2, linha3)
        imprimir_tabuleiro(linha1, linha2, linha3)
        
        break

def checkagem_vencedor():
    """
    Verifica se houve um vencedor no jogo da velha.

    Retorna:
    bool: True se houver um vencedor, False caso contrário.
    """
    # Verifica se as linhas possuem elementos iguais
    for linha in TABULEIRO:
        if linha[0] == linha[1] == linha[2] and linha[0] in ["x", "o"]:
            return True
    
    # Verifica se as colunas possuem elementos iguais
    for coluna in range(3):
        if TABULEIRO[0][coluna] == TABULEIRO[1][coluna] == TABULEIRO[2][coluna] and TABULEIRO[0][coluna] in ["x", "o"]:
            return True
    
    # Verifica se os elementos da diagonal principal são iguais
    if TABULEIRO[0][0] == TABULEIRO[1][1] == TABULEIRO[2][2] and TABULEIRO[0][0] in ["x", "o"]:
        return True
    
    # Verifica se os elementos da diagonal secundária são iguais
    if TABULEIRO[0][2] == TABULEIRO[1][1] == TABULEIRO[2][0] and TABULEIRO[0][2] in ["x", "o"]:
        return True
    
    # Caso nenhuma linha, coluna ou diagonal possuam elementos iguais, retorna False indicando que não há vencedor
    return False

def fim_de_jogo():
    """
    Verifica se o jogo da velha chegou ao fim (tabuleiro completo).

    Retorna:
    bool: True se o jogo terminou empatado, False caso contrário.
    """
    for linha in TABULEIRO:
        for elemento in linha:
            if elemento == ' ':
                return False
    return True

def imprimir_tabuleiro(ln1, ln2, ln3):
    """
    Imprime o estado atual do tabuleiro do jogo da velha.

    Parâmetros:
    ln1 (str): Primeira linha formatada do tabuleiro.
    ln2 (str): Segunda linha formatada do tabuleiro.
    ln3 (str): Terceira linha formatada do tabuleiro.
    """
    quebra = "---+---+---"
    print()
    print(ln1)
    print(quebra)
    print(ln2)
    print(quebra)
    print(ln3)
    print()

def atualiza_tabuleiro(ln1, ln2, ln3):
    """
    Atualiza as strings formatadas das linhas do tabuleiro com o estado atual do TABULEIRO.

    Parâmetros:
    ln1 (str): Primeira linha formatada do tabuleiro.
    ln2 (str): Segunda linha formatada do tabuleiro.
    ln3 (str): Terceira linha formatada do tabuleiro.

    Retorna:
    tuple: Tupla contendo as strings atualizadas das linhas do tabuleiro.
    """
    ln1 = f" {TABULEIRO[0][0]} | {TABULEIRO[0][1]} | {TABULEIRO[0][2]} "
    ln2 = f" {TABULEIRO[1][0]} | {TABULEIRO[1][1]} | {TABULEIRO[1][2]} "
    ln3 = f" {TABULEIRO[2][0]} | {TABULEIRO[2][1]} | {TABULEIRO[2][2]} "
    return ln1, ln2, ln3
