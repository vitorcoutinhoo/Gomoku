# pylint: disable = C0103, C0114, C0116, W0603

# Importa as bibliotecas necessárias para o servidor
from xmlrpc.server import SimpleXMLRPCServer

# Importa os metodos da classe Room
from Models.room import Room

# Guarda as salas ativas
salas_ativas = {}

# função para criar a sala
def criar_sala():
    sala_id = Room.criar_sala()
    salas_ativas[sala_id] = Room.obter_sala(sala_id)
    return sala_id

# função para obter a sala
def obter_jogador_atual(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala :
        return "Sala não encontrada"
    return sala.jogador_atual

# função para registrar o jogador
def registrar_jogador(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"
    return sala.conectar_sala(sala_id)

# função para jogar
def jogar(sala_id, x, y, jogador):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"
    return sala.jogar(x, y, jogador)

# função para mostrar o tabuleiro
def mostrar_tabuleiro(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"
    return sala.mostrar_tabuleiro(sala_id)


# Cria o servidor
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor iniciado na porta 8000")

# Registra as funções no servidor
server.register_function(criar_sala, "criar_sala")
server.register_function(registrar_jogador, "registrar_jogador")
server.register_function(obter_jogador_atual, "obter_jogador_atual")
server.register_function(jogar, "jogar")
server.register_function(mostrar_tabuleiro, "mostrar_tabuleiro")

# Inicia o servidor
server.serve_forever()
