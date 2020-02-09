import turtle


def draw_petal():
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_advanced():
    draw_flower()
    turtle.right(90)
    turtle.up
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down


def draw_flower_bed():
    turtle.up
    turtle.forward(200)
    turtle.left(180)
    turtle.down
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()


draw_flower_bed()
turtle.done()
