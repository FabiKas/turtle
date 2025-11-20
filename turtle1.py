import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

inp = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

counter = 0

if inp == 1:
    num_sides = 3
    while counter < 20:
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)

        reduction_ratio = 0.618

        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]

        counter += 1

if inp == 2:
    num_sides = 4
    while counter < 20:
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)

        reduction_ratio = 0.618

        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]

        counter += 1

if inp == 3:
    num_sides = 5
    while counter < 20:
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)

        reduction_ratio = 0.618

        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]

        counter += 1

if inp == 4:
    while counter < 20:
        num_sides = random.randint(3,5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)

        reduction_ratio = 0.618

        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]

        counter += 1

if inp == 5:
    num_sides = 3
    while counter < 20:

        size = random.randint(80, 180)
        orientation = random.randint(0, 360)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(2, 8)

        draw_polygon(num_sides, size, orientation, location, color, border_size)

        reduction_ratio = 0.7

        local_size = size
        local_location = location.copy()

        for i in range(2):
            local_size *= reduction_ratio

            turtle.goto(local_location[0], local_location[1])
            turtle.forward((size - local_size) * 0.25)
            turtle.left(90)
            turtle.forward((size - local_size) * 0.25)
            turtle.right(90)

            local_location = [turtle.xcor(), turtle.ycor()]

            draw_polygon(num_sides, local_size, orientation, local_location, color, border_size)

        counter += 1

if inp == 6:
    num_sides = 4
    while counter < 20:

        size = random.randint(80, 180)
        orientation = random.randint(0, 360)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(2, 8)

        draw_polygon(num_sides, size, orientation, location, color, border_size)
        
        reduction_ratio = 0.7

        local_size = size
        local_location = location.copy()

        for i in range(2):
            local_size *= reduction_ratio

            turtle.goto(local_location[0], local_location[1])
            turtle.forward((size - local_size) * 0.25)
            turtle.left(90)
            turtle.forward((size - local_size) * 0.25)
            turtle.right(90)

            local_location = [turtle.xcor(), turtle.ycor()]

            draw_polygon(num_sides, local_size, orientation, local_location, color, border_size)

        counter += 1

if inp == 7:
    num_sides = 5
    while counter < 20:

        size = random.randint(80, 180)
        orientation = random.randint(0, 360)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(2, 8)

        draw_polygon(num_sides, size, orientation, location, color, border_size)
        
        reduction_ratio = 0.7

        local_size = size
        local_location = location.copy()

        for i in range(2):
            local_size *= reduction_ratio

            turtle.goto(local_location[0], local_location[1])
            turtle.forward((size - local_size) * 0.25)
            turtle.left(90)
            turtle.forward((size - local_size) * 0.25)
            turtle.right(90)

            local_location = [turtle.xcor(), turtle.ycor()]

            draw_polygon(num_sides, local_size, orientation, local_location, color, border_size)

        counter += 1

if inp == 8:

    while counter < 20:
        num_sides = random.randint(3, 5)
        size = random.randint(80, 180)
        orientation = random.randint(0, 360)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(2, 8)

        draw_polygon(num_sides, size, orientation, location, color, border_size)
        
        reduction_ratio = 0.7

        local_size = size
        local_location = location.copy()

        for i in range(2):
            local_size *= reduction_ratio

            turtle.goto(local_location[0], local_location[1])
            turtle.forward((size - local_size) * 0.25)
            turtle.left(90)
            turtle.forward((size - local_size) * 0.25)
            turtle.right(90)

            local_location = [turtle.xcor(), turtle.ycor()]

            draw_polygon(num_sides, local_size, orientation, local_location, color, border_size)

        counter += 1

if inp == 9:

    while counter < 20:
        num_sides = random.randint(3, 5)
        size = random.randint(80, 180)
        orientation = random.randint(0, 360)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(2, 8)

        draw_polygon(num_sides, size, orientation, location, color, border_size)
        
        reduction_ratio = 0.7

        local_size = size
        local_location = location.copy()

        layer = random.randint(1, 3)

        for i in range(layer):
            if i == 0:
                continue
            else:
                local_size *= reduction_ratio

                turtle.goto(local_location[0], local_location[1])
                turtle.forward((size - local_size) * 0.25)
                turtle.left(90)
                turtle.forward((size - local_size) * 0.25)
                turtle.right(90)

                local_location = [turtle.xcor(), turtle.ycor()]

                draw_polygon(num_sides, local_size, orientation, local_location, color, border_size)

        counter += 1
else:
    print("Invalid Input")

turtle.done()