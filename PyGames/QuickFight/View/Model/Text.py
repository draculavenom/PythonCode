from Model.SharedResources import SharedResources

class Text:
    def __init__(self, screen, name = "Text", y = 0, x = 0, color = "PURPLE"):
        self.name = name
        self.textColor = color
        self.x = x
        self.y = y
        self.resources = SharedResources()
        self.screen = screen
    
    def show(self):
        label_text = self.resources.label_font.render(self.name, True, self.resources.colorsMap[self.textColor])
        self.screen.blit(label_text, (self.x,self.y))