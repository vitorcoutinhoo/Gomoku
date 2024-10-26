# pylint: disable = C0103, C0114, C0116, C0410, W0603, W0621

# Importa as bibliotecas necessárias para o cliente
import sys, os, time
import xmlrpc.client


# Função para limpar a tela
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Menu inicial do cliente
def menu():
    clear_screen()
    print("Bem-vindo ao Gomoku!\n")
    print("1 - Criar uma nova Sala")
    print("2 - Entrar em uma Sala já existente")
    print("3 - Sair")

    return input("\nEscolha uma opção acima: ")

# Função para executar o jogo
def execute(sala_id, jogador):
    wait = False
    while True:
        jogador_atual = proxy.obter_jogador_atual(sala_id)
        if jogador_atual == jogador:
            clear_screen()

            wait = False
            print(f"Sua vez de jogar, jogador {jogador}!")
            print("Sala: " + sala_id + "\n")
            print(proxy.mostrar_tabuleiro(sala_id))

            # Pede a posição para jogar
            x, y = [
                (int(coord.strip()) - 1)
                for coord in input("\nDigite a posição (x, y) para jogar: ").split(",")
            ]
            res = proxy.jogar(sala_id, x, y, jogador)
            
            clear_screen()
            print(res)
            time.sleep(2)

            if "ganhou" in res:
                print("\nTabuleiro final:")
                print(proxy.mostrar_tabuleiro(sala_id))
                break
        else:
            if not wait:
                clear_screen()
                print("Aguarde o outro jogador realizar a jogada!\n")
                wait = True


# Cria o proxy para conectar ao servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
option = menu()

# Encerra o programa caso a opção seja 3
if option == "3":
    clear_screen()
    print("Obrigado por jogar Gomoku!")
    sys.exit()

# Cria uma nova sala caso a opção seja 1
if option == "1":
    clear_screen()
    sala_id = proxy.criar_sala()

    # Encerra caso já tenha atingido o numero máximo de salas
    if not sala_id.isdigit():
        clear_screen()
        print(sala_id)
        time.sleep(2)
        sys.exit()

    print(f"Sala criada com ID: {sala_id}")

    jogador = proxy.registrar_jogador(sala_id)
    print(f"Você é o jogador {jogador}")
    time.sleep(2)

    # Executa o jogo
    execute(sala_id, jogador)


# Entra em uma sala já existente caso a opção seja 2
if option == "2":
    clear_screen()
    sala_id = input("Digite o ID da sala: ")
    jogador = proxy.registrar_jogador(sala_id)

    # Encerra o programa caso a sala esteja cheia
    if jogador == "Sala cheia":
        print("Sala cheia, tente outra sala")
        time.sleep(2)
        sys.exit()

    print(f"Você é o jogador {jogador}")
    time.sleep(2)

    # Executa o jogo
    execute(sala_id, jogador)
