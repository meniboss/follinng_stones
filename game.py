import random
import pygame
from pygame.constants import KEYDOWN
from highscores import HighScores
from shape import Shape


class Game:

    stone: Shape

    def __init__(self,screen, username, selected_texture):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.last_move = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 30)
        self.screen = screen
        self.username = username

        self.bord_width = 400
        self.bord_height = 600
        self.border = 20

        self.paused = False

        self.bord_x = (self.screen.get_width() - self.bord_width) // 2
        self.bord_y = (self.screen.get_height() - self.bord_height) // 2

        self.top = pygame.Rect(self.bord_x, self.bord_y - self.border, self.bord_width, self.border)
        self.bottom = pygame.Rect(self.bord_x, self.bord_y + self.bord_height, self.bord_width, self.border)
        self.left = pygame.Rect(self.bord_x - self.border, self.bord_y, self.border, self.bord_height)
        self.right = pygame.Rect(self.bord_x + self.bord_width, self.bord_y, self.border, self.bord_height)

        self.blocks = []

        self.selected_texture = selected_texture
        self.stone = self.create_new_stone
        self.next_stone = self.create_new_stone

        self.running = True

        self.score = 0
        self.special_score = 0
        self.level = 1
        self.falling_time = 1000
        self.special_move_check = False
        self.special_moves = 0

        self.stone_image = pygame.image.load(self.selected_texture).convert()


    @property
    def create_new_stone(self):
        """shapes = (square, "L" , "+" , reverse "L" ,zigzag,
        reverse zigzag, lain, "T" , "U" , ":", short line, "v", "bowl", gan, revers gan) """
        shapes = [
            [(-1, 0), (-1, 1), (0, 0), (0, 1)],

            [(-1, -1), (-1, 0), (-1, 1), (0, 1)],

            [(-1, -1), (-1, 0), (-1, 1), (0, 0)],

            [(0, -1), (0, 0), (0, 1), (-1, 1)],

            [(-1, -1), (-1, 0), (0, 0), (0, 1)],

            [(0, -1), (0, 0), (-1, 0), (-1, 1)],

            [(-1, -1), (-1, 0), (-1, 1), (-1, 2)],

            [(-1, -1), (0, -1), (0, 0), (0, 1), (1, -1)],

            [(-1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)],

            [(-1, -1), (-1, 1)],

            [(-1, -1), (-1, 0), (-1, 1)],

            [(-1, 0), (0, 0), (-1, 1)],

            [(-1, -1), (0, 0), (-1, 1)],

            [(-1, -1), (0, 0), (0, 1)],

            [(0, -1), (-1, 0), (-1, 1)]
        ]

        blocks = random.choice(shapes)

        return Shape(
            self.bord_x + self.bord_width // 2,
            self.bord_y - 80,
            blocks, self.selected_texture
        )

    def cen_move(self, dx, dy):
        for x, y in self.stone.stones:
            next_pos = pygame.Rect(
                self.stone.x + x * 40 + dx,
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

    def check_lines(self):
        rows = 0
        for y in range(self.bord_y, self.bord_y + self.bord_height, 40):
            row_blocks = [block for block in self.blocks if block.y == y]

            if len(row_blocks) == 10:
                rows += 1
                for block in row_blocks:
                    self.blocks.remove(block)

                for block in self.blocks:
                    if block.y < y:
                        block.y += 40
        if rows == 1:
            self.score += 100
            self.special_score += 100
        elif rows == 2:
            self.score += 350
            self.special_score += 350
        elif rows == 3:
            self.score += 600
            self.special_score += 600
        elif rows == 4:
            self.score += 950
            self.special_score += 950
        if not self.blocks:
            self.score += 1200
            self.special_score += 1200

    def special_move(self):
        for i in range(-40, 41, 40):
            for a in range(-40, 41, 40):

                for x, y in self.stone.stones:
                    x = self.stone.x + x * 40
                    y = self.stone.y + y * 40

                    for block in self.blocks:
                        if block.x == x + i and block.y == y + a :
                            self.blocks.remove(block)

    def game_over(self):
        for x, y in self.stone.stones:
            current_pos = pygame.Rect(
                self.stone.x + x * 40,
                self.stone.y + y * 40,
                40,
                40
            )
            if current_pos.colliderect(self.top):
                return True
        return None

    def run(self,hi_scores):
        while self.running:
            self.level = self.score // 1000 + 1
            self.falling_time = max(100, int(1170 - self.level ** 0.70 * 170))

            current_time = pygame.time.get_ticks()
            keys = pygame.key.get_pressed()

            self.screen.fill((30, 30, 30))

            self.stone.draw(self.screen)
            self.next_stone.draw_next_stone(self.screen)
            for block in self.blocks:
                self.screen.blit(self.stone_image, block)

            pygame.draw.rect(self.screen, (230, 230, 230), self.top)
            pygame.draw.rect(self.screen, (230, 230, 230), self.bottom)
            pygame.draw.rect(self.screen, (230, 230, 230), self.left)
            pygame.draw.rect(self.screen, (230, 230, 230), self.right)

            score_text = self.font.render(f"Score:{self.score}  Level:{self.level}  Special moves:{self.special_moves}",  True, (230, 230, 230))
            next_stone_text = self.font.render("next stone:",True, (230, 230, 230))
            username_text = self.font.render(f"player: {self.username}", True, (230, 230, 230))

            self.screen.blit(score_text, (self.bord_x, self.bord_y + self.bord_height + 40))
            self.screen.blit(next_stone_text, (self.bord_x -200, self.bord_y + 80))
            self.screen.blit(username_text, (self.bord_x -200, self.bord_y + 260))

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        if self.cen_move(40, 0) and not self.paused:
                            self.stone.x += 40

                    if event.key == pygame.K_LEFT:
                        if self.cen_move(-40, 0) and not self.paused:
                            self.stone.x -= 40

                    if event.key == pygame.K_UP:
                        if not self.paused:
                            self.stone.rotate(self.left, self.right, self.bottom, self.blocks)

                    if event.key == pygame.K_SPACE:
                        if not self.special_move_check and self.special_moves > 0 and not self.paused:
                            self.special_moves -= 1
                            self.special_move_check = True

                    if event.key == pygame.K_p:
                        self.paused = not self.paused
                        self.last_move = current_time - self.last_move

            if keys[pygame.K_DOWN]:
                if self.cen_move(0, 40) and not self.paused:
                    if current_time - self.last_move >= 70:
                        self.stone.y += 40
                        self.last_move = current_time

            if current_time - self.last_move >= self.falling_time \
                    and not self.paused:

                if self.cen_move(0, 40) and not self.paused:
                    self.stone.y += 40

                else:
                    if self.game_over():
                        hi_scores.add_score(self.username,self.score)
                        return None


                    for x, y in self.stone.stones:
                        block = pygame.Rect(
                            self.stone.x + x * 40,
                            self.stone.y + y * 40,
                            40,
                            40
                        )
                        self.blocks.append(block)
                    self.check_lines()
                    if self.special_score >= 500:
                        remainder = self.special_score % 500
                        self.special_moves += self.special_score // 500
                        self.special_moves = min(5, self.special_moves)
                        self.special_score = remainder

                    if self.special_move_check:
                        self.special_move()
                        self.special_move_check = False

                    self.stone = self.next_stone
                    self.next_stone = self.create_new_stone

                self.last_move = current_time

            self.clock.tick(60)

        pygame.quit()
        return None
