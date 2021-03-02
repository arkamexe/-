import json

#getting the file name
f = input("Enter the name of your file.\n")
v = f.find(".txt")
if v == -1:
    f = f"{f}.txt".format(f)

#reading the file and getting the contents
with open(f) as file:
    fileData = file.read()

#converting file's contents from string to dict
jsonData = json.loads(fileData)

#checking the depth
def check(val, currDepth):
    if isinstance(val, dict):
        currDepth += 1
        for x in val.values():
            currDepth = check(x, currDepth)
        return currDepth
    elif isinstance(val, list):
        currDepth += 1
        for i in range(len(val)):
            currDepth = check(val[i], currDepth)
        return currDepth

    return currDepth

#checking the file and start search for max depth
def fd(jsonData):
    maxDepth = 0
    currDepth = 0
    for val in jsonData.values():
        currDepth = check(val, currDepth)
        maxDepth = max(maxDepth, currDepth)
        currDepth = 1

    return maxDepth

print("The max depth found is: ", fd(jsonData))
