import pygame, os
pygame.init()

Vector2 = pygame.Vector2

# Клас Node2D, працює як група
class Node2D():
    def __init__(self, name):
        self.name = name
        self.parent = None

        self.children = {}
        self.position = pygame.Vector2(0, 0)
        self.rotation_degrees = 0
        self.scale = 1

        self.width, self.height = self.size = (100, 100)

        self.surface = pygame.Surface((self.width * 2, self.height * 2), flags=pygame.SRCALPHA) # 

    def upscale(self, scale):
        self.scale *= scale

    def rotate(self, rotation_degrees):
        self.rotation_degrees += rotation_degrees

    def move(self, offset: Vector2):
        x, y = self.position
        self.position += offset

    def draw(self, surface):
        children = self.children.values()
        max_surf_size = max([(child.width * child.scale, child.height * child.scale) for child in children])
        if self.size != max_surf_size:
            self.width, self.height = self.size = max_surf_size
            self.surface = pygame.transform.scale(self.surface, (self.width*2, self.height*2))

        for child in children:
            child.draw(self.surface)

        transformed_surface = pygame.transform.rotozoom(self.surface, self.rotation_degrees, self.scale)
        position = self.position.x - transformed_surface.get_width()/2, self.position.y - transformed_surface.get_height()/2
        surface.blit(transformed_surface, position)


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
        image = pygame.transform.rotozoom(self.image, self.rotation_degrees, self.scale)
        position = self.position.x + image.get_width()/2, self.position.y + image.get_height()/2

        surface.blit(image, position)