import turtle

def tree(branch_len, t, level):
    
    if level > 0:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len * 0.7, t, level - 1)  
        t.left(40)
        tree(branch_len * 0.7, t, level - 1)  
        t.right(20)
        t.backward(branch_len)

def main():

    level = int(input("Enter recursion level: "))  

    # Налаштування вікна та черепашки
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")

    # Малювання фрактала
    tree(75, t, level)

    # Показує вікно і чекає подій користувача
    turtle.mainloop()

if __name__ == "__main__":
    main()
