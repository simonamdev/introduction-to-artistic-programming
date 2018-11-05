circles_per_row = 10

# This runs only once
def setup():
    size(800, 600)

# This runs once per frame
def draw():
    background(255)
    fill(0, 255, 0)
    draw_row()

def draw_row():
    circle_width = width / circles_per_row
    for i in range(0, circles_per_row):
        circle_x = i * circle_width
        ellipse(circle_x + circle_width / 2, height / 2, circle_width, height)