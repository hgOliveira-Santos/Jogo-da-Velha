# Importando módulos necessários
import numpy as np
from lógica import *

def main():
    """
    Função principal que executa o jogo da velha.
    """
    # Mensagem inicial
    mensagem = "Jogo da Velha"
    print(f"{mensagem: ^30}\n\n")

    # Definindo as linhas iniciais do tabuleiro
    primeiraLinha = " 1 | 2 | 3 "
    segundaLinha = " 4 | 5 | 6 "
    terceiraLinha = " 7 | 8 | 9 " 

    # Exibindo as posições do tabuleiro
    print("Essas são as posições do tabuleiro: ")
    imprimir_tabuleiro(primeiraLinha, segundaLinha, terceiraLinha)

    # Solicitando nomes dos jogadores
    jogador1 = input("Nome do jogador 1 [x]: ")
    jogador2 = input("Nome do jogador 2 [o]: ")

    # Atualizando as linhas do tabuleiro com o estado inicial
    primeiraLinha = f" {TABULEIRO[0][0]} | {TABULEIRO[0][1]} | {TABULEIRO[0][2]} "
    segundaLinha = f" {TABULEIRO[1][0]} | {TABULEIRO[1][1]} | {TABULEIRO[1][2]} "
    terceiraLinha = f" {TABULEIRO[2][0]} | {TABULEIRO[2][1]} | {TABULEIRO[2][2]} "

    # Exibindo o tabuleiro inicializado
    imprimir_tabuleiro(primeiraLinha, segundaLinha, terceiraLinha)

    # Loop principal do jogo
    while True:
        # Jogador 1 realiza uma jogada
        jogada(jogador1, "x", primeiraLinha, segundaLinha, terceiraLinha)

        # Verificar se o jogador 1 venceu
        if checkagem_vencedor():
            print(f"O jogador {jogador1} venceu!\n")
            break

        # Verificar empate
        if fim_de_jogo():
            print("Fim de jogo!\n")
            print("O jogo terminou empatado!\n")
            break

        # Jogador 2 realiza uma jogada
        jogada(jogador2, "o", primeiraLinha, segundaLinha, terceiraLinha)

        # Verificar se o jogador 2 venceu
        if checkagem_vencedor():
            print(f"O jogador {jogador2} venceu!\n")
            break

        # Verificar empate
        if fim_de_jogo():
            print("Fim de jogo!\n")
            print("O jogo terminou empatado!\n")
            break

# Chamada para executar a função principal do jogo
if __name__ == "__main__":
    main()
