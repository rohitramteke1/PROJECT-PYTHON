import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')


# font
font = pygame.font.SysFont('Times new roman', 40)


# colors
bg = (50, 25, 50)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# game variable

margin = 50
cpu_score = 0
player_score = 0


def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


run = True

while run:

    draw_board()
    draw_text('CPU ' + str(cpu_score), font, white, 20, 10)
    draw_text('Pr ' + str(player_score), font, white, screen_width - 100, 10)
    
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False






    pygame.display.update()

pygame.quit()
quit()
        