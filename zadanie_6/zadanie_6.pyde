class Trojkat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
    def triangle(x1, y1, x2, y2, x3, y3):
        beginShape()
        vertex(x1, y1)
        vertex(x2, y2)
        vertex(x3, y3)
        endShape()
        
class KolorowyTrojkat(Trojkat):
    def sketchKolorowy(self):
        Trojkat.sketch(self, x, y)
    def sketchKolorowy(self, x, y, kolory):
         Trojkat.sketch(self, x, y)
         fill(random(300), 0, 0)
         triangle(
                   random(x, x+100),
                random(y, y+100),
                random(x, x+250),
                random(y, y+200),
                random(x, x+200),
                random(y, y+360)
                )
    
def setup():
    size(500, 500)
    malyKolorowyTrojkat = KolorowyTrojkat(30.0) 
    malyKolorowyTrojkat.sketchKolorowy(random(500), 50, 5) 
    malyKolorowyTrojkat.sketchKolorowy(random(300),268, 7) 
    duzyKolorowyTrojkat = KolorowyTrojkat(120.0)
    duzyKolorowyTrojkat.sketchKolorowy(random(600), 40, 20)
    duzyKolorowyTrojkat.sketch(random(300), 300) 
