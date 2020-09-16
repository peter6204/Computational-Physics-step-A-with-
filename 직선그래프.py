from numpy import *   #"*"로 불러오면 np.linspace 뭐 이런거 안해도됨 
from pylab import *
x = linspace(0,10,51)  #linspace(a,b,c) a이상 b이하 c개의 등차수열 생성 라인의 공간 0이상 10 이하 51개로 쪼개기

#print(x)


y=x-10  #2x -3 이러면 컴퓨터가 인식을 못해요 
z=2*x-10



title('My first graph')  #그래프 이름 
xlabel('Time (fortnights)')  #x축 label
ylabel('Distance(furlongs)')  #y축 label
xlim(0,10)  #x축 범위
ylim(-10,5)  #y축 범위
plot(x,y,'b-')   
plot(x,z,'y-')   
# 점 : bo는 blue , ro=red, go=green 
# 선 : b-
show()
#다양한 함수 직선그래프 그래서 캡쳐해서 제출 