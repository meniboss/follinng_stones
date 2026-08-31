import pygame


class Menu:

    def __init__(self,screen):
        self.screen = screen
        self.running = True
        self.play_button = pygame.Rect(self.screen.get_width() // 2 - 50,
            self.screen.get_height() // 2 -100, 120, 60)

    def run(self):
        while self.running:
            self.screen.fill((30, 30, 30))

            pygame.draw.rect(
                self.screen,
            (230, 230 ,230),
                self.play_button
            )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.collidepoint(event.pos):
                        return "play"

        return None

