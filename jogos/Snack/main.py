"""Jogo da Cobra"""

import random
import sys
import time
import pygame
from pygame.locals import *
from collections import deque

SCREEN_WIDTH = 600      # Largura da tela
SCREEN_HEIGHT = 480     # Altura da tela
SIZE = 20               # Tamanho dos quadrados
LINE_WIDTH = 1          # Largura das linhas da grade

# Limites da área de jogo
SCOPE_X = (0, SCREEN_WIDTH // SIZE - 1)
SCOPE_Y = (2, SCREEN_HEIGHT // SIZE - 1)

# Pontuação e cores dos alimentos
FOOD_STYLE_LIST = [(10, (255, 100, 100)), (20, (100, 255, 100)), (30, (100, 100, 255))]

LIGHT = (100, 100, 100)
DARK = (200, 200, 200)      # Cor da cobra
BLACK = (0, 0, 0)           # Cor das linhas da grade
RED = (200, 30, 30)         # Vermelho, cor do texto GAME OVER
BGCOLOR = (40, 40, 60)      # Cor do fundo


def print_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))


# Inicializa a cobra
def init_snake():
    snake = deque()
    snake.append((2, SCOPE_Y[0]))
    snake.append((1, SCOPE_Y[0]))
    snake.append((0, SCOPE_Y[0]))
    return snake


def create_food(snake):
    food_x = random.randint(SCOPE_X[0], SCOPE_X[1])
    food_y = random.randint(SCOPE_Y[0], SCOPE_Y[1])
    while (food_x, food_y) in snake:
        # Se a comida aparecer no corpo da cobra, gera nova posição
        food_x = random.randint(SCOPE_X[0], SCOPE_X[1])
        food_y = random.randint(SCOPE_Y[0], SCOPE_Y[1])
    return food_x, food_y


def get_food_style():
    return FOOD_STYLE_LIST[random.randint(0, 2)]


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Jogo da Cobra')

    font1 = pygame.font.SysFont('SimHei', 24)  # Fonte da pontuação
    font2 = pygame.font.Font(None, 72)  # Fonte do GAME OVER
    fwidth, fheight = font2.size('GAME OVER')

    # Previne que a cobra morra ao pressionar direções opostas muito rapidamente
    # A variável b controla isso
    b = True

    # Cobra
    snake = init_snake()
    # Comida
    food = create_food(snake)
    food_style = get_food_style()
    # Direção
    pos = (1, 0)

    game_over = True
    start = False       # Controla início do jogo
    score = 0           # Pontuação
    orispeed = 0.5      # Velocidade inicial
    speed = orispeed
    last_move_time = None
    pause = False       # Pausa

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if game_over:
                        start = True
                        game_over = False
                        b = True
                        snake = init_snake()
                        food = create_food(snake)
                        food_style = get_food_style()
                        pos = (1, 0)
                        # Pontuação
                        score = 0
                        last_move_time = time.time()
                elif event.key == K_SPACE:
                    if not game_over:
                        pause = not pause
                elif event.key in (K_w, K_UP):
                    # Previne morte instantânea ao pressionar direção oposta
                    if b and not pos[1]:
                        pos = (0, -1)
                        b = False
                elif event.key in (K_s, K_DOWN):
                    if b and not pos[1]:
                        pos = (0, 1)
                        b = False
                elif event.key in (K_a, K_LEFT):
                    if b and not pos[0]:
                        pos = (-1, 0)
                        b = False
                elif event.key in (K_d, K_RIGHT):
                    if b and not pos[0]:
                        pos = (1, 0)
                        b = False

        # Preenche fundo
        screen.fill(BGCOLOR)
        # Desenha linhas verticais da grade
        for x in range(SIZE, SCREEN_WIDTH, SIZE):
            pygame.draw.line(screen, BLACK, (x, SCOPE_Y[0] * SIZE), (x, SCREEN_HEIGHT), LINE_WIDTH)
        # Desenha linhas horizontais da grade
        for y in range(SCOPE_Y[0] * SIZE, SCREEN_HEIGHT, SIZE):
            pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y), LINE_WIDTH)

        if not game_over:
            curTime = time.time()
            if curTime - last_move_time > speed:
                if not pause:
                    b = True
                    last_move_time = curTime
                    next_s = (snake[0][0] + pos[0], snake[0][1] + pos[1])
                    if next_s == food:
                        # Cobra comeu a comida
                        snake.appendleft(next_s)
                        score += food_style[0]
                        speed = orispeed - 0.03 * (score // 100)
                        food = create_food(snake)
                        food_style = get_food_style()
                    else:
                        if SCOPE_X[0] <= next_s[0] <= SCOPE_X[1] and SCOPE_Y[0] <= next_s[1] <= SCOPE_Y[1] \
                                and next_s not in snake:
                            snake.appendleft(next_s)
                            snake.pop()
                        else:
                            game_over = True

        # Desenha comida
        if not game_over:
            # Evita que a comida sobreponha o texto de GAME OVER
            pygame.draw.rect(screen, food_style[1], (food[0] * SIZE, food[1] * SIZE, SIZE, SIZE), 0)

        # Desenha cobra
        for s in snake:
            pygame.draw.rect(screen, DARK, (s[0] * SIZE + LINE_WIDTH, s[1] * SIZE + LINE_WIDTH,
                                            SIZE - LINE_WIDTH * 2, SIZE - LINE_WIDTH * 2), 0)

        print_text(screen, font1, 30, 7, f'Velocidade: {score//100}')
        print_text(screen, font1, 450, 7, f'Pontos: {score}')

        if game_over:
            if start:
                print_text(screen, font2, (SCREEN_WIDTH - fwidth) // 2, (SCREEN_HEIGHT - fheight) // 2, 'GAME OVER', RED)

        pygame.display.update()


if __name__ == '__main__':
    main()
