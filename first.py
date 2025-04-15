import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_SPACE:
                print("Space key pressed!")
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))
    pygame.display.flip()
    