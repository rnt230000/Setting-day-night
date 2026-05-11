import pygame

class EnableGrayscale():
    def __init__(self, image, pos, enable):
        self.img = image
        self.pos = pos
        self.enable = enable
        self.new_img = self.convert_image()

    def convert_image(self):
        orig_img = self.img
        gray_img = pygame.transform.grayscale(self.img)
        gray_r, gray_b, gray_g = gray_img
        if self.enable == True:
            for w in range(orig_img.get_width()):
                for h in range(orig_img.get_height()):
                    r, g, b, = orig_img.get_at((w, h))
                    orig_img.set_at((w, h), pygame.Color(gray_r, gray_g, gray_b))
        elif self.enable == False:
            for w in range(orig_img.get_width()):
                for h in range(orig_img.get_height()):
                    r, g, b, = orig_img.get_at((w, h))
                    orig_img.set_at((w, h), pygame.Color(r, g, b))

    def draw(self, surface):
        surface.blit(self.new_img, self.pos)

class GroundSurface():
    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = color
        self.surface = self.create_surface()
    
    def create_surface(self):
        surf = pygame.Surface((int(self.size*35), int(self.size*10)))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        surface.blit(self.surface, self.pos)

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
        if y == 137 and enable == True:
            y += 1
            #if y >= 378:
                #y = 378
        else:
            y = 378
        self.pos = (x, y)
        print(self.pos)
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

class CloudSurface():
    def __init__(self, width, height, enable):
        self.width = width
        self.height = height
        self.enable = enable
        self.day_clr = (176, 176, 176)
        self.night_clr = (38, 38, 38)
        self.alpha = 0 if enable else 255

    def update_color(self, enable, dt_ms):
        self.enable = enable
        target_alpha = 0 if self.enable else 255
        fade_speed = 0.89

        if self.alpha < target_alpha:
            self.alpha = min(target_alpha, self.alpha + (fade_speed * dt_ms))
        elif self.alpha > target_alpha:
            self.alpha = max(target_alpha, self.alpha - (fade_speed * dt_ms))

    def draw(self, surface, n_enable):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        if n_enable == False:
            overlay.fill((*self.night_clr, int(self.alpha)))
        elif n_enable == True:
            overlay.fill((*self.day_clr, int(self.alpha)))
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
    moon_surf = SunMoonSurface((int(screen.width//1.2), int(screen.height//1.3)), 70, moon)

    # PNG
    panda_png = pygame.image.load("pixel_panda.png")
    panda = pygame.transform.scale(panda_png, (100*2, 100*2))

    green_meadow_png = pygame.image.load("pixel_green_meadow.png")
    green_meadow = pygame.transform.scale(green_meadow_png, (1900, 1000))

    dirt_meadow = GroundSurface((screen.width//900, screen.height//1.3), 50, (23, 103, 100))

    clear_bg = DaySurface(screen.width, screen.height, (92, 206, 250), is_day_enabled)
    cloudy_bg = CloudSurface(screen.width, screen.height, is_clear_enabled)


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
                if is_clear_enabled == False:
                    is_clear_enabled = True
                    is_cloudy_enabled = False
                else:
                    is_cloudy_enabled = False
            if clear_button.check_click():
                if is_cloudy_enabled == False:
                    is_cloudy_enabled = True
                    is_clear_enabled = False
                else:
                    is_cloudy_enabled = False

        if not pygame.mouse.get_pressed()[0] and not is_button_enabled: 
            is_button_enabled = True

        # Game loop required
        clear_bg.update_color(is_day_enabled, dt)
        cloudy_bg.update_color(is_cloudy_enabled, dt)
        sun_surf.update_pos(is_day_enabled, dt)
        moon_surf.update_pos(is_night_enabled, dt)

        # Draw
        draw_this(clear_bg, screen)
        draw_this(sun_surf, screen)
        draw_this(moon_surf, screen)
        cloudy_bg.draw(screen, is_night_enabled)
        draw_this(dirt_meadow, screen)
        screen.blit(green_meadow, (screen.width//1000, screen.height*-0.2))
        screen.blit(panda, (screen.width//2, screen.height//2))
        draw_this(day_button, screen)
        draw_this(night_button, screen)
        draw_this(cloudy_button, screen)
        draw_this(clear_button, screen)

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
