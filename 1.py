import random

#user input and validation
while True:
    sqSide = input("Give the size of each side of the square:\n")
    try:
        sqSide = int(sqSide)
    except:
        print("Please use intergers.\n")
        continue
    if sqSide < 4:
        print("Please enter an interger of value greater or equal to 4.\n")
        continue
    break

#making the table
#step 1 making the list of 1 and 0 and shuffling
sum = sqSide ** 2
table = []
for i in range(sum):
    if i > sum//2:
        table.append(0)
    else:
        table.append(1)

random.shuffle(table)

#making the actual table
rows = sqSide
cols = sqSide
gTable = []
start = 0
end = cols
for i in range(rows):
    gTable.append(table[start:end])
    start += cols
    end += cols


#looping the search 100 times
totalCounter = 0
for e in range(100):
#searching for quadriplets of 1 in the X axis
    for i in range(rows):
        oneCounter = 0
        for j in range(cols):
            if gTable[i][j] == 1:
                oneCounter += 1
            elif gTable[i][j] == 0 and oneCounter >= 4:
                totalCounter += (oneCounter - 3)
                oneCounter = 0
            elif gTable[i][j] == 0:
                oneCounter = 0
        if oneCounter >= 4:
            totalCounter += (oneCounter - 3)

#searching for quadriplets of 1 in the Y axis
    for i in range(cols):
        oneCounter = 0
        for j in range(rows):
            if gTable[j][i] == 1:
                oneCounter += 1
            elif gTable[j][i] == 0 and oneCounter >= 4:
                totalCounter += (oneCounter - 3)
                oneCounter = 0
            elif gTable[j][i] == 0:
                oneCounter = 0
        if oneCounter >= 4:
            totalCounter += (oneCounter - 3)

#searching for quadriplets of 1 in main diagonals
#upper left to lower right
    oneCounter = 0
    for i in range(rows):
        if gTable[i][i] == 1:
            oneCounter += 1
        elif gTable[i][i] == 0 and oneCounter >= 4:
            totalCounter += (oneCounter -3)
            oneCounter = 0
        elif gTable[i][i] == 0:
            oneCounter = 0
    if oneCounter >= 4:
        totalCounter += (oneCounter -3)

#lower left to upper right
    oneCounter = 0
    for i in range(rows - 1, -1, -1):
        if gTable[(rows - 1) - i][i] == 1:
            oneCounter += 1
        elif gTable[(rows - 1) - i][i] == 0 and oneCounter >= 4:
            totalCounter += (oneCounter -3)
            oneCounter = 0
        elif gTable[(rows - 1) - i][i] == 0:
            oneCounter = 0
    if oneCounter >= 4:
        totalCounter += (oneCounter -3)

#rest of the diagonals
#upper left to lower right above main
    possibleDiag = sqSide - 4
    max = sqSide - 1
    for i in range(possibleDiag):
        oneCounter = 0
        for x in range(0, max, 1):
            if gTable[x][x + 1] == 1:
                oneCounter += 1
            elif gTable[x][x + 1] == 0 and oneCounter >= 4:
                totalCounter += (oneCounter - 3)
                oneCounter = 0
            elif gTable[x][x + 1] == 0:
                oneCounter = 0
        if oneCounter >= 4:
            totalCounter += (oneCounter - 3)
        if max > 4:
            max -= 1

#upper left to lower right below main
    for i in range(possibleDiag):
        oneCounter = 0
        for x in range(0, max, 1):
            if gTable[x][x - 1] == 1:
                oneCounter += 1
            elif gTable[x][x - 1] == 0 and oneCounter >= 4:
                totalCounter += (oneCounter - 3)
                oneCounter = 0
            elif gTable[x][x - 1] == 0:
                oneCounter = 0
        if oneCounter >= 4:
            totalCounter += (oneCounter - 3)
        if max > 4:
            max -= 1

#lower left to upper right above main
    max = sqSide - 1
    min = 4
    for i in range(possibleDiag):
        oneCounter = 0
        for x in range(0, i + 4, 1):
            if gTable[(min - 1) - x ][x] == 1:
                oneCounter += 1
            elif gTable[(min - 1) - x][x] == 0 and oneCounter >= 4:
                totalCounter += (oneCounter - 3)
                oneCounter = 0
            elif gTable[(min - 1) - x][x] == 0:
                oneCounter = 0
        if oneCounter >= 4:
            totalCounter += (oneCounter - 3)
        if min < max:
            min += 1

#lower left to upper right below main
    min = 4
    for i in range(possibleDiag):
        oneCounter = 0
        for x in range(0, max - i, 1):
            if gTable[max - x][x + i + 1] == 1:
                oneCounter += 1
            elif gTable[max - x][x + i + 1] == 0 and oneCounter >= 4:
                totalCounter += (oneCounter - 3)
                oneCounter = 0
            elif gTable[max - x][x + i + 1] == 0:
                oneCounter = 0
        if oneCounter >= 4:
            totalCounter += (oneCounter - 3)

    random.shuffle(gTable)

#calculating the average and printing it
print(totalCounter)
print("The average of four 1's in row for a square table of size: ",sqSide,"x",sqSide," is: ", totalCounter/100)
