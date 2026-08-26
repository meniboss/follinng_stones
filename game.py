import pygame
from pygame.constants import KEYDOWN

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600,800))

bord_width = 400
bord_height = 600
border = 20
paused = False

bord_x = (screen.get_width() - bord_width) // 2
bord_y = (screen.get_height()- bord_height) // 2

stone = pygame.Rect(bord_x + 200, bord_y, 40, 40)

def create_new_stone():
    return pygame.Rect(bord_x + 200, bord_y, 40, 40)


blocks = []


top = pygame.Rect(bord_x, bord_y - border, bord_width, border)
bottom = pygame.Rect(bord_x, bord_y + bord_height, bord_width, border)
left = pygame.Rect(bord_x - border, bord_y,border, bord_height)
right = pygame.Rect(bord_x + bord_width, bord_y, border, bord_height)

last_move = pygame.time.get_ticks()

running = True

while running:
    current_time = pygame.time.get_ticks()

    screen.fill((30,30,30))

    for block in blocks:
        pygame.draw.rect(screen, (200,200,200), block)
    pygame.draw.rect(screen,(200,200,200), stone)

    pygame.draw.rect(screen,(230,230,230),top)
    pygame.draw.rect(screen,(230,230,230),bottom)
    pygame.draw.rect(screen,(230,230,230),left)
    pygame.draw.rect(screen,(230,230,230),right)

    pygame.display.flip()

    keys = pygame.key.get_pressed()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            print(blocks)

        if event.type == KEYDOWN:

            if event.key == pygame.K_RIGHT:
                next_pos = stone.move(40,0)

                if not next_pos.colliderect(right)\
                        and not any(next_pos.colliderect(block) for block in blocks)\
                        and not paused:
                    stone.x += 40

            if event.key == pygame.K_LEFT:
                next_pos = stone.move(-40,0)

                if not next_pos.colliderect(left)\
                        and not any(next_pos.colliderect(block) for block in blocks)\
                    and not paused:
                    stone.x -= 40

            if event.key == pygame.K_DOWN:
                next_pos = stone.move(0, 40)

                if not next_pos.colliderect(bottom)\
                        and not any(next_pos.colliderect(block) for block in blocks) \
                        and not paused:
                    stone.y +=40
                    last_move = current_time

            if event.key == pygame.K_SPACE:
                blocks.append(stone)
                stone = create_new_stone()
                last_move = current_time

            if event.key == pygame.K_p:
                paused = not paused
                last_move = current_time - last_move

    next_pos = stone.move(0, 40)
    if current_time - last_move >= 700 \
            and not paused:


        if not next_pos.colliderect(bottom)\
                and not any(next_pos.colliderect(block) for block in blocks):
            stone.y += 40


        else:
            blocks.append(stone)
            stone = create_new_stone()

        last_move = current_time

    clock.tick(60)


pygame.quit()