# Tic-Tac-Toe com Minimax e Poda Alfa-Beta

Este projeto é uma implementação do jogo da velha (Tic-Tac-Toe) em Python, utilizando o algoritmo Minimax com poda alfa-beta para garantir jogadas otimizadas e a melhor decisão possível para o computador.

## Descrição do Projeto

O objetivo deste projeto é criar uma versão do jogo da velha em que um jogador humano compete contra uma IA que utiliza o algoritmo Minimax para tomar decisões. A IA joga de forma ótima, garantindo que nunca perderá se seguir a estratégia correta.

## Funcionalidades

- Implementação completa do jogo da velha em Python.
- Utilização do algoritmo Minimax com poda alfa-beta para reduzir a complexidade computacional e garantir decisões rápidas.
- Funções implementadas incluem:
  - **initial_state**: Cria o estado inicial do tabuleiro.
  - **player**: Determina qual jogador tem o próximo turno.
  - **actions**: Retorna as ações possíveis para o tabuleiro.
  - **result**: Calcula o estado do tabuleiro após uma jogada.
  - **winner**: Determina o vencedor do jogo, se houver.
  - **terminal**: Verifica se o jogo terminou.
  - **utility**: Calcula o valor do jogo (1 para X, -1 para O, 0 para empate).
  - **minimax**: Encontra a jogada ótima para o jogador atual.

## Como Executar

1. Clone o repositório para o seu computador:
   ```bash
   git clone https://github.com/usuario/jogodavelha-ai.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd jogodavelha-ai
   ```
3. Execute o jogo:
   ```bash
   python tictactoe.py
   ```

## Requisitos

- Python 3.12 ou versão superior.

## Estrutura do Código

- **initial_state**: Retorna o tabuleiro vazio.
- **player**: Calcula qual jogador deve jogar a seguir.
- **actions**: Retorna todas as ações possíveis no tabuleiro.
- **result**: Retorna o novo estado do tabuleiro após uma jogada.
- **winner**: Determina o vencedor do jogo, se houver.
- **terminal**: Retorna `True` se o jogo terminou, `False` caso contrário.
- **utility**: Calcula a pontuação do jogo (1 para X, -1 para O, 0 para empate).
- **minimax**: Retorna a ação ótima para o jogador atual.
