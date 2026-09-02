import pygame


class Shape:
    def __init__(self, x, y, stones,selected_texture):
        self.x = x
        self.y = y
        self.stones = stones
        self.selected_texture = selected_texture
        self.stone_image = pygame.image.load(self.selected_texture).convert()
        self.small_stone_image = pygame.transform.scale(self.stone_image, (25, 25))

    def draw(self, screen):
        for x, y in self.stones:
            screen.blit(
                self.stone_image,
                pygame.Rect(
                    self.x + x * 40,
                    self.y + y * 40,
                    40,
                    40
                )
            )

    def draw_next_stone(self, screen):
        for x, y in self.stones:
            screen.blit(self.small_stone_image,
                pygame.Rect(
                    self.x -340 + x * 25,
                    self.y + 220 + y * 25,
                    25,
                    25
                )
            )

    def rotate(self, left, right, bottom, blocks):
        new_stones = []
        legal = True
        for x, y in self.stones:
            new_x = -y
            new_y = x
            next_pos = pygame.Rect(
                self.x + new_x,
                self.y + new_y,
                40, 40)

            if not (next_pos.colliderect(left) or
                    next_pos.colliderect(right) or
                    next_pos.colliderect(bottom) or
                    any(next_pos.colliderect(block) for block in blocks)):

                new_stones.append((new_x, new_y))

            else:
                legal = False
                break

        if legal:
            self.stones = new_stones
