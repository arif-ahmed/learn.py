import turtle

# Create a turtle object
hex_turtle = turtle.Turtle()


# Draw a hexagon: 6 sides, 60 degrees each
for _ in range(6):
    hex_turtle.forward(100)  # move forward by 100 units
    hex_turtle.left(60)      # turn left by 60 degrees

# Prevent the window from closing immediately
turtle.done()
