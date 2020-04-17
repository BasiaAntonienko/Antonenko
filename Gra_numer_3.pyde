def setup():
    global wtekstu, lit1, lit2, x1, y1, x2, y2, kolor1, kolor2, a, wcisniety
    size(700,500)
    lit1 = "b"
    lit2 = "a"
    x1 = 300
    y1 = 250
    x2 = 400
    y2 = 250
    wtekstu = 100
    kolor1 = "#CC527A"
    kolor2 = "#A8A7A7"
    noFill()
    stroke(kolor1)
    rect(x1, y1-10, 175, 100, 10)
    textSize(wtekstu)
    a = False
    wcisniety = False
    
    
def draw():
    global a
    global wcisniety
    n = najechanie(x1, y1)
    w = wcisniety
    if a == True:
        n, w = w, n
    
    if n == True:
        fill(kolor1)
    else:
        fill(kolor2)
    text(lit1.upper(), x1, y1+75)
    if w == True:
        fill(kolor1)
    else:
        fill(kolor2)
    text(lit2.upper(), x2, y2+75)
    n = False
    w = False

def keyPressed():
    global a
    global wcisniety
    if keyCode in [LEFT, RIGHT]:
        a = True
    if key == lit2:
        wcisniety = True
def keyReleased():
    global a
    global wcisniety
    if keyCode in [LEFT, RIGHT]:
        a = False
    if key == lit2:
        wcisniety = False

def najechanie(x, y):
    if mouseX >= x and mouseX <= x + wtekstu:
        if mouseY >= y and mouseY <= y + wtekstu:
            return True
    return False
