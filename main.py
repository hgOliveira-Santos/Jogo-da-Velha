from lógica import *

if __name__ == "__main__":

    def main():
        mensagem = "Jogo da Velha"
        print(f"{mensagem: ^30}\n\n")

        primeiraLinha = " 1 | 2 | 3 "
        segundaLinha = " 4 | 5 | 6 "
        terceiraLinha = " 7 | 8 | 9 " 

        print("Essas são as posições do tabuleiro: ")
        imprimir_tabuleiro(primeiraLinha, segundaLinha, terceiraLinha)

        jogador1 = input("Nome do jogador 1 [x]: ")
        jogador2 = input("Nome do jogador 2 [o]: ")

        primeiraLinha = f" {TABULEIRO[0][0]} | {TABULEIRO[0][1]} | {TABULEIRO[0][2]} "
        segundaLinha = f" {TABULEIRO[1][0]} | {TABULEIRO[1][1]} | {TABULEIRO[1][2]} "
        terceiraLinha = f" {TABULEIRO[2][0]} | {TABULEIRO[2][1]} | {TABULEIRO[2][2]} "

        imprimir_tabuleiro(primeiraLinha, segundaLinha, terceiraLinha)

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

    main()