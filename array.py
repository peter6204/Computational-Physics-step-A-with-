import numpy as np

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
B = np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
C = np.array([2,4,6,8,10,12,14,16,18,20])


"""
print(A, A[2,3])
print(A * B) #array 곱은 각 요소를 곱한다.  
print(C[2])
print(C[1:3])
print(C[:4])

print(C[-2])  #끝에서 2번째 끝은 0번째 없다.

print(C[-3:])
"""
print(A[:,2]) #모든 행의 2열을 가져와라
print(B[1,:])  #1행의 모든 열 인쇄  이 두개가 핵심이다.


            #array 는 시작이 0부터임




