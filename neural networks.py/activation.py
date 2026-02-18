import numpy as np
class layer_dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights=0.01*np.random.randn(n_inputs,n_neurons)
        self.biases= np.zeros((1,n_neurons))
    def forward (self,inputs):
        self.output=np.dot(inputs,self.weights) + self.biases

class activation_ReLu:
   def forward (self,inputs):
     self.output=np.maximum(0,inputs)


layer1= layer_dense(3,4)
activation1=activation_ReLu()
layer2= layer_dense(4,2)
activation2=activation_ReLu()
X=[[1,2,3]]
layer1.forward(X)
activation1.forward(layer1.output)
layer2.forward(activation1.output)
activation2.forward(layer2.output)
print(activation2.output)
