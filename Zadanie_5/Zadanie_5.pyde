global cWidth
global cHeight
cWidth=600
cHeight=600
class character(object):
    def __init__(self):
          self.x=100
          self.y=100
          self.up=0
          self.down=0
          self.left=0
          self.right=0
          self.speed=4
          self.w = 20
          self.h = 20
    def show(self):
            fill(200);
            rect(100, 100, 400, 400);
            fill(0,0,255);
            rect(439,465,60,35);
            fill(0,0,255);
            rect(100,100,60,35);
            fill(0,0,255);
            rect(100,100,60,35);
            fill(255,0,0);
            rect(200,100,20,350);
            fill(255,0,0);
            rect(275,150,20,350);
            fill(255,0,0);
            rect(350,100,20,350);
            fill(0);
            rect(self.x,self.y,self.w,self.h)
                            
    def update(self):
        self.x = self.x + (self.right - self.left)*self.speed
        self.y = self.y + (self.down - self.up)*self.speed
        if not(self.x >= 100):
            self.x=100
        if not(self.y >= 100):
            self.y=100
        if not(self.x <= 500-self.w):
            self.x=500-self.w
        if not(self.y <= 500-self.h):
            self.y=500-self.h
        if self.x>200-self.w and self.x<218 and self.y<450:
            self.x=100
            self.y=100
        if self.x>279-self.w and self.x<295 and self.y>131:
            self.x=100
            self.y=100
        if self.x>350-self.w and self.x<368 and self.y<450:
            self.x=100
            self.y=100
        if self.x>=385 and self.x<=390 and self.y>131:
            self.x=385        
            textSize(25);
            text("Przezroczysta ściana?", 150, 300); 
            fill(0, 102, 153);
def mouseClicked():
    clear()        
                                                                                                        
def setup():
    size(cWidth,cHeight)
    global c
    c=character() # miały być utworzone z klasy dwa obiekty

def draw():
    background(100)
    c.show()
    c.update()
        
def keyPressed():
    if keyCode == UP:
        c.up = 1
    if keyCode == DOWN:
        c.down = 1
    if keyCode == RIGHT:
        c.right = 1
    if keyCode == LEFT:
            c.left = 1
    
def keyReleased():
    if keyCode == UP:
        c.up = 0
    if keyCode == DOWN:
        c.down = 0
    if keyCode == RIGHT:
        c.right = 0
    if keyCode == LEFT:
            c.left = 0
# przydało by się po wjchaniu na końcowy prostokąt wyświetlić informację i zamknąć program :)
# plus do aktywności za kreatywność
# choć samo sterowanie widziałąm już takie samo w nie wiem ilu programach...
#1,75pkt
