import numpy as np

A = np.array([[1,2,3],[2,1,-4],[3,-1,2]])
B = np.array([13, -7, 11])
print(A)
print(B)

C = np.linalg.solve(A,B)  
#행렬 A에 무엇을 곱할 때 B가 나오는가를 구하는 방법임 선형대수의 해
print(C)

