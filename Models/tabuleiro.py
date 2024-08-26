class tabuleiro():
    # Inicializa o tabuleiro com 15x15
    def __init__(self):
        self.tabuleiro = [["="] * 15 for _ in range(15)]

    # Função para movimentar a peça no tabuleiro
    def movimentar_peca(self, x, y, peca):

        # Verifica se a posição é válida
        if self.verificar_posicao(x, y):
            self.tabuleiro[y][x] = peca

            # Adiciona a posição da peça no tabuleiro
            if peca == "0":
                self.pos_0.append([x, y])
            else:
                self.pos_x.append([x, y])

        else:
            print("Posição inválida")
    
    # Função para verificar posição a ser movimentada
    def verificar_posicao(self, x, y):

        # Verifica se a posição está dentro do tabuleiro
        if x < 0 or x > 14 or y < 0 or y > 14:
            return False
        
        # Verifica se a posição está vazia
        if self.tabuleiro[y][x] != "=":
            return False

        return True
    
    # Função para verificar se alguém ganhou
    # olha em todas as direções possiveis
    def verificar_ganhador(self, x, y, peca):
        for dx, dy in [(1, 0), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1)]:
            if self.checar_sequencia(x, y, dx, dy, peca):
                return True
        return False

    # Função para checar sequência de peças
    def checar_sequencia(self, x, y, dx, dy, peca):
        for k in range(5):
            # nx e ny são as posições a serem verificadas
            nx, ny = x + k * dx, y + k * dy

            # se a posição não for válida ou a peça for diferente, retorna falso
            if nx < 0 or ny < 0 or nx >= 15 or ny >= 15 or self.tabuleiro[ny][nx] != peca:
                return False
        return True

    # Função para mostrar o tabuleiro
    def mostrar_tabuleiro(self):
        return "\n".join([" ".join(row) for row in self.tabuleiro])


x = tabuleiro()
x.movimentar_peca(1, 7, "X")
x.movimentar_peca(2, 8, "X")
x.movimentar_peca(3, 9, "X")
x.movimentar_peca(4, 10, "X")
x.movimentar_peca(5, 11, "X")

# verifica ganhador -> (last_x, last_y, peca)
print(x.verificar_ganhador(5, 11, "X"))
print(x.mostrar_tabuleiro())
