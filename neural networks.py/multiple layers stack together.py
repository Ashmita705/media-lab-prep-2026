import numpy as np
class layer_dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights=0.01*np.random.randn(n_inputs,n_neurons)
        self.biases= np.zeros((1,n_neurons))
    def forward (self,inputs):
        self.output=np.dot(inputs,self.weights) + self.biases


layer1= layer_dense(3,4)
layer2= layer_dense(4,2)
X=[[1,2,3]]
layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)