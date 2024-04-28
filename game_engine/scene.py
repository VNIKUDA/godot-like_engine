from .nodes import Node2D, Sprite2D
import pygame
pygame.init()

class Scene():
    def __init__(self):
        self.children = {}

    def add_child(self, child):
        self.children[child.name] = child
        child.parent = self

    def remove_child(self, child):
        self.children.remove(child)

    def draw(self, surface):
        for child in self.children.values():
            child.draw(surface)
            
            