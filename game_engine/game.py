import pygame
import pygame.event
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
        self.run_game = self.game_loop(int)


    def set_scene(self, scene):
        self.scene = scene

    def set_main_script(self, game_script):
        self.run_game = self.game_loop(game_script)

    def game_loop(self, game_script=None):
        def wrapper():
            while self.run == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                
                delta = self.window.clock.tick(self.window.FPS) / 100

                self.window.screen.fill((200, 200, 200))

                if game_script:
                    game_script(delta)
                self.scene.run_scripts(delta)                
                self.scene.draw(self.window.screen)

                pygame.display.update()
                

        return wrapper
    
class Input():
    _actions = {}

    @staticmethod
    def get_direction(left, right, up, down):

        direction = Vector2(0, 0)
        if Input.action_is_pressed(left):
            direction += Vector2(-1, 0)

        if Input.action_is_pressed(right):
            direction += Vector2(1, 0)

        if Input.action_is_pressed(up):
            direction += Vector2(0, -1)

        if Input.action_is_pressed(down):
            direction += Vector2(0, 1)

        return direction
    
    @staticmethod
    def key_pressed(key):
        keys = pygame.key.get_pressed()
        return keys[key]
    
    def key_just_pressed(key):
        # pygame.event.set_allowed(pygame.KEYDOWN)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return True
                    
        return False
    
    @staticmethod
    def mouse_is_pressed(btn):
        buttons = ["left", "midlle", "right"]
        return pygame.mouse.get_pressed()[buttons.index(btn)]
    
    @staticmethod
    def create_action(name):
        Input._actions[name] = []

    @staticmethod
    def bind_keys_to_action(action, *keys):
        Input._actions[action] += keys

    @staticmethod
    def action_is_pressed(action):
        keys = pygame.key.get_pressed()
        return True in [keys[key] for key in Input._actions[action]]

    
    @staticmethod
    def get_mouse_position():
        return pygame.mouse.get_pos()