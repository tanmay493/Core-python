def show():
    x=10
    def display():
        nonlocal x
        x=x+5
        print(x)
    display()
show()
# print(x)        