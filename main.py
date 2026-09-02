from game import Game
from menu import Menu
from highscores import HighScores
import pygame
from settings import Settings


def main():
    pygame.init()

    screen = pygame.display.set_mode((1000, 800))
    settings = Settings(screen)
    selected_texture = settings.selected_texture

    hi_scores = HighScores()



    running = True
    while running:
        menu = Menu(screen, selected_texture)
        result,username = menu.run(hi_scores)

        if result == "setting":
            result, new_texture = settings.run()

            if result == "yes":
                selected_texture = new_texture
                menu.run(hi_scores)

        elif result == "play":
            game = Game(screen, username,selected_texture)
            result = game.run(hi_scores)

            if result == "game over":
                menu.run(hi_scores)



        elif result == "quit":
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
