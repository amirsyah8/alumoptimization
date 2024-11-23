import pandas as pd
#ini file excell
global_vars = {}

# Assuming your data is in the range A1:D100
df = pd.DataFrame(xl("A1:D300"))  # Read data from Excel range
df.columns = ['Column A', 'Column B', 'Column C', 'Column D']

# Convert 'Column A' and 'Column B' to numeric, replacing errors with NaN
df['Column A'] = pd.to_numeric(df['Column A'], errors='coerce')
df['Column B'] = pd.to_numeric(df['Column B'], errors='coerce')

# Fill NaN values with a default value (e.g., 0)
df['Column A'] = df['Column A'].fillna(0)
df['Column B'] = df['Column B'].fillna(0)

ext = []
for index, row in df.iterrows():
    ext.extend([int(row['Column A'])] * int(row['Column B']))

cutLi = []
cutLiExt = []
#rawMate = 6100
rawMate = int(xl("D1"))
spare =  int(xl("D2"))

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
                
global_vars['cutLi'] = cutLi
global_vars['cutLiExt'] = cutLiExt
global_vars['rawMate'] = rawMate
global_vars['calcExt'] = calcExt

cExt = 0
for extSubList in cutLiExt:
    cExt+=1
    print(f"{cExt}",end=" ")
    print(extSubList)
f"\nQty alum Length {rawMate}mm need : {len(cutLi)}\n"

#xl("F5").value = cutLiExt