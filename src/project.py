import pygame

class SomeClass():

    def method_1():
        ...

    def method_2():
        ...

    def method_n():
        ...

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
