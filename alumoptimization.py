ext = [6090, 5600, 5600, 5600, 1200, 1200, 400, 400, 2500, 2500, 2500, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
cutLi = []
rawMate = 6100
spare = 25
calcExt = [x + spare if x + spare <= rawMate else rawMate for x in ext]

for i in range(len(calcExt)):
    if len(cutLi) == 0:
        cutLi = [[rawMate]]  # Initializing the cut list with raw material

    count = 0
    while count < len(cutLi):
        if cutLi[count][-1] - calcExt[i] >= 0:
            newBalance = cutLi[count][-1] - calcExt[i]
            cutLi[count][-1] = calcExt[i]
            cutLi[count].append(newBalance)
            break
        else:
            count += 1
            if count == len(cutLi):
                cutLi.append([rawMate])  # Add a new cut if no space left


# Print the result
print(len(cutLi))
for sublist in cutLi:
    print(sublist)
