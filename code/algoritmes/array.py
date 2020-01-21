import numpy as np
import pandas as pd


x = 10
y = 10
wijk = [[0 for i in range(x)] for j in range(y)]
wijk = np.array(wijk)
print(wijk)

edge_coordinate = (3,3)
# slicer = tuple(slice(edge,edge + i) for edge, i in zip(edge_coordinate, ))
wijk[3:6, 3:6] = 1 
print(wijk)

som = np.sum(wijk[3:6, 3:6])
print(som)

# np.savetxt('np.csv', wijk, fmt='%.2f', delimiter=',')
# df = pd.DataFrame(a)
# print(df)
# # df.to_csv('pd.csv', float_format='%.2f', na_rep="NAN!")
# # df.to_csv('pd.csv', float_format='%.2f')
# df.to_csv('pd.csv')
# np.sum