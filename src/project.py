import pygame

class Button():

    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled

    def draw(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 18)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.Rect((self.x_pos , self.y_pos), (150, 25))
        pygame.draw.rect(surface, 'gray', button_rect, 0, 5)
        pygame.draw.rect(surface, 'black', button_rect, 2, 5)
        surface.blit(button_text, (self.x_pos + 3, self.y_pos + 3))



def main():
    pygame.init()
    pygame.display.set_caption("Time Setting")

    clock = pygame.time.Clock()
    dt = 0
    moniter_size = pygame.display.Info()
    screen = pygame.display.set_mode((moniter_size.current_w, moniter_size.current_h), pygame.NOFRAME)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        day_button = Button('Day', screen.width // 4, screen.height / 1.5, True)
        night_button = Button('Night', screen.width // 1.5, screen.height / 1.5, True)
        day_button.draw(screen)
        night_button.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
    pygame.quit()


def function_1():
    ...


def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()
