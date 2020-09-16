import numpy as np  #"*"는 모든 이란 뜻
import pylab as pl
x = pl.linspace(0,10,51)  #linspace(a,b,c) a이상 b이하 c개의 등차수열 생성 라인의 공간 0이상 10 이하 51개로 쪼개기

#print(x)


y=2*x*x -x -1
z=x*x



pl.title('My Second graph')  #그래프 이름 
pl.xlabel('Time (fortnights)')  #x축 label
pl.ylabel('Distance(furlongs)')  #y축 label
pl.xlim(0,10)  #x축 범위 
pl.ylim(-10,200)  #u축 범위
pl.plot(x,y,'y-')   
pl.plot(x,z,'r-') 
# 점 : bo는 blue , ro=red, go=green 
# 선 : b-
pl.show()
#다양한 함수 직선그래프 그래서 캡쳐해서 제출 