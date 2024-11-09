import pandas as pd

# Assuming your data is in the range A1:D100
df = pd.DataFrame(xl("A1:D200"))  # Read data from Excel range
df.columns = ['Column A', 'Column B', 'Column C', 'Column D']

# Convert 'Column A' and 'Column B' to numeric, replacing errors with NaN
df['Column A'] = pd.to_numeric(df['Column A'], errors='coerce')
df['Column B'] = pd.to_numeric(df['Column B'], errors='coerce')

# Fill NaN values with a default value (e.g., 0)
df['Column A'] = df['Column A'].fillna(0)
df['Column B'] = df['Column B'].fillna(0)

# Generate the 'ext' list from Column A and Column B values
ext = []
for index, row in df.iterrows():
    ext.extend([int(row['Column A'])] * int(row['Column B']))

# Initialize cut list and raw material value (assuming Column D holds the raw material length)
rawMate = int(xl("D1"))  # Access Column D as the raw material length

# Cut calculation loop
cutLi = []
for i in range(len(ext)):
    if len(cutLi) == 0:
        cutLi = [[rawMate]]  # Initializing the cut list with raw material

    count = 0
    while count < len(cutLi):
        if cutLi[count][-1] - ext[i] >= 0:
            newBalance = cutLi[count][-1] - ext[i]
            cutLi[count][-1] = ext[i]
            cutLi[count].append(newBalance)
            break
        else:
            count += 1
            if count == len(cutLi):
                cutLi.append([rawMate])  # Add a new cut if no space left

# Prepare the result for Excel (displaying the cut list and quantity needed)
cutLi_str = str(cutLi)  # Convert cutLi list to string for display
quantity_needed = f"Quantity needed: {len(cutLi)}"  # String to display quantity needed

# Output the results to Excel
xl("E1").value = cutLi_str  # Output the cut list in cell E1
xl("E2").value = quantity_needed  # Output the quantity needed in cell E2

# Optionally, you can print the result to the console as well
print(cutLi_str)
print(quantity_needed)
