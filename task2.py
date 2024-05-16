import turtle


screen = turtle.Screen()
screen.bgcolor("blue")
t = turtle.Turtle()
t.color("white")
t.speed(0)
t.left(90)
t.up()
t.bk(100)
t.down()


def draw_pifagor_tree(t, branch_length, angle, level):
    if level == 0:
        return
    t.fd(branch_length)
    t.right(angle)
    draw_pifagor_tree(t, 0.7 * branch_length, angle, level - 1)
    t.left(2 * angle)
    draw_pifagor_tree(t, 0.7 * branch_length, angle, level - 1)
    t.right(angle)
    t.bk(branch_length)


def main():
    level = int(input("Введіть рівень рекурсії: "))
    draw_pifagor_tree(t, 100, 50, level)


t.hideturtle()


if __name__ == "__main__":
    main()
