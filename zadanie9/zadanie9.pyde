def setup ():
    global photo
    photo = loadImage ("kot.jpg")
    size (500, 500)
    noFill()
def draw():
    try:
        image(photo, height/2, width/2, 200, 200) 
    except:
        stroke("#FF7F50")
        text("Nie udalo sie wczytac zdjecia", 100, 25)
    else:
        stroke("#66CDAA")
    finally:
        rect(height/2-1, width/2-1, 200, 200)
        
#2pkt
