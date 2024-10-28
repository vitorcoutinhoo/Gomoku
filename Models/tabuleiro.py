# pylint: disable = C0103, C0114, C0115, C0116, C0301, W0603


class Tabuleiro:

    # Inicializa o tabuleiro com 15x15 posições e valores iniciais da ultima posição jogada
    def __init__(self):
        self.tabuleiro = [["*" for _ in range(15)] for _ in range(15)]
        self.lastpos = (0, 0, None)

    # Função para movimentar a peça no tabuleiro
    def movimentar_peca(self, x, y, peca):

        # verifica se a posição é válida
        if self.verificar_posicao(x, y):
            self.tabuleiro[x][y] = peca
            self.lastpos = (x, y, peca)
            return True

        # se a posição não for válida, retorna falso
        return False

    # Função para verificar a posição a ser movimentada
    def verificar_posicao(self, x, y):

        # verifica se a posição está dentro do tabuleiro
        if x < 0 or x > 14 or y < 0 or y > 14:
            return False

        # verifica se a posição não está vazia
        if self.tabuleiro[x][y] != "*":
            return False

        # se a posição for válida, retorna verdadeiro
        return True

    # Função para verificar se alguém ganhou
    def verificar_ganhador(self):
        # atribui as posições da última jogada
        x, y, peca = self.lastpos

        # verifica se existe uma sequência de 5 peças iguais em todas as direções possiveis
        for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]:
            if self.checar_sequencia(x, y, dx, dy, peca) or self.checar_sequencia(x, y, -dx, -dy, peca):
                return True

        # se não existir, retorna False
        return False

    # Função para checar sequência de peças
    def checar_sequencia(self, x, y, dx, dy, peca):
        for k in range(5):
            # px e py são as posições a serem verificadas
            px, py = x + k * dx, y + k * dy

            # se a posição não for válida ou a peça for diferente, retorna falso
            if (
                px < 0
                or py < 0
                or px >= 15
                or py >= 15
                or self.tabuleiro[px][py] != peca
            ):
                return False

        # se todas as posições forem iguais, retorna verdadeiro
        return True

    # Função para mostrar o tabuleiro
    def mostrar_tabuleiro(self):

        # Cria uma cópia para visualização com bordas
        tabuleiro_visual = [[" "] * 16 for _ in range(16)]

        # Ajusta a célula inicial para alinhamento
        tabuleiro_visual[0][0] = "  "

        # Adiciona números nas bordas com alinhamento
        for i in range(1, 16):
            tabuleiro_visual[0][i] = str(i).rjust(2)  # Números do topo
            tabuleiro_visual[i][0] = str(i).rjust(2)  # Números da esquerda

        # Preenche a visualização com os dados do tabuleiro
        for i in range(1, 16):
            for j in range(1, 16):
                tabuleiro_visual[i][j] = self.tabuleiro[i - 1][j - 1].rjust(2)

        # Exibe o tabuleiro formatado
        return "\n".join([" ".join(row) for row in tabuleiro_visual])
