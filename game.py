import random
import pygame
from pygame.constants import KEYDOWN
from shape import Shape

class Game:



    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.last_move = pygame.time.get_ticks()

        self.screen = pygame.display.set_mode((600, 800))

        self.bord_width = 400
        self.bord_height = 600
        self.border = 20

        self.paused = False

        self.bord_x = (self.screen.get_width() - self.bord_width) // 2
        self.bord_y = (self.screen.get_height()- self.bord_height) // 2
        
        self.top = pygame.Rect(self.bord_x, self.bord_y - self.border, self.bord_width, self.border)
        self.bottom = pygame.Rect(self.bord_x, self.bord_y + self.bord_height, self.bord_width, self.border)
        self.left = pygame.Rect(self.bord_x - self.border, self.bord_y, self.border, self.bord_height)
        self.right = pygame.Rect(self.bord_x + self.bord_width, self.bord_y, self.border, self.bord_height)
        
        self.blocks = []
        self.stone = self.create_new_stone()

        self.running = True


    def create_new_stone(self):
        shapes =[
            [
                (-1,0),
                (-1,1),
                (0,0),
                (0,1)
            ],
            [
                (-1,0),
                (-1,1),
                (-1,2),
                (0,2)
            ],
            [
                (-1, 0),
                (-1, 1),
                (-1, 2),
                (0, 1)
            ]
        ]


        blocks = random.choice(shapes)


        return Shape(
            self.bord_x + self.bord_width // 2,
            self.bord_y,
            blocks
        )

    def cen_move(self,dx,dy):
        for x, y in self.stone.stones:
            next_pos = pygame.Rect(
                self.stone.x + x *  + dx,
                self.stone.y + y * 40 + dy,
                40,
                40
            )

            if (next_pos.colliderect(self.left) or
                    next_pos.colliderect(self.right) or
                    next_pos.colliderect(self.bottom) or
                    any(next_pos.colliderect(block) for block in self.blocks)):
                return False
        return True


    def run(self):
        while self.running:
            current_time = pygame.time.get_ticks()
    
            self.screen.fill((30,30,30))

            self.stone.draw(self.screen)
            for block in self.blocks:
                pygame.draw.rect(self.screen, (200,200,200), block)
    
            pygame.draw.rect(self.screen,(230,230,230),self.top)
            pygame.draw.rect(self.screen,(230,230,230),self.bottom)
            pygame.draw.rect(self.screen,(230,230,230),self.left)
            pygame.draw.rect(self.screen,(230,230,230),self.right)
    
            pygame.display.flip()
    
            for event in pygame.event.get():
    
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == KEYDOWN:
    
                    if event.key == pygame.K_RIGHT:
                        if self.cen_move(40,0) and not self.paused:
                            self.stone.x += 40
    
                    if event.key == pygame.K_LEFT:
                        if self.cen_move(-40,0) and not self.paused:
                            self.stone.x -= 40
    
                    if event.key == pygame.K_DOWN:
                        if self.cen_move(0,40) and not self.paused:
                            self.stone.y += 40
                            self.last_move = current_time
    
                    if event.key == pygame.K_p:
                        self.paused = not self.paused
                        self.last_move = current_time - self.last_move

            if current_time - self.last_move >= 700\
                    and not self.paused:

                if self.cen_move(0,40):
                    self.stone.y += 40

                else:
                    for x,y in self.stone.stones:
                        block = pygame.Rect(
                            self.stone.x + x * 40,
                            self.stone.y + y * 40,
                            40,
                            40
                        )
                        self.blocks.append(block)
                    self.stone = self.create_new_stone()

                self.last_move = current_time

            self.clock.tick(60)
    
    
        pygame.quit()