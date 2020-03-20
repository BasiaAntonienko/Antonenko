def setup():
  size(500, 500)
  c = color(200,0,0)
  stroke(c)
  fill(c)
  rectMode(CORNER)
def draw():
    rect(mouseX,40, height, width)
    print ( mouseX, mouseY, mousePressed)
    line (20,mouseX, 60, mouseY)
    clear();
    
    if mousePressed:
        line (mouseX, mouseY, 50, 60)
        print (mouseX, mouseY, 50, 60)
    else:
        rect( mouseX, 30, mouseY, 40)
 
# poprawnie: 2pkt    

        

    
   
    
        
