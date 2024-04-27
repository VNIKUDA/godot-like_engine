class GameConfig():
    _instance = None
    
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            cls._instance.set_window_size(1280, 720)
    
    def set_window_size(self, width, height):
        self.width = width
        self.height = height
