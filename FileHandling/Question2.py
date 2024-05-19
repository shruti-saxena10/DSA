#Write a dictionary to a file in Python

import json

details={"Name" :"Shruti", "Age":"28"}
#Use json.dumps() for json string
with open("file.txt","w") as output:
    output.write(json.dumps(details))