inputs=[1,2,3,4]
weights1=[2.3,1.4,-0.6,3.5]
weights2= [3.4,-0,8,1.9,2.7]
weights3=[2.8,4.7,5.9,-0,2]

bias1=2
bias2=3
bias3=5

output= [inputs[0]*weights1[0]+inputs[1]*weights1[1]+inputs[2]*weights1[2]+inputs[3]*weights1[3]+bias1,
        inputs[0]*weights2[0]+inputs[1]*weights2[1]+inputs[2]*weights2[2]+inputs[3]*weights2[3]+bias1,
        inputs[0]*weights3[0]+inputs[1]*weights3[1]+inputs[2]*weights3[2]+inputs[3]*weights3[3]+bias1]
print(output)
       
    