import pygame

# pygame setup
pygame.init()
display_size = pygame.display.get_desktop_sizes()
WIDTH = display_size[0][0]
HEIGHT = display_size[0][1]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True


while running:

    screen.fill("black")

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

