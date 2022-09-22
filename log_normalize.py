import numpy as np
import pandas as pd
import sys

## Log Normalize:

input = pd.read_csv(sys.argv[1], delimiter="\t")
## To normalize by row swap rows and columns
inputT = input.T
for column in inputT.columns:
    # eliminate negative values by column
    minValue = inputT[column].min()
    if minValue < 0:
        inputT[column] += abs(minValue)
    # log normalize
    inputT[column] = np.log(inputT[column])

input = inputT.T
out_filename = "output.gct"

transformedData = input.to_csv("data_df", sep = "\t")
with open(transformedData, 'r'):
    data = transformedData.read()
with open(out_filename, 'w') as outFile:
    outFile.write(f"#1.2\n{input.shape[0]}\t{input.shape[1]}")
with open(out_filename, 'a') as outFile:
    outFile.write(data)

# Maybe delete transformedData
