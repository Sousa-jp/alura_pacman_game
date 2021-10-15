import pygame

from constantes.cores import *



class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 100
        self.raio = int(self.tamanho / 2)

    def pintar(self, tela):
        pygame.draw.circle(
            tela,
            AMARELO,
            (self.centro_x, self.centro_y),
            self.raio
        )

        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(
            tela,
            PRETO,
            pontos,
            0
        )

        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(
            tela,
            PRETO,
            (olho_x, olho_y),
            olho_raio,
            0
        )


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600), 0)

    pacman = Pacman()
    while True:
        pacman.pintar(screen)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
