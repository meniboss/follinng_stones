from game import Game
from menu import Menu
from highscores import HighScores
import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((1000, 800))


    hi_scores = HighScores()
    menu = Menu(screen,hi_scores)

    running = True
    while running:
        result,username = menu.run()

        if result == "play":
            game = Game(screen, username, hi_scores)
            game_result = game.run()

            if game_result == "game over":
                menu.run()

        elif result == "quit":
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
