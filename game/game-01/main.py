#!usr/bin/python3

import pygame
import sys
import random

pygame.init()

# Setting up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Setting up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pythonic Games - Catch The Fish")

# Setting up the fish and the shark
fish_width = 50
fish_height = 50
fish_pos = [random.randint(0, WINDOW_WIDTH - fish_width), random.randint(0, WINDOW_HEIGHT - fish_height)]
shark_width = 100
shark_height = 100
shark_pos = [random.randint(0, WINDOW_WIDTH - shark_width), random.randint(0, WINDOW_HEIGHT - shark_height)]

# Setting up the scores
score = 0

# Setting up the player
player_size = 50
player_pos = [WINDOW_WIDTH / 2, WINDOW_HEIGHT - player_size]

# Creating a player object
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((player_size, player_size))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = player_pos

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

# Creating a fish object
class Fish(pygame.sprite.Sprite):
    def __init__(self):
        super(Fish, self).__init__()
        self.image = pygame.Surface((fish_width, fish_height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = fish_pos

    def update(self):
        global score
        if pygame.sprite.collide_rect(self, player):
            self.rect.center = [random.randint(0, WINDOW_WIDTH - fish_width), random.randint(0, WINDOW_HEIGHT - fish_height)]
            score += 1

# Creating a shark object
class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super(Shark, self).__init__()
        self.image = pygame.Surface((shark_width, shark_height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = shark_pos

    def update(self):
        global score
        if pygame.sprite.collide_rect(self, player):
            score -= 1
            if score <= 0:
                running = False

# Creating a player instance
player = Player()

# Creating a sprite group
sprites = pygame.sprite.Group()
sprites.add(player)

# Creating a fish and a shark instance
fish = Fish()
shark = Shark()

# Adding the fish and the shark to the sprite group
sprites.add(fish)
sprites.add(shark)

# Game loop
running = True
while running:
    window.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()
    sprites.draw(window)

    # Updating the score display
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, BLUE)
    window.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()