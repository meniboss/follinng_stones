
import pygame


class Shape:
    def __init__(self,x,y,stones):
        self.x = x
        self.y = y
        self.stones = stones

    def draw(self,screen):
        for x, y in self.stones:
            pygame.draw.rect(
                screen,
                (200,200,200),
                pygame.Rect(
                self.x + x * 40,
                self.y + y * 40,
                40,40
                )
            )

    def move(self,dx,dy):
        self.x += dx
        self.y += dy





