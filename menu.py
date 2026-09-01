import pygame
from highscores import HighScores


class Menu:

    def __init__(self, screen, hi_scores):
        self.screen = screen
        self.running = True
        self.play_button = pygame.Rect(self.screen.get_width() // 2 - 50,
            self.screen.get_height() // 2 -100, 120, 60)

        self.font = pygame.font.Font(None, 60)
        self.small_font = pygame.font.Font(None, 30)
        self.username = ""
        self.start = False
        self.hi_scores = hi_scores
        self.score_text = ""

    def run(self):
        self.hi_scores.lode()
        self.score_text = ""
        for score in self.hi_scores.highscores:
            self.score_text += f"{score["username"]}: {score["score"]}\n"

        while self.running:

            self.screen.fill((30, 30, 30))
            y = 500
            for line in self.score_text.splitlines():
                scores_text = self.small_font.render(line,
                                        True, (200, 100, 100), )
                self.screen.blit(scores_text, (100, y))
                y += 30
            if self.start:
                text = self.font.render(f"username:{self.username}",
                            True, (200,100,100),)
                self.screen.blit(text, (200, 450))

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
                        # return "play", self.username
                        self.start = True

                if event.type == pygame.KEYDOWN:
                    if self.start:
                        if event.key == pygame.K_RETURN:
                            return "play", self.username

                        elif event.key == pygame.K_BACKSPACE:
                            self.username = self.username[:-1]

                        else:
                            self.username += event.unicode
        return None




