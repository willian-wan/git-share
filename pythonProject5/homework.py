import numpy as np
import matplotlib.pyplot as plt
print("---------------homewokr1-3-----------------")
a = np.array([4,5,6])
b = np.array([(4,5,6),(1,2,3)])
print(a.dtype,a.shape,a[1],sep="\n")
print(b.shape,b[0,0],b[0,1],b[1,1],sep="\n")
print("---------------homewokr4-5-----------------")
a = np.zeros((3,3))
b = np.ones((4,5))
c = np.eye(4)
print(a,b,c,sep="\n")
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a,a[2,3],a[0,0],sep="\n")
print("---------------homewokr6-7-----------------")
b = np.array(a[0:1,2:])
c = np.array(a[1:,:])
print(b,b[0,0],c,c[0,-1],sep="\n")
print("---------------homewokr8-10-----------------")
a = np.array([[1,2],[3,4],[5,6]])
print(a[[0, 1, 2], [0, 1, 0]])
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])
a[np.arange(4), b]+=10
print(a)
print("---------------homewokr11-12-----------------")
x = np.array([1, 2])
print(x.dtype)
x = np.array([1.0, 2.0])
print(x.dtype)
print("---------------homewokr13-18-----------------")
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(x+y,np.add(x,y),sep="\n")
print(x-y,np.subtract(x,y),sep="\n")
print(x*y,np.multiply(x,y),np.dot(x,y),np.multiply(x,3),sep="\n")
print(np.divide(x,y))
print(np.sqrt(x))
print(x.dot(y))
print(np.dot(x,y))
print("---------------homewokr19-20-----------------")
print(np.sum(x))
print(np.sum(x,axis=0))
print(np.sum(x,axis=1))
print(np.mean(x))
print(np.mean(x,axis=0))
print(np.mean(x,axis=1))
print("---------------homewokr21-23-----------------")
print(x.T)
print(np.exp(x))
print(np.nanargmax(x,axis=0))
print(np.argmax(x,axis=1))
print("---------------homewokr24-25-----------------")
x=np.arange(0,100,0.1)
y=x*x
plt.subplot(212)
plt.plot(x,y)
x=np.arange(0,3*np.pi,0.1)
plt.subplot(211)
plt.plot(x,np.sin(x),label='sin(x)')
plt.plot(x,np.cos(x),label='cos(x)')
plt.legend()
plt.show()
