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
"""
import pandas as pd

file_path = r'C:\Users\iconf\OneDrive\Documents\VS Code\alumoptimization\Alumopt.xlsx'  # Replace with your actual file path

df = pd.read_excel(file_path, usecols="A:D", header=None, names=['Column A', 'Column B', 'Column C', 'Column D'], engine='openpyxl')

#print(f"DataFrame Shape: {df.shape}")
#print(df.head()) 

#try:
#    print("Value in 4th column (index 3):", int(df.iloc[0, 3]))  # Access the 4th column of first row
#except IndexError:
#    print("IndexError: The DataFrame doesn't have enough columns.")

df['Column A'] = pd.to_numeric(df['Column A'], errors='coerce')  # Handle errors gracefully
df['Column B'] = pd.to_numeric(df['Column B'], errors='coerce')

#print(int(df.iloc[0, 3]))

ext = []
for index, row in df.iterrows():
    ext.extend([int(row['Column A'])] * int(row['Column B']))
print(ext)
print(int(df.iloc[0, 3]))

"""