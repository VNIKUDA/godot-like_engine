from .nodes import Node2D, Sprite2D
import pygame
pygame.init()

class Scene():
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def draw(self, surface):
        for child in self.children:
            if isinstance(child, Node2D):
                child.draw(surface)

            if isinstance(child, Sprite2D):
                image = pygame.transform.rotozoom(child.image, child.rotation_degrees, child.scale)
                surface.blit(image, child.position)
            
            