import json

data = {
    "data":[1,2,3,4,5,6]
}

''' file = open("test.txt","w")
json.dump(data,file)
file.close() '''
open("test.txt","w").write("").close()
file = open("test.txt")
print(json.load(file)["data"])