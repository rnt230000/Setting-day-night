import pygame
import time


class SunMoonSurface():
    def __init__(self, pos, size, img):
        self.pos = pos
        self.size = size
        self.img = img
        self.color = (0, 255, 0)
        self.alpha = 255
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((int(self.size), int(self.size)))
        surf.fill(self.color)
        surf.set_colorkey(self.color)
        resized_img = pygame.transform.scale(self.img, (surf.width, surf.height))
        surf.blit(resized_img, (surf.width//40, surf.height//40))
        return surf
    
    def update_pos(self, enable, dt):
        x, y = self.pos
        travel_speed = 0.99
        new_y = 0
        if y == 730:
            y = 730 if enable else 137 
            new_y = 730 if enable else 137 
        if y == 137:
            y = 137 if enable else 730
            new_y = 137 if enable else 730
        if y < new_y:
            y = min(y, new_y + travel_speed * dt)
        elif y > new_y:
            y = max(y, new_y - travel_speed * dt)
        self.pos = (x, y)
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class CloudSurface():
    def __init__(self, width, height, color, enable):
        self.width = width
        self.height = height
        self.enable = enable
        self.color = color
        self.alpha = 0 if enable else 255


    def update_color(self, enable, dt_ms):
        self.enable = enable
        target_alpha = 0 if self.enable else 255
        fade_speed = 0.89

        if self.alpha < target_alpha:
            self.alpha = min(target_alpha, self.alpha + (fade_speed * dt_ms))
        elif self.alpha > target_alpha:
            self.alpha = max(target_alpha, self.alpha - (fade_speed * dt_ms))

    def draw(self, surface):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((*self.color, int(self.alpha)))
        surface.blit(overlay, (0,0))



class DaySurface():

    def __init__(self, width, height, color, enable):
        self.width = width
        self.height = height
        self.enable = enable
        self.color = color
        self.alpha = 0 if enable else 255


    def update_color(self, enable, dt_ms):
        self.enable = enable
        target_alpha = 0 if self.enable else 255
        fade_speed = 0.89

        if self.alpha < target_alpha:
            self.alpha = min(target_alpha, self.alpha + (fade_speed * dt_ms))
        elif self.alpha > target_alpha:
            self.alpha = max(target_alpha, self.alpha - (fade_speed * dt_ms))

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
    is_cloudy_enabled = True
    is_clear_enabled = False


    clock = pygame.time.Clock()
    dt = 0
    moniter_size = pygame.display.Info()
    screen = pygame.display.set_mode((moniter_size.current_w, moniter_size.current_h), pygame.NOFRAME)


    # Sun
    sun = pygame.image.load("pixel_sun.png")
    sun_surf = SunMoonSurface((screen.width//8, screen.height//7), 70, sun)

    # Moon
    moon = pygame.image.load("pixel_moon.png")
    moon_surf = SunMoonSurface((screen.width//1.2, screen.height//1.3), 70, moon)

    # PNG
    panda_png = pygame.image.load("pixel_panda.png")
    panda = pygame.transform.scale(panda_png, (100*2, 100*2))

    green_mellow_png = pygame.image.load("pixel_green_meadow.png")
    green_mellow = pygame.transform.scale(green_mellow_png, (1900, 1000))
    n_green_mellow = pygame.transform.grayscale(green_mellow)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        # Buttons
        day_button = Button('Day', screen.width // 5, screen.height / 1.3, is_day_enabled)
        night_button = Button('Night', screen.width // 1.6, screen.height / 1.3, is_night_enabled)
        cloudy_button = Button('Cloudy', screen.width// 4, screen.height / 1.2, is_cloudy_enabled)
        clear_button = Button('Clear', screen.width// 1.8, screen.height / 1.2, is_clear_enabled)

        if pygame.mouse.get_pressed()[0] and is_button_enabled: 
            is_button_enabled = False
            # Day & Night buttons
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
            # Weather buttons
            if cloudy_button.check_click():
                if is_cloudy_enabled == False:
                    is_cloudy_enabled = True
                    is_clear_enabled = False
                else:
                    is_cloudy_enabled = False
            if clear_button.check_click():
                if is_clear_enabled == False:
                    is_clear_enabled = True
                    is_cloudy_enabled = False
                else:
                    is_clear_enabled = False

        if not pygame.mouse.get_pressed()[0] and not is_button_enabled: 
            is_button_enabled = True

        # Game loop required
        clear_bg = DaySurface(screen.width, screen.height, (92, 206, 250), is_day_enabled)
        cloudy_bg = CloudSurface(screen.width, screen.height, (176, 176, 176), is_day_enabled)
        clear_bg.update_color(is_button_enabled, dt)
        sun_surf.update_pos(is_day_enabled, dt)

        # Draw
        draw_this(clear_bg, screen)
        
        screen.blit(green_mellow, (screen.width//850, -200))
        screen.blit(panda, (screen.width//2, screen.height//2))

        draw_this(day_button, screen)
        draw_this(night_button, screen)
        draw_this(cloudy_button, screen)
        draw_this(clear_button, screen)
        draw_this(sun_surf, screen)
        draw_this(moon_surf, screen)


        pygame.display.flip()
        dt = clock.tick(12)

    pygame.quit()


def draw_this(vari, screen):
    """The vari needs to have a "draw" method in their class to work."""
    vari.draw(screen)


def function_n():
    ...

if __name__ == "__main__":
    main()
