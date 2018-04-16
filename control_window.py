import pygame


class Color:
    WHITE = (255, 64, 64)
    BLACK = (0, 0, 0)
    HUD = (230, 50, 0)


def create_main_window():
    pygame.init()
    size = (620, 480)
    screen = pygame.display.set_mode(size)

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 20)

    screen.fill(Color.WHITE)

    img = pygame.image.load('images/arrow.jpg')
    screen.blit(img, (210, 250))

    img = pygame.image.load('images/clockwise.png')
    img = pygame.transform.scale(img, (100, 100))
    screen.blit(img, (100, 200))

    forward = myfont.render("A", False, Color.BLACK)
    screen.blit(forward, (145, 235))

    img = pygame.image.load('images/counterclockwise.png')
    img = pygame.transform.scale(img, (100, 100))
    screen.blit(img, (420, 200))

    forward = myfont.render("D", False, Color.BLACK)
    screen.blit(forward, (465, 235))

    forward = myfont.render('Forward', False, Color.BLACK)
    screen.blit(forward, (275, 255))

    forward = myfont.render('Back', False, Color.BLACK)
    screen.blit(forward, (290, 415))

    forward = myfont.render('Left', False, Color.BLACK)
    screen.blit(forward, (160, 370))

    forward = myfont.render('Right', False, Color.BLACK)
    screen.blit(forward, (415, 370))

    pygame.display.flip()

    return screen, myfont
