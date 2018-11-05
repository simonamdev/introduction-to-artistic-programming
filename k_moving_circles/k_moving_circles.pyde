circle_width = 50
circle_x, circle_y = 0, 0
direction = 1
move_amount = 20

# This runs only once
def setup():
    size(800, 800)
    fill(255, 255, 0)

# This runs once per frame
def draw():
    background(255)
    draw_circle()
    move_circle()
    
def draw_circle():
    ellipse(circle_x, circle_y, circle_width, circle_width)

def move_circle():
    global circle_x, circle_y, direction, move_amount
    if is_out_of_bounds(circle_x, circle_y):
        direction = -direction
    circle_x += direction * move_amount
    circle_y += direction * move_amount

def is_out_of_bounds(x, y):
    return (x < 0 and y < 0) or (x > width and y > height)