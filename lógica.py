import numpy as np

# Variável global TABULEIRO
TABULEIRO = np.full((3, 3), ' ')

def jogada(jogador, símbolo, linha1, linha2, linha3):
    global TABULEIRO  # Indicando que estamos referenciando a variável global TABULEIRO

    idx1 = {"1": 0,
            "2": 0,
            "3": 0,
            "4": 1,
            "5": 1,
            "6": 1, 
            "7": 2,
            "8": 2, 
            "9": 2}
    
    idx2 = {"1": 0,
            "2": 1,
            "3": 2,
            "4": 0,
            "5": 1,
            "6": 2, 
            "7": 0,
            "8": 1, 
            "9": 2}
    
    while True:
        try:
            posição = int(input(f"{jogador} - Digite a posição: "))
            posição = str(posição)
            if posição not in idx1 and posição not in idx2:
                raise ValueError
        except ValueError:
            print("\nVocê deve digitar um número de 1 a 9!\n")
            continue
        
        if posição == "1":
            if TABULEIRO[idx1["1"]][idx2["1"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["1"]][idx2["1"]] = símbolo

        elif posição == "2":
            if TABULEIRO[idx1["2"]][idx2["2"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["2"]][idx2["2"]] = símbolo

        elif posição == "3":
            if TABULEIRO[idx1["3"]][idx2["3"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["3"]][idx2["3"]] = símbolo

        elif posição == "4":
            if TABULEIRO[idx1["4"]][idx2["4"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["4"]][idx2["4"]] = símbolo

        elif posição == "5":
            if TABULEIRO[idx1["5"]][idx2["5"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["5"]][idx2["5"]] = símbolo

        elif posição == "6":
            if TABULEIRO[idx1["6"]][idx2["6"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["6"]][idx2["6"]] = símbolo

        elif posição == "7":
            if TABULEIRO[idx1["7"]][idx2["7"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["7"]][idx2["7"]] = símbolo

        elif posição == "8":
            if TABULEIRO[idx1["8"]][idx2["8"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["8"]][idx2["8"]] = símbolo

        elif posição == "9":
            if TABULEIRO[idx1["9"]][idx2["9"]] in ["x", "o"]:
                print("\nPosição já preenchida!\n")
                continue
            else:
                TABULEIRO[idx1["9"]][idx2["9"]] = símbolo
        
        linha1, linha2, linha3 = atualiza_tabuleiro(linha1, linha2, linha3)
        imprimir_tabuleiro(linha1, linha2, linha3)
        
        break

def checkagem_vencedor():
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
    
    # Caso nenhuma linha, coluna ou diagonal possuam elementos iguais, a função retornará False indicando que não há vencedor
    return False

def fim_de_jogo():
    for linha in TABULEIRO:
        for elemento in linha:
            if elemento == ' ':
                return False
    return True

def imprimir_tabuleiro(ln1, ln2, ln3):
    quebra = "---+---+---"
    print()
    print(ln1)
    print(quebra)
    print(ln2)
    print(quebra)
    print(ln3)
    print()

def atualiza_tabuleiro(ln1, ln2, ln3):
    ln1 = f" {TABULEIRO[0][0]} | {TABULEIRO[0][1]} | {TABULEIRO[0][2]} "
    ln2 = f" {TABULEIRO[1][0]} | {TABULEIRO[1][1]} | {TABULEIRO[1][2]} "
    ln3 = f" {TABULEIRO[2][0]} | {TABULEIRO[2][1]} | {TABULEIRO[2][2]} "
    return ln1, ln2, ln3