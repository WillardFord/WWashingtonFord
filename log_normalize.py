import numpy as np
import pandas as pd
import argparse
#import gp

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--filename",
                    type=str,
                    help="Name of the file to be read")
parser.add_argument("-o", "--output_filename",
                    type=str,
                    help="The basename to use for output file",
                    default='logNormal.gct')

args = parser.parse_args()

## Log Normalize:

input = pd.read_csv(args.filename, delimiter="\t")
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
#gpserver = gp.GPServer('https://cloud.genepattern.org/gp','myusername', 'mypassword')
out_filename = parser.output_filname
if not out_filename.endswith('.gct'):
        out_filename = out_filename + '.gct'

transformedData = input.to_csv("data_df", sep = "\t")
with open(transformedData, 'r'):
    data = transformedData.read()
with open(out_filename, 'w') as outFile:
    outFile.write(f"#1.2\n{input.shape[0]}\t{input.shape[1]}")
with open(out_filename, 'a') as outFile:
    outFile.write(data)

# Maybe delete transformedData