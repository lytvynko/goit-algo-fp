import turtle

def draw_tree(branch_len, t, recursion_depth):
    if recursion_depth > 0:
        t.forward(branch_len)
        t.right(25)
        draw_tree(branch_len - 15, t, recursion_depth - 1)
        t.left(50)
        draw_tree(branch_len - 15, t, recursion_depth - 1)
        t.right(25)
        t.backward(branch_len)

def main(recursion_depth=5):
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    draw_tree(100, t, recursion_depth)
    my_win.exitonclick()

main(7)