import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
bg = pygame.Color("black")

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

    screen.fill(bg)

    screen.blit(main_character.body, dest = (main_character.x_position, main_character.y_position))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()