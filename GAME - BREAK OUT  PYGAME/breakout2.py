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

# paddle colour's
paddle_col = (142, 135, 123)
paddle_outline = (100, 100, 100)

# Game variables
rows = 6
cols = 6
fpsClock = pygame.time.Clock()
fps = 60


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


class paddle():
    def __init__(self):
        self.height = 20
        self.width = int(screen_width // cols)
        self.x = int((screen_width/2) - (self.width/2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
    

    def move(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1


    def draw(self):
        pygame.draw.rect(screen, paddle_col, self.rect)
        pygame.draw.rect(screen, paddle_outline, self.rect, 3)
        

# create wall
wall = wall()
wall.create_wall()

# create paddle
player_paddle = paddle()

# Game Loop
run = True
while run:
    fpsClock.tick(fps)
    screen.fill(bg)

    wall.draw_wall()
    player_paddle.draw()
    player_paddle.move()
    
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
