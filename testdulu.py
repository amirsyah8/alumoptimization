ext = [6090, 5600, 5600, 5600, 1200, 1200, 400, 400, 2500, 2500, 2500, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
cutLi = []
cutLiExt = []
rawMate = 6100
spare = 25

# Calculate the new values after adding spare
calcExt = [x + spare if x + spare <= rawMate else rawMate for x in ext]

for i in range(len(calcExt)):
    if len(cutLi) == 0:
        cutLi.append([rawMate])  # Initializing the cut list with raw material balance
        cutLiExt.append([])  # Initialize corresponding cut list for original ext values

    count = 0
    while count < len(cutLi):
        # Check if we can fit the current cut in the current list
        if cutLi[count][-1] - calcExt[i] >= 0:
            newBalance = cutLi[count][-1] - calcExt[i]
            cutLi[count][-1] = calcExt[i]
            cutLi[count].append(newBalance)
            cutLiExt[count].append(ext[i])
            break
        else:
            count += 1
            # If no space is left, add a new cut with raw material balance
            if count == len(cutLi):
                cutLi.append([rawMate])
                cutLiExt.append([])

# Print the result
print(f"Number of raw materials used: {len(cutLi)}")
print("Cut lists with remaining balances:")
for sublist in cutLi:
    print(sublist)
print("Original ext values for each cut list:")
for extSubList in cutLiExt:
    print(extSubList)
