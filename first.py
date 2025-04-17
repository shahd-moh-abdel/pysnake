import pygame
import random
import time
pygame.init()

class Game:

    def __init__(self):
        pygame.init()
        # Constants
        self.WIDTH, self.HEIGHT = 500, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.x = 100
        self.y = 100
        self.speed = 15
        self.score = 0
        self.font = pygame.font.SysFont("comicsans", 36)

        #colors
        self.BLACK = pygame.Color(0, 0, 0)
        self.WHITE = pygame.Color(255, 255, 255)
        self.RED = pygame.Color(227, 100, 136)
        self.GREEN = pygame.Color(174, 244, 164)
        self.BLUE = pygame.Color(121, 184, 209)
        self.YELLOW = pygame.Color(255, 253, 183)

        self.head = [self.x, self.y]
        self.snake = [[self.x, self.y], [self.x - 10, self.y], [self.x - 20, self.y]]
        self.dir = "RIGHT"
        self.next_dir = self.dir
        self.food_pos = [random.randrange(1, (self.WIDTH // 10)) * 10,
                         random.randrange(1, (self.HEIGHT // 10)) * 10]
        self.food_spawn = True
        self.eaten = False

    def show_score(self):
        score_surface = self.font.render(f"Score: {self.score}", True, self.BLACK)
        score_rect = score_surface.get_rect()
        self.screen.blit(score_surface, score_rect)

    def spawn_food(self):
        if self.eaten:
            self.food_pos = [random.randrange(1, (self.WIDTH // 10)) * 10, random.randrange(1, (self.HEIGHT // 10)) * 10]
            # pygame.draw.rect(self.screen, self.YELLOW,pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
            self.eaten = False

    def keyboard(self, key):
        if key == pygame.K_UP:
            self.next_dir = "UP"
        if key == pygame.K_DOWN:
            self.next_dir = "DOWN"
        if key == pygame.K_LEFT:  
            self.next_dir = "LEFT"
        if key == pygame.K_RIGHT:
            self.next_dir = "RIGHT"

        if self.next_dir == "UP" and self.dir != "DOWN":
            self.dir = "UP"
        if self.next_dir == "DOWN" and self.dir != "UP":
            self.dir = "DOWN"
        if self.next_dir == "LEFT" and self.dir != "RIGHT":
            self.dir = "LEFT"
        if self.next_dir == "RIGHT" and self.dir != "LEFT":
            self.dir = "RIGHT"

    def snake_method(self):
            pygame.draw.rect(self.screen, self.RED, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
            self.snake.insert(0, list(self.head))
            if self.head[0] == self.food_pos[0] and self.head[1] == self.food_pos[1]:
                self.score += 10
                self.eaten = True
            else:
                self.snake.pop()

            
            for pos in self.snake:
                pygame.draw.rect(self.screen, self.BLUE, pygame.Rect(pos[0], pos[1], 10, 10))

            if self.dir == "UP":
                self.head[1] -= 10
            if self.dir == "DOWN":
                self.head[1] += 10
            if self.dir == "LEFT":
                self.head[0] -= 10
            if self.dir == "RIGHT":
                self.head[0] += 10

            if self.head[0] < 0 or self.head[0] > (self.WIDTH - 10) or self.head[1] < 0 or self.head[1] > (self.HEIGHT - 10):
                self.game_over()
            for block in self.snake[1:]:
                if self.head[0] == block[0] and self.head[1] == block[1]:
                    self.game_over()

    def game_over(self):
        game_over_surface = self.font.render("Game Over", True, self.RED)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.WIDTH / 2, self.HEIGHT / 4)
        self.screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()

    def start(self):
        pygame.display.set_caption("My First Game")
        fps = pygame.time.Clock()

        while True:
            self.screen.fill(self.GREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    self.keyboard(event.key)

            self.snake_method()
            self.show_score()

            if self.eaten:
                self.spawn_food()
                self.eaten = False

            pygame.display.update()
            fps.tick(self.speed)
       

if __name__ == "__main__":
    game = Game()
    game.start()
    