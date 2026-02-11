import numpy as np
inputs=[1,2,3,4]
weights=[[1.2,3.4,5.6,7.8],
         [1.3,4.6,7.9,0.1],
         [2.4,5.9,2.0,-9.3]]
biases=0.2,3.4,6.5

output=np.dot(weights,inputs)+biases
print(output)