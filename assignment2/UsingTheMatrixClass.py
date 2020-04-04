import numpy as np
from matrix import matrix

#This code shows how to effectively use the matrix class

#Creating a 2 by 4 matrix with elements initialized to 0
m1 = matrix(np.zeros((2,4)))
print(m1)

#Creating a 2 by 4 matrix with elements initialized to 1
m2 = matrix(np.ones((2,4)))
print(m2)

#Creating a 4 by 4 matrix initialized to identity
m3 = matrix(np.identity(4))
print(m3)

#Multiplying 2 matrices of compatible size
m4 = m2 * m3
print(m3)

#Obtaining the number of rows and columns for a matrix
print(m3.getNumberOfRows())
print(m3.getNumberOfColumns())

#Testing for equality between matrices
m1 = matrix(np.identity(3))
m2 = matrix(np.identity(4))

if m1 == m2:
    print("Matrices are equal")
else:
    print("Matrices are different")

m1 = matrix(np.identity(4))

if m1 == m2:
    print("Matrices are equal")
else:
    print("Matrices are different")

#Computing the dot product of two row vectors as a matrix multiplication
m1 = matrix(np.zeros((1,3)))
#Using the set method to initialize vectors
m1.set(0,0,1.0)
m1.set(0,1,0.0)

m2 = matrix(np.zeros((1,3)))
m2.set(0,0,0.0)
m2.set(0,1,1.0)

m3 = m1 * m2.transpose()
print(m3)

#Computing the cross product of two vectors
m3 = m1.crossProduct(m2)
print(m3)

#Computing the inverse of a matrix
m1 = matrix(np.identity(4))
m2 = m1.inverse()
print(m2)

#Computing the l2 norm

m1 = matrix(np.zeros((1,3)))
m1.set(0,0,1.0)
m1.set(0,1,1.0)
m1.set(0,2,1.0)
print(m1.norm())

#Multiplying a matrix with a scalar
m1 = matrix(np.ones((3,3)))
m2 = m1.scalarMultiply(4.0)
print(m2)

#Normalizing a row vector
m1 = matrix(np.zeros((1,3)))
m1 = m1.initialize(5.0)
m1 = m1.normalize()
print(m1)
print(m1.norm())

#Computing the determinant of a matrix
m1 = matrix(np.identity(4))
print(m1)
print(m1.determinant())

#Adding and deleting matrix rows and columns
m1 = matrix(np.zeros((4,4)))
m1.set(0,0,1.0)
m1.set(1,0,2.0)
m1.set(2,0,3.0)
m1.set(3,0,4.0)
print(m1)
m1 = m1.removeColumn(1)
m1 = m1.removeRow(0)
print(m1)
m1 = m1.insertColumn(1,0.0)
print(m1)
m1 = m1.insertRow(0,0.5)
m1 = m1.insertRow(3,9.0)
print(m1)

#Duplicating a matrix
m1 = matrix(np.identity(4))
m2 = m1.copyMatrix()
print(m1 + m2)

#Performing simple matrix arithmetics
m2.set(3,3,3.0)
print(m1)
print(m2)

m2.set(1,1,10.0)
print(m2)
m2 = -m2
print(m2)
m2 += m2
print(m2)