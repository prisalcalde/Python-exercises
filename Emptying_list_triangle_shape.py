a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def triangle():
    while a != []:
        a.pop()
        print(a)
    else:
        print("The list is now empty")

triangle()
