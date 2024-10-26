# Gomoku 

<p align="justify">
    <strong>Gomoku</strong> é um jogo de tabuleiro no estilo "cinco em linha" jogado em uma grade 15x15, onde dois jogadores competem para alinhar cinco peças consecutivas em linha reta, seja horizontal, vertical ou diagonal.<br><br>
    Este projeto implementa uma versão distribuída do jogo utilizando chamadas remotas de procedimento (RPC), permitindo que os jogadores se conectem e interajam em diferentes salas de jogo.
</p>

### Funcionalidades

<lo align="justify">
    <li>Salas de Jogo (Rooms): Cada partida ocorre em uma sala única, identificada por um código de sala, onde os jogadores se conectam e competem entre si.</li><br>
    <li>Servidor RPC: Disponibiliza funções específicas das classes para o cliente, permitindo que ele chame diretamente métodos do servidor para manipular e obter informações sobre o jogo. Além de manter o estado das rooms.</li><br>
    <li>Cliente RPC: Permite aos jogadores realizar jogadas e receber atualizações do servidor em tempo real.</li>
</lo>
