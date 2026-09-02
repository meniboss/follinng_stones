import pygame

class Menu:

    def __init__(self, screen, selected_texture):
        self.screen = screen
        self.running = True
        self.play_button = pygame.Rect(self.screen.get_width() // 2 - 50,
            self.screen.get_height() // 2 -100, 200, 60)

        self.setting_button = pygame.Rect(self.screen.get_width() // 2 - 50,
            self.screen.get_height() // 2 -180, 200, 60)

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 60)
        self.small_font = pygame.font.Font(None, 30)
        self.username = ""
        self.score_text = ""
        self.selected_texture = selected_texture
        self.stone_image = pygame.image.load(self.selected_texture).convert()
        self.butten_image = pygame.transform.scale(self.stone_image, (200, 60))

    def get_user_name(self,key, unicode):
        if key == pygame.K_BACKSPACE:
            self.username = self.username[:-1]
            return None

        else:
            self.username += unicode
            return None

    def run(self,hi_scores):
        hi_scores.lode()
        self.score_text = ""
        for score in hi_scores.highscores:
            self.score_text += f"{score["username"]}: {score["score"]}\n"

        while self.running:
            self.screen.fill((30, 30, 30))

            y = 500
            for line in self.score_text.splitlines():
                scores_text = self.small_font.render(line,
                                        True, (100, 200, 100), )
                self.screen.blit(scores_text, (100, y))
                y += 30

            username_text = self.font.render(f"username:{self.username}",True, (200,100,100),)
            play_text = self.font.render("play", True, (100, 100, 200))
            rect_text = play_text.get_rect(center=self.play_button.center)

            setting_text = self.font.render("setting", True, (100, 100, 200))
            rect_st_text = setting_text.get_rect(center=self.setting_button.center)

            self.screen.blit(username_text, (200, 450))

            self.screen.blit(self.butten_image, self.play_button)
            self.screen.blit(self.butten_image, self.setting_button)

            self.screen.blit(play_text, rect_text)
            self.screen.blit(setting_text, rect_st_text)



            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.collidepoint(event.pos):
                        return "play",self.username
                    elif self.setting_button.collidepoint(event.pos):
                        return "setting",None

                if event.type == pygame.KEYDOWN:
                    self.get_user_name(event.key, event.unicode)

            self.clock.tick(60)
        return None




