from game import Game
from menu import Menu
from highscores import HighScores
import pygame
from settings import Settings


def main():
    pygame.init()

    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Falling stones 🕹️")
    settings = Settings(screen)
    selected_texture = settings.selected_texture
    username = ""
    hi_scores = HighScores()



    running = True
    while running:
        menu = Menu(screen, selected_texture,username)
        result,username = menu.run(hi_scores)

        if result == "setting":
            settings_result, new_texture = settings.run()

            if settings_result == "yes":
                selected_texture = new_texture

        elif result == "play":
            game = Game(screen, username,selected_texture)

            game_result = game.run(hi_scores)

            pygame.mixer.music.stop()
            if game_result == "quit":
                running = False



        elif result == "quit":
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
