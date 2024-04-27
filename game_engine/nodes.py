import pygame, os
pygame.init()


class Node2D():
    def __init__(self):
        self.children = []
        self.position = (0, 0)
        self.rotation_degrees = 0
        self.scale = 1

        self.size = (0, 0)

        self.surface = pygame.Surface((100, 100))

    # def transform(self, position=None, rotation_degrees=None, scale=None):
    #     if position:
    #         self.position = position

    #     if rotation_degrees:
    #         self.rotation_degrees = rotation_degrees

    #     if scale:
    #         self.scale = scale

    def upscale(self, scale):
        self.scale *= scale

    def rotate(self, rotation_degrees):
        self.rotation_degrees += rotation_degrees

    def move(self, position):
        x, y = self.position
        self.position = x + position[0], y + position[1]

    def draw(self, surface):
        for child in self.children:
            if isinstance(child, Node2D):
                child.draw(surface)

            if isinstance(child, Sprite2D):
                image = pygame.transform.rotozoom(child.image, child.rotation_degrees, child.scale)
                surface.blit(image, child.position)

    def resize_if_needed(self, child):
        size = self.size
        w, h = child.size

        if w > size[0]:
            size = w, size[1]
        if h > size[1]:
            size = size[0], h 

        if self.size != size:
            self.size = size
            self.surface = pygame.Surface(self.size)


    def add_child(self, child):
        self.children.append(child)
        self.resize_if_needed(child)
        

    def remove_child(self, child):
        self.children.remove(child)
        self.resize_if_needed(child)


class Sprite2D(Node2D):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(os.path.join(image_path))
        
        self.width, self.height = self.size = self.image.get_size()