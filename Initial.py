import numpy as np

def printTensorAttribs(x):
    result = "Dimensions: " + str(x.ndim) + " Shape: " + str(x.shape) + " DataType: " + str(x.dtype)
    print(result)
    
# 0D Tensor
x = np.array(12)
printTensorAttribs(x)

# 1D Tensor
y = np.array([1,2,3,4])
printTensorAttribs(y)

# 2D Tensor
z = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
printTensorAttribs(z)

# 3D Tensor
w = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
printTensorAttribs(w)

# 4D Tensor
v = np.array([[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]]],
[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]]],
[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]]]])
printTensorAttribs(v)