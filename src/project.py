import pygame


class SunMoonSurface():
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.color = (0, 255, 0)
        self.alpha = 255
        self.surface = self.update_surface()
    
    def update_surface(self):
        surf = pygame.Surface((int(self.size), int(self.size)))
        surf.fill(self.color)
        #surf.set_colorkey(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class Day():

    def __init__(self, width, height, enable):
        self.width = width
        self.height = height
        self.enable = enable
        self.color = (92, 206, 250)
        self.alpha = 0 if enable else 255


    def update_color(self, enable, dt_ms):
        self.enable = enable
        target_alpha = 0 if self.enable else 255
        fade_speed = 0.99

        if self.alpha < target_alpha:
            self.alpha = min(target_alpha, self.alpha + fade_speed * dt_ms)
        elif self.alpha > target_alpha:
            self.alpha = max(target_alpha, self.alpha - fade_speed * dt_ms)

    def draw(self, surface):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((*self.color, int(self.alpha)))
        surface.blit(overlay, (0,0))

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
        if self.enabled:
            if self.check_click():
                pygame.draw.rect(surface, 'dark gray', button_rect, 0, 5)
            else: 
                pygame.draw.rect(surface, 'light gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(surface, 'black', button_rect, 0, 5)
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

    is_day_enabled = False
    is_night_enabled = True
    is_button_enabled = True

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
        
        sun_bg = SunMoonSurface((screen.width//8, screen.height//7), 70)
        moon_bg = SunMoonSurface((screen.width//1.2, screen.height//1.3), 70)
        #print((int(screen.width//8), int(screen.height//1.3)))
        #print((int(screen.width//1.2), int(screen.height//7)))

        # Buttons
        day_button = Button('Day', screen.width // 5, screen.height / 1.3, is_day_enabled)
        night_button = Button('Night', screen.width // 1.6, screen.height / 1.3, is_night_enabled)
        #print(day_button.check_click())
        #print(night_button.check_click())

        if pygame.mouse.get_pressed()[0] and is_button_enabled: 
            is_button_enabled = False
            if night_button.check_click():
                if is_day_enabled == False:
                    is_day_enabled = True
                    is_night_enabled = False
                else:
                    is_day_enabled = False
            if day_button.check_click():
                if is_night_enabled == False:
                    is_night_enabled = True
                    is_day_enabled = False
                else:
                    is_night_enabled = False
        if not pygame.mouse.get_pressed()[0] and not is_button_enabled: 
            is_button_enabled = True


        day_bg = Day(screen.width, screen.height, is_day_enabled)
        day_bg.update_color(is_button_enabled, dt)

        # Draw
        day_bg.draw(screen)
        day_button.draw(screen)
        night_button.draw(screen)
        sun_bg.draw(screen)
        moon_bg.draw(screen)

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
