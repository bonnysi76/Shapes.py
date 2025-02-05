import turtle

# Draw a circle with a fixed radius
def draw_circle():
    turtle.circle(50)  # Draw a circle with radius 50

# Draw a square
def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

# Draw a rectangle
def draw_rectangle():
    for _ in range(2):
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)

# Draw an equilateral triangle
def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)

# Draw a pentagon
def draw_pentagon():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)

# Draw a hexagon
def draw_hexagon():
    for _ in range(6):
        turtle.forward(100)
        turtle.right(60)

# Draw a 5-pointed star
def draw_star():
    for _ in range(5):
        turtle.forward(150)
        turtle.right(144)

# Draw a spiral (increasing line lengths)
def draw_spiral():
    length = 5
    for _ in range(50):
        turtle.forward(length)
        turtle.right(20)
        length += 5

# Draw a fractal tree recursively (complex shape)
def draw_fractal_tree(branch_length):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(20)
        draw_fractal_tree(branch_length - 15)
        turtle.left(40)
        draw_fractal_tree(branch_length - 15)
        turtle.right(20)
        turtle.backward(branch_length)

# Main function to ask the user for a shape and draw it
def main():
    # Set the drawing speed to the fastest so you get instant art
    turtle.speed(0)
    # Prompt the user for a shape
    shape = input("Enter a shape (circle, square, rectangle, triangle, pentagon, hexagon, star, spiral, fractal_tree): ").lower()

    # Call the corresponding function based on input
    if shape == "circle":
        draw_circle()
    elif shape == "square":
        draw_square()
    elif shape == "rectangle":
        draw_rectangle()
    elif shape == "triangle":
        draw_triangle()
    elif shape == "pentagon":
        draw_pentagon()
    elif shape == "hexagon":
        draw_hexagon()
    elif shape == "star":
        draw_star()
    elif shape == "spiral":
        draw_spiral()
    elif shape == "fractal_tree":
        # Position the turtle to start drawing the tree upward
        turtle.left(90)
        draw_fractal_tree(100)
    else:
        print("Shape not recognized, bro! Try one of the available shapes.")
    
    turtle.done()  # Keeps the window open

if __name__ == '__main__':
    main()
