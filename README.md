## Gomoku - Projeto de Sistemas Distribuídos

**Gomoku** é um jogo de tabuleiro (15 x 15), onde dois jogadores competem entre si. Para atingir a vitória um dos jogadores deve completar **5 peças em sequência**.

O objetivo do projeto é implementar uma versão do jogo com **métodos de chamadas remotas (RPC)**.

#### Arquivos
- Pasta Models: Possui a classe **Tabuleiro**. Essa sendo responsável pelos métodos para criar um tabuleiro, mover as peças e verificar se algum jogador ganhou.

- _server.py_: Arquivo onde está a configuração do servidor, e seus eventuais métodos RPC. Responsável pela **parte lógica** do jogo e por manter o estado atual do jogo.

- _client.py_: Arquivo onde está a comunicação entre cliente e servidor. Responsável por **enviar a jogada** ao servidor e receber a resposta.

#### Rodando os arquivos:
Para rodar o servidor basta estar na pasta raiz e digitar no terminal
``` bash
python server.py 
```
Para rodar o client abra um terminal novo na pasta raiz e digite
```bash
python client.py
```
<p style="font-size: 11px; font-style: italic"> Obs: Cada jogador deve ser aberto em um terminal diferente!</p>
