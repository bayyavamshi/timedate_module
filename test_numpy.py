import numpy as np
a=np.array([1,2,4,3,5,6])
b=np.zeros((5,6))
c=np.ones((3,4))
d=np.eye(10)
e=np.arange(1,20,2)
f=np.linspace(0,1,5)
# print(a.shape)
# print(a.ndim)
# print(a.dtype)
# print(a.itemsize)
# print(a.size)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# arr=np.array([10,20,30,40,50])
# print(arr[::-1])
# mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(mat[:,1:3])
arr=np.array([1,2,3,4,5,6])
# print(arr[[0,2,4]])
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print(a+b)
# print(b-a)
# print(a*b)
# a = np.array([[1], [2], [3]])   # shape (3,1) → column vector
# b = np.array([10, 20, 30])      # shape (3,)  → row vector
# print(a,b)
# print(a + b)
import numpy as np

# arr = np.array([[1, 2, 3],[0, 5, 6]])
# print(arr.sum())
# print(arr.mean())
# print(arr.min())
# print(arr.max())
# arr=np.array(12)

# print(arr.reshape(3,4))
# print(arr.flatten())

a = np.array([1,2,3])
b = np.array([4,5,6])


# print(np.hstack([a,b]))
# print("Vertical Stack:\n", np.vstack([a,b]))
# print("Horizontal Stack:", np.hstack([a,b]))
# print("Column Stack:\n", np.column_stack((a,b)))


# import numpy as np

# print(np.random.randn(3,3))  # 3x3 array of random numbers between 0 and 1
print(np.random.choice([1,2,34,5]))


np.random.seed(42)
print(np.random.rand(3))  # Will always print the same 3 numbers
# print(np.where([1,2,3,4]<2))  # (array([2, 3]),)
