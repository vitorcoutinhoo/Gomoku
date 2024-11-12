# pylint: disable = C0103, C0114, C0116, W0603


# Importa as bibliotecas necessárias para o servidor
from xmlrpc.server import SimpleXMLRPCServer


# Importa os metodos da classe Room
from Models.room import Room


# Guarda as salas ativas e o número máximo de salas
salas_ativas = {}
max_salas = 3


# Função para criar a sala
def criar_sala(nome):
    # impede que o número de salas ativas ultrapasse o máximo
    if len(salas_ativas) >= max_salas:
        return "Número máximo de salas atingido"

    # cria a sala e a adiciona na lista de salas ativas
    sala_id = Room().criar_sala(nome)
    salas_ativas[sala_id] = Room.obter_sala(sala_id)

    # retorna o id da sala
    return sala_id


# Função para listar as salas
def listar_salas():
    salas = "Salas ativas:\n\n"
    for sala_id, sala in salas_ativas.items():
        salas += f"ID: {sala_id}, Nome: {sala.nome}, Status: {sala.status}\n"

    # retorna uma lista com as salas ativas
    return salas


# Função para obter o status da sala
def obter_status(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"

    # retorna o status da sala, caso a sala exista
    return sala.status


# Função para obter a sala
def obter_jogador_atual(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"

    # retorna o jogador atual, caso a sala exista
    return sala.jogador_atual


# Função para obter o ganhador
def obter_ganhador(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"

    # retorna o ganhador, caso a sala exista
    return sala.winner


# Função para registrar o jogador
def registrar_jogador(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"

    # conecta o jogador à sala, caso a sala exista
    return sala.conectar_sala(sala_id)


# Função para jogar
def jogar(sala_id, x, y, jogador):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"

    # realiza a jogada, caso a sala exista
    return sala.jogar(x, y, jogador)


# Função para finalizar a sala
def finalizar_sala(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"

    # finaliza a sala e retira ela das salas ativas, caso a sala exista
    Room.finalizar_sala(sala_id)
    salas_ativas.pop(sala_id)
    return "Sala finalizada"


# Função para mostrar o tabuleiro
def mostrar_tabuleiro(sala_id):
    sala = salas_ativas.get(sala_id)
    if not sala:
        return "Sala não encontrada"

    # retorna o tabuleiro, caso a sala exista
    return sala.mostrar_tabuleiro(sala_id)


# Cria o servidor
server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor iniciado na porta 8000")

# Registra as funções do servidor a serem disponibilizadas para o cliente
server.register_function(criar_sala, "criar_sala")
server.register_function(listar_salas, "listar_salas")
server.register_function(obter_status, "obter_status")
server.register_function(finalizar_sala, "finalizar_sala")
server.register_function(mostrar_tabuleiro, "mostrar_tabuleiro")

server.register_function(registrar_jogador, "registrar_jogador")
server.register_function(obter_jogador_atual, "obter_jogador_atual")
server.register_function(obter_ganhador, "obter_ganhador")
server.register_function(jogar, "jogar")

# Inicia o servidor
server.serve_forever()
