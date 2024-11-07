"""
import pandas as pd

# Read data from Excel file
df = pd.read_excel('your_file.xlsx', header=None)  # Adjust the path to your Excel file

# Convert the values in the first column to a list
ext = df[0].tolist()

# Print the extracted data
print("Extracted data from Excel:", ext)
"""
ext = [1200, 500, 4090, 3200, 200,110,2900,120]
cutLi = []
rawMate = 6100


for i in range(len(ext)):  # nak loop ext
    if len(cutLi) == 0: # check sekiranya cutlist  permulaan
        cutLi = [[rawMate]]  # tambah dulu 1 batang 6100

    count = 0  # Counter to track the number of elements in each sublist
    while count < len(cutLi):
        if cutLi[count][-1] - ext[i] >= 0:
            newBalance = cutLi[count][-1] - ext[i]
            cutLi[count][-1] = ext[i]
            if newBalance > 0:
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
