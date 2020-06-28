import random
add_library('pdf')

def setup():
    global img,  okulary, okulary2
    size(492,633)
    img = loadImage("zdjecie.jpg")
    imageMode(CORNER)
    beginRecord(PDF, "out1Zdjecie.pdf")
    print(random.random())
    okulary = loadImage("okulary.jpg")
    print(type(img))
    fill(20,255,200)
    
def draw():
    global img, okulary, okulary2
    image(img, 0,0, 492, 633)
    if key == "1":
        image(okulary, 34,165, 400, 400) 
    elif key == "2":
        image(okulary2, 0,180, 450, 470)
    
    
        
def mousePressed():
    endRecord()
    exit()
