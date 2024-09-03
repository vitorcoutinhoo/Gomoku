# pylint: disable = C0103, C0114, C0116, W0603

# Importa as bibliotecas necessárias para o servidor
from xmlrpc.server import SimpleXMLRPCServer
import threading  # --> Utilizado para evitar que os dois jogadores joguem ao mesmo tempo

from Models.tabuleiro import Tabuleiro  # --> Importa a classe Tabuleiro

# Inicializa a classe Tabuleiro
tabuleiro = Tabuleiro()

# Define o jogador atual como X
jogador_atual = "X"

# Jogadores, inicialmente vazios
jogador1 = None
jogador2 = None

# Trava para evitar que dois jogadores joguem ao mesmo tempo
lock = threading.Lock()


# Função RPC para registrar jogador
def registrar_jogador():
    # Importa as variáveis globais para serem modificadas
    global jogador1, jogador2

    # A partir do momento que a função é chamada, a trava é ativada
    with lock:
        # Verifica se o jogador 1 está vazio, se sim, o jogador 1 é registrado como X
        if not jogador1:
            jogador1 = threading.current_thread().name
            return "X"

        # Verifica se o jogador 2 está vazio, se sim, o jogador 2 é registrado como O
        if not jogador2:
            jogador2 = threading.current_thread().name
            return "O"

        # Se ambos os jogadores já estiverem registrados, retorna None
        return None


# Função RPC para jogar
def jogar(x, y, jogador):
    # Importa as variáveis globais para serem modificadas
    global jogador_atual

    # A partir do momento que a função é chamada, a trava é ativada
    with lock:
        # Verifica se o jogador atual é o mesmo que o jogador que está tentando jogar
        if jogador_atual != jogador:
            return "Não é sua vez"  # --> Se não for a vez do jogador, retorna "Não é sua vez"

        # Mostra o tabuleiro atual, antes de realizar a jogada
        tabuleiro.mostrar_tabuleiro()

        # Chama a função movimentar_peca do tabuleiro
        if tabuleiro.movimentar_peca(x, y, jogador):
            # Verifica se o jogador atual ganhou
            if tabuleiro.verificar_ganhador():
                tabuleiro.mostrar_tabuleiro() # --> Mostra o tabuleiro ao final da partida
                return f"Jogador {jogador} ganhou"

            # Troca o jogador atual
            jogador_atual = "O" if jogador == "X" else "X"
            tabuleiro.mostrar_tabuleiro() # --> Mostra o tabuleiro ao final de cada jogada
            
            return "Jogada realizada"  # --> Se a jogada for realizada, retorna "Jogada realizada"

        return "Posição inválida"  # --> Se a posição for inválida, retorna "Posição inválida"


# Inicia o servidor RPC
servidor = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor iniciado na porta 8000")

# Registra as funções RPC
servidor.register_function(registrar_jogador, "registrar_jogador")
servidor.register_function(jogar, "jogar")

# Inicia o servidor
servidor.serve_forever()
