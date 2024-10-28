# pylint: disable = C0103, C0114, C0116, C0410, W0603, W0621

# Importa as bibliotecas necessárias para o cliente
import os, time


# Função para limpar a tela
def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Menu inicial do cliente
def menu():
    clean_screen()
    print("Bem-vindo ao Gomoku!\n")
    print("1 - Criar uma nova Sala")
    print("2 - Entrar em uma Sala já existente")
    print("3 - Sair")

    return input("\nEscolha uma opção acima: ")


# Função para executar o jogo
def execute(sala_id, jogador, proxy):
    # flag de espera
    wait = False

    while True:
        # obtem o jogador atual
        jogador_atual = proxy.obter_jogador_atual(sala_id)

        # se for a vez do jogador, ele faz a sua jogada
        if jogador_atual == jogador:
            wait = False

            # mostra o tabuleiro atual para o jogador fazer a sua jogada
            clean_screen()
            print(f"Sua vez de jogar, jogador {jogador}!")
            print("Sala: " + sala_id + "\n")
            print(proxy.mostrar_tabuleiro(sala_id))

            # pede a posição para jogar, e efetua a jogada
            x, y = [
                (int(coord.strip()) - 1)
                for coord in input("\nDigite a posição (x, y) para jogar: ").split(",")
            ]
            res = proxy.jogar(sala_id, x, y, jogador)

            # mostra a mensagem após a jogada, se foi válida, inválida ou se o jogador ganhou
            clean_screen()
            print(res)
            time.sleep(2)

            # se o jogador ganhou, mostra o tabuleiro final
            if "ganhou" in res:
                print("\nTabuleiro final:")
                print(proxy.mostrar_tabuleiro(sala_id))
                break

        # se não for a vez do jogador, ele espera a sua vez
        else:

            # verifica se o outro jogador ganhou
            if proxy.obter_ganhador(sala_id) != "":
                clean_screen()
                print(f"Jogador {proxy.obter_ganhador(sala_id)} ganhou!")
                print("\nTabuleiro final:")

                # se ganhou mostra a mensagem, o tabuleiro final e finaliza a sala
                print(proxy.mostrar_tabuleiro(sala_id))
                proxy.finalizar_sala(sala_id)
                break

            # mostra a mensagem de espera e o tabuleiro atual
            if not wait:
                clean_screen()
                print("Aguarde o outro jogador realizar a jogada!\n")

                print("\nTabuleiro atual:")
                print(proxy.mostrar_tabuleiro(sala_id))
                wait = True
