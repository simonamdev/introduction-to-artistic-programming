circles = 3
circle_width = 50

centre_x, centre_y = 0, 0

# This runs only once
def setup():
    size(800, 600)
    fill(127, 255, 127)

# This runs once per frame
def draw():
    background(255)
    draw_circles()
    
def draw_circles():
    for i in range(-circles, circles + 1):
        circle_x = centre_x + (i * circle_width)
        ellipse(circle_x, centre_y, circle_width, circle_width)
    for i in range(-circles, circles + 1):
        circle_y = centre_y + (i * circle_width)
        ellipse(centre_x, circle_y, circle_width, circle_width)

def mouseMoved():
    global centre_x, centre_y
    centre_x, centre_y = mouseX, mouseY