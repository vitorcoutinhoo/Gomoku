# pylint: disable = C0103, C0114, C0115, C0116, W0603

import threading
from Models.tabuleiro import Tabuleiro


class Room:
    salas = {}

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador1 = None
        self.jogador2 = None
        self.jogador_atual = "X"
        self.lock = threading.Lock()

    @classmethod
    def criar_sala(cls):
        sala_id = str(len(cls.salas) + 1)
        cls.salas[sala_id] = Room()
        return sala_id

    @classmethod
    def obter_sala(cls, sala_id):
        return cls.salas.get(sala_id)

    def conectar_sala(self, sala_id):
        with self.lock:
            sala = self.salas.get(sala_id)

            if sala.jogador1 is None:
                sala.jogador1 = "X"
                return sala.jogador1

            if sala.jogador2 is None:
                sala.jogador2 = "O"
                return sala.jogador2

            return "Sala cheia"

    def jogar(self, x, y, jogador):
        with self.lock:
            if jogador != self.jogador_atual:
                return "Não é sua vez"

            if self.tabuleiro.movimentar_peca(x, y, jogador):
                if self.tabuleiro.verificar_ganhador():
                    return f"Jogador {jogador} ganhou!"

                self.jogador_atual = "O" if jogador == "X" else "X"
                return "Jogada Realizada!"
            return "Posição Inválida!"

    @classmethod
    def mostrar_tabuleiro(cls, sala_id):
        return cls.salas.get(sala_id).tabuleiro.mostrar_tabuleiro()
