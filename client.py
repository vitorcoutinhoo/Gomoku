# pylint: disable = C0103, C0114, C0116, C0410, W0603

# Importa as bibliotecas necessárias para o cliente
import sys
import xmlrpc.client


# Menu inicial do cliente
def menu():
    print("Bem-vindo ao Gomoku!\n")
    print("1 - Criar uma nova Sala")
    print("2 - Entrar em uma Sala já existente")
    print("3 - Sair")

    return input("\nEscolha uma opção acima: ")


# Cria o proxy para conectar ao servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
option = menu()

# Encerra o programa caso a opção seja 3
if option == "3":
    sys.exit()

if option == "1":
    sala_id = proxy.criar_sala()
    print(f"Sala criada com ID: {sala_id}")

    jogador_atual = proxy.obter_jogador_atual(sala_id)

    jogador = proxy.registrar_jogador(sala_id)
    print(f"Você é o jogador {jogador}")

    count = 0
    while True:
        if jogador_atual != jogador:
            if count == 0:
                print("Aguarde a jogada do seu oponente")
                count += 1
            continue
        
        print(proxy.mostrar_tabuleiro(sala_id))

        x = int(input("Digite a posição x (1 - 15): ")) - 1
        y = int(input("Digite a posição y (1 - 15): ")) - 1

        result = proxy.jogar(sala_id, x, y, jogador)
        if "ganhou" in result:
            print(proxy.mostrar_tabuleiro(sala_id))
            break

        print(f"ID: {sala_id}")
        print(proxy.mostrar_tabuleiro(sala_id))
