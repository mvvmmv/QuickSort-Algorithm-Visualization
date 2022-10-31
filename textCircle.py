class TextCircle():
    
    instances = []
    
    def __init__(self, canvas, x, y, text):
        self.canvas = canvas
        self.text_id = canvas.create_text((x, y), text=text)
        self.x = x
        self.y = y
        self.instances.append(self)
    
    def move(self, x1New, y1New):
        coordinates = self.canvas.coords(self.text_id)
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.canvas.move(self.text_id, x1New - coordinates[0], y1New - coordinates[1])