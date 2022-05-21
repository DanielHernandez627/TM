import json

with open("nuevaTabla.json", "r") as j:
    mydata = json.load(j)
    for x in range(0,len(mydata)):
        print(x)



