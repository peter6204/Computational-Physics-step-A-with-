import pylab as pl
#import numpy as np
#import scipy.linalg as np 

time = pl.linspace(0.0, 10.0, 10000)
height = pl.exp(-time / 3.0)* pl.sin(time*3)  #exp는 밑이 e라는 지수함수 
pl.figure()
#첫번째 핑크색 함수 이게 지금 damping 되고 있는 곳임 exp 로(마이너스 붙어서 감소함수임 ) 결과적으로 진폭 감소함 
pl.plot(time, height, 'm-')    #m은 마젠타로 보라색계열 

#두번째 초록색 함수  이건 그냥 단진동 함수 
pl.plot(time, 0.3*pl.sin(time*3), 'b-') 

pl.legend(['damped','constant amplitude'], loc='upper right') #주석을 달겠다. loc=location의 약자로 위치를 지정해준다. lower, upper right, left 조합으로 가능 
pl.xlabel('Time (s)')
pl.ylabel('height(m)')
pl.show()

