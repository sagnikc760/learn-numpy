import numpy as np

a = np.array([1,2,3])
print(a)

b = np.array([[0.9,123.33,123.33],[12313.33,122.33,0.3]])
print(b)

print(a.ndim * b.ndim)

## get type
print(b.dtype)

## get sie 
print(a.itemsize)

## total size
print(a.size)

## typecasting data type 

c = np.array([1,2,3],dtype='float32')
print(c.dtype)

## access/change specific elemetns,rows ,columns 

a = np.array([[1,2,34,5],[123,3123213,331,33]])
print(a)
# get the specific elemnt [r,c]
print(a[1,3])

#get a specific row 
print(a[0,:])

# get a specific column
print(a[:,2])

## more fancy access
print(a[0,1:3:-2])

# change leemnt 
a[1,2] = 123
print(a)
a[:,2] = [1,2]
print(a)


