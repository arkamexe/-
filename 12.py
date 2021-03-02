
#getting the file name
f = input("Enter the name of your file.\n")
v = f.find(".txt")
if v == -1:
    f = f"{f}.txt".format(f)

#reading the file and getting the characters
mirroredCharText = ''
with open(f) as file:
    fileData = file.read()
    print(type(fileData))
    for line in fileData:
        for character in line:
#mirroring each character
            mirroredCharText += (chr(128 - ord(character)))

#printing the mirrored text with reverse order
finalText = str(mirroredCharText[::-1])
finalTextUTF8 = finalText.encode()
print(finalTextUTF8)
