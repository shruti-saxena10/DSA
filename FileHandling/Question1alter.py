#Read content from one file and write it into another file

with open("Output_file.txt","w") as output:
    with open("Hello.txt", "r") as input:

        output.write(input.read())

output.close()