import turtle
import random

# Set up the screen with pastel yellow background
screen = turtle.Screen()
screen.bgcolor("#FFFACD")  # Pastel yellow (Lemon Chiffon)
screen.setup(width=800, height=800)

pen = turtle.Turtle()
pen.speed(5)

def draw_vase():
    """
    Draws a detailed vase using a series of points.
    The vase is drawn from the bottom (-200) up to its mouth.
    """
    pen.up()
    pen.goto(-75, -200)   # bottom left
    pen.down()
    pen.color("blue")
    pen.begin_fill()
    pen.goto(-100, -150)   # left-side curve
    pen.goto(-40, -12.5)   # rising toward the vase mouth
    pen.goto(-30, -12.5)   # left edge of the vase mouth
    pen.goto(30, -12.5)    # right edge of the vase mouth
    pen.goto(40, -12.5)    # continue right
    pen.goto(100, -150)    # right-side curve
    pen.goto(75, -200)     # bottom right
    pen.goto(-75, -200)    # close the shape
    pen.end_fill()

def draw_flower(x, y, scale=8):
    """
    Draws a flower at (x, y) with six rounded petals.
    The size of the flower is controlled by the 'scale' factor.
    """
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.color("red")
    pen.pensize(2)
    pen.begin_fill()
    # Draw six petals; each petal is drawn using two arcs.
    for _ in range(6):
        pen.circle(20 * scale, 60)  # first arc of petal
        pen.left(120)
        pen.circle(20 * scale, 60)  # second arc of petal
        pen.left(60)
    pen.end_fill()

def draw_stem(x, y, length, thickness):
    """
    Draws a stem starting at (x, y) going downward.
    'length' and 'thickness' are adjustable.
    """
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.color("green")
    pen.pensize(thickness)
    pen.setheading(270)  # Point directly downward
    pen.forward(length)

# Draw the vase first.
draw_vase()

# The vase mouth in the drawing is along y = –12.5,
# but we now want the stems to start a bit higher (at y = –5)
# so that they appear to originate exactly from the vase lip.
stem_origins = [(-30, 85), (0, 85), (30, 85)]

for pos in stem_origins:
    x, y = pos
    # Choose a random stem length (so that the flower heights vary)
    stem_length = random.randint(80, 120)  # e.g., between 80 and 120 units
    # Choose a random thickness for the stem
    thickness = random.randint(5, 10)
    draw_stem(x, y, stem_length, thickness)
    
    # Vary the flower size a bit too.
    flower_scale = random.uniform(1, 1.5)
    # The flower will be drawn at the top of the stem.
    draw_flower(x, y, scale=flower_scale)

pen.hideturtle()
turtle.done()
