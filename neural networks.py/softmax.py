import numpy as np
class layer_dense:
    def __init__(self,n_inputs, n_neurons):
        self.weights=np.random.randn(n_inputs,n_neurons)
        self.biases= np.zeros((1,n_neurons))
    def forward (self,inputs):
        self.output=np.dot(inputs,self.weights) + self.biases

class activation_ReLu:
   def forward (self,inputs):
     self.output=np.maximum(0,inputs)

class activation_softmax:
   def forward (self,inputs):
      exp_values = np.exp(inputs - np.max(inputs,axis=1,keepdims=True))
      probabilities = exp_values/np.sum(exp_values , axis=1,keepdims=True)
      self.output=probabilities
X = np.array([
    [1, 2],
    [2, 3],
    [3, 1],
    [4, 2]
])


layer1= layer_dense(2,4)
activation1=activation_ReLu()
layer2= layer_dense(4,3)
activation2=activation_softmax()
layer1.forward(X)
activation1.forward(layer1.output)
layer2.forward(activation1.output)
activation2.forward(layer2.output)
print(activation2.output[:5])
