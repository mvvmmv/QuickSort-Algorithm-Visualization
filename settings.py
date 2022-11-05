class Settings():
    """Class to store settings for the visualisation part"""

    def __init__(self) -> None:
        self.WIDTH = 800
        self.HEIGHT = 250
        self.SHIFT_X = 100
        self.SHIFT_X_NEW = 100
        self.INIT_CIRCLE_X = 0
        self.INIT_CIRCLE_Y = 115
        self.CIRCLE_WIDTH = 50
        self.CIRCLE_HEIGHT = self.CIRCLE_WIDTH
        self.DISTANCE_BETWEEN_CIRCLES = 60
        self.INIT_TEXT_Y = self.INIT_CIRCLE_Y+self.CIRCLE_HEIGHT//2
        self.SHIFT = 25
        self.BUTTON_WIDTH = 10
        # Colors
        self.BACKGROUND_COLOR = '#E5E3E4'
        self.INIT_COLOR = "#4EB9C1"
        self.PIVOT_COLOR = "#1C7173"
        self.TEMP_PIVOT_COLOR = '#BBC6C8'
        self.USERINPUT_BACKGROUND_COLOR = "#FAF7F3"
        self.BUTTON_BACKGROUND_COLOR = self.BACKGROUND_COLOR
        self.TEXT_COLOR = "#0A1919"

    def getInitXCoord(self, index):
        '''Calculates initial X coordinate of the circle'''
        return self.SHIFT_X_NEW+index*self.DISTANCE_BETWEEN_CIRCLES
