# This runs only once
def setup():
    size(800, 600)

# This runs once per frame
def draw():
    background(255)
    
# This runs only when the mouse is moved
def mouseMoved():
    fill(0, 0, 255)
    ellipse(mouseX, mouseY, 50, 50)