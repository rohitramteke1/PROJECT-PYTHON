import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")

# NOTE: define colors
bg = (234, 218, 184)
# block colors
block_red = (242, 85, 96)
block_green = (86, 174, 87)
block_blue = (69, 177, 233)

# Game variables
rows = 6
cols = 6

# brick wall class
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50

    def create_wall(self):
        self.blocks = []
        # define an empty list for an individual wall
        block_individual = []
        for row in range(rows):
            # reset the block_row list
            block_row = []
            # iterate through the each column of that row
            for col in range(cols):
                # generate x and y positions for rach block and create a rectangle from that
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                # asign block strength based on row
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                # create a list at this point to store the rect and column data
                block_individual = [rect, strength]
                # append that individual to block row
                block_row.append(block_individual)
            # append the row to the full list of block
            self.blocks.append(block_row)

    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                # assign color based on block strength
                if block[1] == 3:
                    block_col = block_blue
                elif block[1] == 2:
                    block_col = block_green
                elif block[1] == 1:
                    block_col = block_red
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, (block[0]), 2)
                
# instance of wall
wall = wall()                
wall.create_wall()

    
# Game Loop
run = True
while run:

    screen.fill(bg)
    
    wall.draw_wall()
    
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