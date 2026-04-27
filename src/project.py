import pygame


class Day():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = (92, 206, 250, 0.8)

    def draw(self, surface):
        rect = pygame.Rect((0,0), (self.width, self.height))
        pygame.draw.rect(surface, self.color, rect)

class Button():

    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled

    def draw(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 40)
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.Rect((self.x_pos , self.y_pos), (150*2, 25*2))
        if self.check_click():
            pygame.draw.rect(surface, 'dark gray', button_rect, 0, 5)
        else: 
            pygame.draw.rect(surface, 'light gray', button_rect, 0, 5)
        pygame.draw.rect(surface, 'black', button_rect, 2, 5)
        surface.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.Rect((self.x_pos , self.y_pos), (150*2, 25*2))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False



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
        # Buttons
        day_button = Button('Day', screen.width // 5, screen.height / 1.3, True)
        night_button = Button('Night', screen.width // 1.6, screen.height / 1.3, True)
        print(day_button.check_click())
        print(night_button.check_click())

        day_bg = Day(screen.width, screen.height)

        # Draw
        day_bg.draw(screen)
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
