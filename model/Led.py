from constants.LedConstants import ColorPosition as PosL
class Led:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    
    def __init__(self, colors):
        self.red = colors[PosL.R_POS]
        self.green = colors[PosL.G_POS]
        self.blue = colors[PosL.B_POS]
        
        
    def setColor(self, colors):
        self.red = colors[PosL.R_POS]
        self.green = colors[PosL.G_POS]
        self.blue = colors[PosL.B_POS]
    