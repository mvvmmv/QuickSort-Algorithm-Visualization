class ElementCircle:
    '''Class for circle elements'''

    # Keep each instance of the class as an attribute of the class.
    instances = []
    # Keep pivots.
    pivots = []

    def __init__(self, canvas, settings, x, y, init_color):
        '''Initialize the circle element'''

        self.canvas = canvas
        self.circle_id = canvas.create_oval(x,
                                            y,
                                            x+settings.CIRCLE_WIDTH,
                                            y+settings.CIRCLE_HEIGHT,
                                            fill=init_color,
                                            outline=init_color)
        self.x = x
        self.y = y
        self.instances.append(self)

    def move(self, x1New, y1New):
        '''Get current coordinates from canvas,
        save them to attributes and perform moving to
        new coordinates'''

        coordinates = self.canvas.coords(self.circle_id)
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.canvas.move(self.circle_id,
                         x1New - coordinates[0],
                         y1New - coordinates[1])

    def set_color(self, color):
        '''Set colors of the circle'''

        self.canvas.itemconfig(self.circle_id,
                               fill=color,
                               outline=color)
