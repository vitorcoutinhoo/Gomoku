# pylint: disable = C0103, C0114, C0116, W0603

# Importa as bibliotecas necessárias para o cliente
import sys
import xmlrpc.client

# Cria o proxy para conectar ao servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Registra o jogador
jogador = proxy.registrar_jogador()

if not jogador:
    print("Jogo cheio")
    sys.exit()

print(f"Você é o jogador {jogador}!")

# Loop principal do jogo
while True:
    if proxy.player_atual() == jogador: # --> Verifica se é a vez do jogador
        
        # Mostra o tabuleiro
        print(proxy.mostrar_tabuleiro())

        # Pede a linha e a coluna para o jogador
        x = int(input("Digite a linha (0 - 14): "))
        y = int(input("Digite a coluna (0 - 14): "))

        # Chama a função jogar do servidor
        resultado = proxy.jogar(x, y, jogador)
        print(resultado)

        # Encerra o jogo se o jogador ganhou
        if "ganhou" in resultado:
            print(proxy.mostrar_tabuleiro()) # --> Mostra o tabuleiro final
            break
    else:
        print("Aguardando o Oponente")