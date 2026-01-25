import pygame
from Appwrite_test import get_top_scores
from Appwrite_test import add_score
from names_generator import generate_name
from random import randint 
import datetime



pygame.init()
screen = pygame.display.set_mode((2560, 1440))
clock = pygame.time.Clock()
running = True
bg = pygame.Color("black")
score = 0
player_name = generate_name(seed=str(datetime.datetime.now()))

class Person:
    def __init__(self, x_size, y_size, x_position, y_position):

        self.body = pygame.Surface((x_size, y_size))
        self.body.fill(bg)
        self.x_position = x_position
        self.y_position = y_position
        pygame.draw.ellipse(self.body, "white", rect = [0, 0, self.body.get_width(), self.body.get_height()])

main_character = Person(100, 100, 100, 100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score += 100

    screen.fill(bg)

    screen.blit(main_character.body, dest = (main_character.x_position, main_character.y_position))

    pygame.display.flip()

    clock.tick(60)
    

    if pygame.time.get_ticks() > 10000:
        running = False




add_score({'Name': player_name, 'Score': score})
print(f"Score submitted: {player_name} - {score}\n")
print("Top Scores:\n")

top_scores = get_top_scores(10)
i = 10

for score in top_scores['rows']:
    print(f"{i}. {score['Name']}: {score['Score']}\n")
    i -= 1



pygame.quit()