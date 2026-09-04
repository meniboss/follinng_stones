import pygame


class Settings:
    def __init__(self,screen):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.font = pygame.font.Font(None, 60)
        self.running = True
        self.frames = []
        self.return_button = pygame.Rect(self.screen.get_width() // 2 - 50,
            self.screen.get_height() // 2 -100, 200, 60)

        self.stone_pngs = [
            "textures/brick.png",
            "textures/cobblestone.png",
            "textures/crystal.png",
            "textures/gold.png",
            "textures/ice.png",
            "textures/lava.png",
            "textures/metal.png",
            "textures/moss.png",
            "textures/stone.png",
            "textures/wood.png",
            "textures/simple.png"
        ]
        self.selected_texture = "textures/brick.png"
        self.creat_frames()

    def creat_frames(self):
        y = 40
        for _ in self.stone_pngs:
            frame = pygame.Rect(60, y, 40, 40)
            self.frames.append(frame)

            y += 60

    def blit_stone_image(self):
        for i, stone in enumerate(self.stone_pngs):
            stone_image = pygame.image.load(stone).convert()
            self.screen.blit(stone_image,self.frames[i])


    def run(self):

        while self.running:
            self.screen.fill((30, 30, 30))
            return_text = self.font.render("Return", True, (100, 100, 200))
            rect_text = return_text.get_rect(center=self.return_button.center)

            stone_image = pygame.image.load(self.selected_texture).convert()
            stone_image = pygame.transform.scale(stone_image, (200, 60))
            self.screen.blit(stone_image, self.return_button)
            self.screen.blit(return_text, rect_text)

            self.blit_stone_image()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, frame in enumerate(self.frames):
                        if frame.collidepoint(event.pos):
                            self.selected_texture = self.stone_pngs[i]

                    if self.return_button.collidepoint(event.pos):
                        return "yes", self.selected_texture





            self.clock.tick(60)
        return None
