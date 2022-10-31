class Settings():
    """Class to store settings for the visualisation part"""
    def __init__(self) -> None:
        self.WIDTH = 800
        self.HEIGHT = 250
        self.SHIFT_X = 100
        self.SHIFT_X_NEW = 100
        self.INIT_CIRCLE_X = 0
        self.INIT_CIRCLE_Y = 100
        self.CIRCLE_WIDTH = 50
        self.CIRCLE_HEIGHT = self.CIRCLE_WIDTH
        self.DISTANCE_BETWEEN_CIRCLES = 60
        self.INIT_COLOR = "GREEN"
        self.PIVOT_COLOR = "BLUE"
        self.INIT_TEXT_Y = self.INIT_CIRCLE_Y+self.CIRCLE_HEIGHT//2
        self.SHIFT = 25
    
    def getInitXCoord(self, index):
        return self.SHIFT_X_NEW+index*self.DISTANCE_BETWEEN_CIRCLES