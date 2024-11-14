import turtle

# Set up the screen and window
screen = turtle.Screen()
screen.setup(width=500, height=500)
screen.bgcolor("white")

# Create a turtle object to draw the donut
donut = turtle.Turtle()
donut.speed(1)  # Set the speed of the drawing turtle

# Define the colors for the donut and its outline
fill_color = "light yellow"
outline_color = "dark orange"

# Draw the outer edge of the donut
donut.penup()
donut.goto(-250, 0)  # Position the turtle to the top left corner
donut.pendown()
donut.fillcolor(outline_color)
donut.begin_fill()
for i in range(36):
    donut.forward(100)  # Draw a segment of the donut outline
    donut.left(10)
donut.end_fill()

# Fill in the center of the donut
donut.penup()
donut.goto(-250, -100)  # Position the turtle to the bottom left corner
donut.pendown()
donut.fillcolor(fill_color)
donut.begin_fill()
for i in range(36):
    donut.forward(70)  # Draw a smaller segment of the donut center
    donut.left(10)
donut.end_fill()

# Make the donut spin
while True:
    donut.right(1)  # Rotate the turtle 1 degree