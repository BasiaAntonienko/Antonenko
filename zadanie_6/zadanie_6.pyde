class Trojkat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
    def mytriangle(x1, y1, x2, y2, x3, y3): # lepiej nie używać nazw wbudowanych, bo nie wiemy czy potem używamy naszej metody, czy wbudowanej
        beginShape()
        vertex(x1, y1)
        vertex(x2, y2)
        vertex(x3, y3)
        endShape()
        # ta metoda nie została ani razu użyta
        
class KolorowyTrojkat(Trojkat):
    def sketchKolorowy(self, x, y): # nigdize nie użyłąś zmiennej kolory, to po co ją przekazywać?
         Trojkat.sketch(self, x, y)
         fill(random(300), 0, 0)
         triangle( # tu została użyta wbudowana
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
    malyKolorowyTrojkat.sketchKolorowy(random(500), 50) 
    malyKolorowyTrojkat.sketchKolorowy(random(300),268) 
    duzyKolorowyTrojkat = KolorowyTrojkat(120.0)
    duzyKolorowyTrojkat.sketchKolorowy(random(600), 40) # usunięte argumenty nie były nigdize użyte i nie miały żadnego sensu
    duzyKolorowyTrojkat.sketch(random(300), 300)
    
#1pkt
