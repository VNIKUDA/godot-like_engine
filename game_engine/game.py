import pygame
pygame.init()

Vector2 = pygame.Vector2

class GameWindow():
    def __init__(self, window_size=(1280, 720), flags=0, FPS=60):
        self.screen = pygame.display.set_mode(window_size, flags)
        self.FPS = FPS
        self.clock = pygame.time.Clock()

class Game():
    def __init__(self, window_size=(1280, 720), flags=0, FPS=60):
        self.window = GameWindow(window_size, flags, FPS)
        self.run = True

        self.scene = None
        self.run_game = None


    def set_scene(self, scene):
        self.scene = scene

    def set_game_script(self, game_script):
        self.run_game = self.game_loop(game_script)

    def game_loop(self, game_script):
        def wrapper():
            while self.run == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                
                delta = self.window.clock.tick(self.window.FPS) / 100

                self.window.screen.fill((200, 200, 200))

                self.scene.draw(self.window.screen)
                game_script(delta)

                print(self.window.clock.get_fps())

                pygame.display.update()
                

        return wrapper
    
class Input():
    @staticmethod
    def get_direction(left, right, up, down):
        keys = pygame.key.get_pressed()

        direction = Vector2(0, 0)
        if keys[left]:
            direction += Vector2(-1, 0)

        if keys[right]:
            direction += Vector2(1, 0)

        if keys[up]:
            direction += Vector2(0, -1)

        if keys[down]:
            direction += Vector2(0, 1)

        return direction
    
    @staticmethod
    def key_is_pressed(key):
        keys = pygame.key.get_pressed()

        return keys[key]