import pygame, os, math
pygame.init()
Vector2 = pygame.Vector2

# Клас Node2D, працює як група
class Node2D():
    def __init__(self, name):
        self.name = name
        self.parent: Node2D

        self.script = lambda self, delta: "pass"

        self.children = {}
        self.position = Vector2(0, 0)
        self.rotation_degrees = 0
        self.scale = 1

        self.width, self.height = self.size = (1000, 1000)

        self.surface = pygame.Surface((self.width, self.height), flags=pygame.SRCALPHA).convert_alpha() 

    def upscale(self, scale):
        self.scale *= scale

    def rotate(self, rotation_degrees):
        self.rotation_degrees += rotation_degrees

    def move(self, offset: Vector2):
        self.position += offset

    def get_global_position(self):
        position = self.position.copy()
        parent = self.parent

        try:
            while 1:
                position += parent.position

                parent = parent.parent
        finally:
            return Vector2(position)
        
    # def set_relative_position(self, position):
    #     self.position = Vector2(position.x + self.width/2, position.y + self.height/2)


    def draw(self, surface: pygame.Surface):
        self.surface.fill((0,0,0,0))
        if self.children != {}:
            children = self.children.values()

            right = max([abs(child.position.x  + child.width * child.scale) for child in children])
            down = max([abs(child.position.y  + child.height * child.scale) for child in children])

            top = max([child.position.x for child in children])
            left = max([child.position.y for child in children])

            self.width, self.height = self.size = abs(right - left), abs(down - top)

            self.surface = pygame.transform.scale(self.surface, self.size)

            for child in self.children.values():
                child.draw(self.surface)

            transformed_surface = pygame.transform.rotozoom(self.surface, self.rotation_degrees, self.scale).convert_alpha()
            # position = self.position.x - transformed_surface.get_width()/2, self.position.y - transformed_surface.get_height()/2
            position = left + self.position.x - transformed_surface.get_width()/2, top + self.position.y - transformed_surface.get_height()/2

            rect = transformed_surface.get_rect()
            rect.move(position)

            blit_area = surface.get_rect().clip(rect)
            print(blit_area)
            surface.blit(transformed_surface, position)

    def run_scripts(self, delta):
        self.script(self, delta)

        if self.children != {}:
            for child in self.children.values():
                child.run_scripts(delta)

    def attach_sctipt(self, script):
        self.script = script

    def add_child(self, child):
        self.children[child.name] = child
        child.parent = self
        

    def remove_child(self, child):
        self.children.remove(child)


class Sprite2D(Node2D):
    def __init__(self, name, image_path):
        super().__init__(name)
        self.image = pygame.image.load(os.path.join(image_path)).convert_alpha()
        
        self.width, self.height = self.size = self.image.get_size()

    def draw(self, surface):
        image = pygame.transform.rotozoom(self.image, self.rotation_degrees, self.scale).convert_alpha()
        position = self.position.x - image.get_width()/2 + self.parent.width/2, self.position.y - image.get_height()/2 + self.parent.height/2


        surface.blit(image, position)