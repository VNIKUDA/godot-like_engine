import pygame
pygame.init()

Vector2 = pygame.Vector2
class Scene():
    def __init__(self):
        self.children = {}
        self.position = Vector2(0, 0)
        self.width, self.height = (0, 0)

        self.script = lambda self, delta: "pass"

    def attach_sctipt(self, script):
        self.script = script

    def run_scripts(self, delta):
        self.script(self, delta)

        if self.children != {}:
            for child in self.children.values():
                child.run_scripts(delta)

    def add_child(self, child):
        self.children[child.name] = child
        child.parent = self

    def remove_child(self, child):
        self.children.remove(child)

    def draw(self, surface):
        for child in self.children.values():
            child.draw(surface)
            
            