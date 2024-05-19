with open("Hello.txt", "r") as file:

    while True:
        c=file.read(5)
        if not c:
            break

        print(c)

