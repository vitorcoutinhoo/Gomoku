# pylint: disable = C0103, C0114, C0115, C0116, W0603

class Tabuleiro():

    # Inicializa o tabuleiro com 15x15 posições
    def __init__(self):
        self.tabuleiro = [["*"] * 15 for _ in range(15)]
        self.lastpos = (0, 0, None)

    # Função para movimentar a peça no tabuleiro
    def movimentar_peca(self, x, y, peca):

        # Verifica se a posição é válida
        if self.verificar_posicao(x, y):
            self.tabuleiro[x][y] = peca
            self.lastpos = (x, y, peca)
            return True

        # Se a posição não for válida, retorna falso
        return False


    # Função para verificar posição a ser movimentada
    def verificar_posicao(self, x, y):

        # Verifica se a posição está dentro do tabuleiro
        if x < 0 or x > 14 or y < 0 or y > 14:
            return False

        # Verifica se a posição não está vazia
        if self.tabuleiro[y][x] != "*":
            return False

        return True


    # Função para verificar se alguém ganhou
    def verificar_ganhador(self):
        x, y, peca = self.lastpos

        # Verifica se existe uma sequência de 5 peças iguais em todas as direções possiveis
        for dx, dy in [(1, 0), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1)]:
            if self.checar_sequencia(x, y, dx, dy, peca):
                return True
        
        # Se não existir, retorna False
        return False


    # Função para checar sequência de peças
    def checar_sequencia(self, x, y, dx, dy, peca):
        for k in range(5):
            # nx e ny são as posições a serem verificadas
            nx, ny = x + k * dx, y + k * dy

            # Se a posição não for válida ou a peça for diferente, retorna falso
            if nx < 0 or ny < 0 or nx >= 15 or ny >= 15 or self.tabuleiro[ny][nx] != peca:
                return False
        return True


    # Função para mostrar o tabuleiro
    def mostrar_tabuleiro(self):
        return "\n".join([" ".join(row) for row in self.tabuleiro])
