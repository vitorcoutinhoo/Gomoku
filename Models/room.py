# pylint: disable = C0103, C0114, C0115, C0116, W0603


# Importa a biblioteca threading e a classe Tabuleiro
import threading
from Models.tabuleiro import Tabuleiro


class Room:
    # Armazena as salas criadas
    salas = {}

    # Inicializa a sala com um tabuleiro e os jogadores
    def __init__(self):
        self.nome = ""
        self.status = "Aguardando Jogadores"
        self.tabuleiro = Tabuleiro()
        self.jogador1 = None
        self.jogador2 = None
        self.jogador_atual = "X"
        self.winner = ""
        self.lock = threading.Lock()

    # Função para criar a sala
    def criar_sala(self, nome):
        sala_id = str(len(self.salas) + 1)

        self.salas[sala_id] = Room()
        self.salas[sala_id].nome = nome
        return sala_id

    # Função para finalizar a sala
    @classmethod
    def finalizar_sala(cls, sala_id):
        cls.salas.pop(sala_id)

    # Função para obter a sala
    @classmethod
    def obter_sala(cls, sala_id):
        return cls.salas.get(sala_id)

    # Função para conectar o jogador à sala
    def conectar_sala(self, sala_id):
        with self.lock:
            # verifica se a sala existe
            sala = self.salas.get(sala_id)
            if not sala:
                return "Sala não encontrada"

            # verifica se já existe o jogador X na sala
            if sala.jogador1 is None:
                sala.jogador1 = "X"
                return sala.jogador1

            # verifica se já existe o jogador O na sala
            if sala.jogador2 is None:
                sala.jogador2 = "O"
                sala.status = "Em Andamento"
                return sala.jogador2

            # se a sala estiver cheia, retorna a mensagem
            return "Sala cheia"

    # Função para jogar
    def jogar(self, x, y, jogador):
        with self.lock:
            # se não for a vez do jogador, retorna a mensagem
            if jogador != self.jogador_atual:
                return "Não é sua vez"

            # se a posição for válida, movimenta a peça
            if self.tabuleiro.movimentar_peca(x, y, jogador):

                # verifica se o jogador ganhou, caso sim, retorna a mensagem
                if self.tabuleiro.verificar_ganhador():
                    self.winner = jogador
                    return f"Jogador {jogador} ganhou!"

                # se não ganhou, passa a vez para o outro jogador
                self.jogador_atual = "O" if jogador == "X" else "X"
                return "Jogada Realizada!"

            # se a posição for inválida, retorna a mensagem
            return "Posição Inválida!"

    # Mostra o tabuleiro da sala
    @classmethod
    def mostrar_tabuleiro(cls, sala_id):
        return cls.salas.get(sala_id).tabuleiro.mostrar_tabuleiro()
