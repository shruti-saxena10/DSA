#Read content from one file and write it into another file


with open("Hello.txt", "r") as file1:
    with open("Intro.txt","w") as file2:

        for line in file1:
            file2.write(line)