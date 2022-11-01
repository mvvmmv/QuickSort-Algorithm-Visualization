class TextCircle():
    '''Class for text elements'''

    # Keep each instance of the class as an attribute of the class.
    instances = []

    def __init__(self, canvas, settings, x, y, text):
        '''Initialize the text element'''

        self.canvas = canvas
        self.text_id = canvas.create_text(x,
                                          y,
                                          text=text,
                                          font=('Helvetica', '16', 'bold'),
                                          fill=settings.TEXT_COLOR)
        self.x = x
        self.y = y
        self.instances.append(self)

    def move(self, x1New, y1New):
        '''Get current coordinates from canvas,
        save them to attributes and perform moving to
        new coordinates'''

        coordinates = self.canvas.coords(self.text_id)
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.canvas.move(self.text_id,
                         x1New - coordinates[0],
                         y1New - coordinates[1])
