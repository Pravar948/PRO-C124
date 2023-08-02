import numpy as np

A = np.array([1, 2, 3, 4, 5])
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix shape:", A.shape)
diag = np.diag(A)
print("Diagonal elements:", diag)

rows, columns = A.shape
print("Number of rows:", rows)
print("Number of columns:", columns)

n=rows*cols
C=np.zeros([rows,cols])

for i in range(rows):
  for j in range(cols):
    count+=1
print('Element ',count)