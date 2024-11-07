ext = [5600, 5600, 5600, 1200, 1200, 400, 400, 2500, 2500, 2500, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
cutLi = []
rawMate = 5600


for i in range(len(ext)):  # nak loop ext
    if len(cutLi) == 0: # check sekiranya cutlist  permulaan
        cutLi = [[rawMate]]  # tambah dulu 1 batang 6100

    count = 0  # Counter to track the number of elements in each sublist
    while count < len(cutLi):
        if cutLi[count][-1] - ext[i] >= 0:
            newBalance = cutLi[count][-1] - ext[i]
            cutLi[count][-1] = ext[i]
            cutLi[count].append(newBalance)        
            break
        else:
            count += 1
            if count == len(cutLi):
                cutLi.append([rawMate])


# Print the result
print(len(cutLi))
for sublist in cutLi:
    print(sublist)
