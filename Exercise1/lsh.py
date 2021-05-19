import pandas as pd
from itertools import combinations
import collections

#def find_buckets(indices, array):
    #for


SIG2 = pd.DataFrame([
                [1, 2, 1, 1, 2, 5, 4],
                [2, 3, 4, 2, 3, 2, 2],
                [3, 1, 2, 3, 1, 3, 2],
                [4, 1, 3, 1, 2, 4, 4],
                [5, 2, 5, 1, 1, 5, 1],
                [6, 1, 6, 4, 1, 1, 4]
            ],
            columns=["C1", "C2", "C3", "C4", "C5", "C6", "C7"],
            dtype='int64')
SIG2
bands = 3
rows_per_band = int(SIG2.shape[0] / bands) # this only works for multiples here
print("bands", bands, "rows/band", rows_per_band)

my_Sig = SIG2.to_numpy()

band_indices = [x*rows_per_band for x in range(0, bands)]
cols = []
columns = []
for band in band_indices:
    cols = []
    for index in range(0, SIG2.shape[1]):
        col_in_band = []
        for rpb in range(band, band + rows_per_band):
            col_in_band.append(my_Sig[rpb][index])
        cols.append(col_in_band)
    columns.append(cols)
#print(columns)
idx = 1
buckets = []
#print(cols)

buckets = []
for col in columns:
    idx = 1
    bucket = []
    for c in col:
        #bucket = []
        idx1 = 1
        for c1 in col:
            if c == c1:
                if idx != idx1:
                    if(sorted((idx,idx1)) not in bucket):
                        bucket.append(sorted((idx, idx1)))
            idx1+=1
        idx += 1
    buckets.append(bucket)

print(buckets)
