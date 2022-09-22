import numpy as np
import pandas as pd
import sys

## Log Normalize:

input = pd.read_csv(sys.argv[1], delimiter="\t", skiprows=2)

## To normalize by row swap rows and columns
inp_no_desc = input.drop(['Name','Description'], axis = 1)
inputT = inp_no_desc.T

for column in inputT.columns:
    # eliminate negative values by column
    minValue = inputT[column].min()
    if minValue < 0:
        inputT[column] += abs(minValue)
    # log normalize
    inputT[column] = np.log(inputT[column])
output = inputT.T

# Add back in non-numeric columns
columns = input.columns
for i in range(2):
    output.insert(i, columns[i], input[columns[i]])

out_filename = "output.gct"
output.to_csv("data_df", sep = "\t", index= False)

with open("data_df", 'r') as transformedData:
    data = transformedData.read()
with open(out_filename, 'w') as outFile:
    outFile.write(f"#1.2\n{input.shape[0]}\t{input.shape[1]-2}\n")
with open(out_filename, 'a') as outFile:
    outFile.write(data)

# Maybe delete transformedData
