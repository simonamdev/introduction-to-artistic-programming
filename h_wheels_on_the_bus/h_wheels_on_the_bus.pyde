bus_x, bus_y = 0, 0

# This runs only once
def setup():
    size(800, 600)

# This runs once per frame
def draw():
    background(255)
    draw_bus(bus_x, bus_y)
    
def draw_bus(x, y):
    fill(255, 255, 0) # R, G, B
    # Add the body
    rect(x, y, 300, 150)
    
    # Add the wheels
    fill(0) # Brightness
    ellipse(x + 75, y + 150, 100, 100)
    ellipse(x + 225, y + 150, 100, 100)

def mouseMoved():
    global bus_x, bus_y
    bus_x = mouseX
    bus_y = mouseY