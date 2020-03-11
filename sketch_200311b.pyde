def setup():
    size(400,600)
    stroke(255, 0, 0)
    strokeWeight (3)
    global natezenie
    natezenie = 0
    global index
    index = 0
    frameRate(5)
    global szerokosc
    szerokosc = 0
    natezenie = 0
def draw():
    global index
    global natezenie
    natezenie = natezenie + 1
    if natezenie ==255:
        natezenie = 0
    line(mouseX, mouseY, width/3, height/3)
    fill(0,0,natezenie, 120)
    rect(20,40,120,140)
    fill(0,natezenie,0,120)
    global szerokosc
    szerokosc = szerokosc + 1
    rect(szerokosc, 100,100,100)
    
    slownik = {"czerwony":(255,0,0), "niebieski":(0,0,255), "zielony":(0,255,0)}
    print(slownik["zielony"])
    stroke(*slownik["zielony"])
    lista = []
    for nazwa, wartosc in slownik.items():
        lista.append(wartosc)
    index += 1
    if index==3:
        index = 0
    stroke(*lista[index])
    
    def mousePressed():
        exit()
