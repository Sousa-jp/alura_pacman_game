import pygame

from constantes.cores import *
from constantes.settings import *

pygame.init()
display = (640, 480)

tela = pygame.display.set_mode(display, 0)
X = 10
Y = 10
velocidade_x = VELOCIDADE
velocidade_y = VELOCIDADE
while True:
    X += velocidade_x
    Y += velocidade_y

    if X + RAIO > 640:
        velocidade_x = -VELOCIDADE
    if X - RAIO < 0:
        velocidade_x = VELOCIDADE
    if Y + RAIO > 480:
        velocidade_y = -VELOCIDADE
    if Y - RAIO < 0:
        velocidade_y = VELOCIDADE

    tela.fill(PRETO)
    pygame.draw.circle(
        surface=tela,
        color=AMARELO,
        center=(int(X), int(Y)),
        radius=RAIO,
        width=2
    )
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
