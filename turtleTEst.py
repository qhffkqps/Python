import turtle

m = 0


def TurtleMake(tur, col, mov, rad):
    global m
    tur.color(col)
    tur.circle(int(rad))
    m = int(m) + 50
    t.goto(m, 0)
    return tur


while True:
    c = input("색깔 입력 :>")
    if c == 'q':
        print("종료")

    else:
        m = input("이동거리 설정 :>")
        r = input("반지름은?:>")
        print("=========================")
        t = turtle.Turtle()

TurtleMake(t, c, m, r)

turtle.mainloop()
turtle.bye()
