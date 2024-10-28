# pylint: disable = C0103, C0114, C0116, C0410, W0603, W0621

# Importa as bibliotecas necessárias para o cliente
import sys, time
import xmlrpc.client
import game


# Cria conexão com o servidor, na porta 8000 do localhost
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Mostra o menu e obtem a opção escolhida pelo jogador
option = game.menu()

# Encerra o programa caso a opção seja 3
if option == "3":
    game.clean_screen()
    print("Obrigado por jogar Gomoku!")
    sys.exit()

# Cria uma nova sala caso a opção seja 1
if option == "1":
    game.clean_screen()
    sala_id = proxy.criar_sala()

    # encerra caso já tenha atingido o numero máximo de salas
    if not sala_id.isdigit():
        game.clean_screen()
        print(sala_id)
        time.sleep(2)
        sys.exit()

    print(f"Sala criada com ID: {sala_id}")

    # registra o jogador na sala
    jogador = proxy.registrar_jogador(sala_id)
    print(f"Você é o jogador {jogador}")
    time.sleep(2)

    # executa o jogo
    game.execute(sala_id, jogador, proxy)


# Entra em uma sala já existente caso a opção seja 2
if option == "2":
    game.clean_screen()
    sala_id = input("Digite o ID da sala: ")

    # registra o jogador na sala
    jogador = proxy.registrar_jogador(sala_id)

    # encerra o programa caso a sala não exista
    if jogador == "Sala não encontrada":
        print("Sala não encontrada, tente novamente")
        time.sleep(2)
        sys.exit()

    # encerra o programa caso a sala esteja cheia
    if jogador == "Sala cheia":
        print("Sala cheia, tente outra sala")
        time.sleep(2)
        sys.exit()

    print(f"Você é o jogador {jogador}")
    time.sleep(2)

    # executa o jogo
    game.execute(sala_id, jogador, proxy)
