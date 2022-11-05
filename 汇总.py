
from 到达起飞容量模型 import C_arrivals_departues
from 连续到达容量模型 import con_arrival_modle
from 连续起飞容量模型 import con_takeoff_modle

'''参数部分
这里定义了一些全局变量
'''
y1 = 0.3   #0.3     #跑道清空时，最后进近的航空器距离跑道入口的距离
e = 1.5  #0.01    #距离间隔裕度
m = 1      #到达航班对之间插入m架起飞航空器数
Fij = [[0.03,0.05,0.06],[0.03,0.05,0.06],[0.03,0.05,0.06]]  #前机i后机j在连续起飞时的最小时间间隔
wij=[[11.1,13,14,8],[11.1,13,14.8],[11.1,13,14.8]] #同上，这里表示的事故前后ij的雷达尾流安全间隔规定
vi=[251,263,278]    #表示第i种飞机的进近速度
DROTi = [0.05,0.05,0.08]  #第i项表示第i种飞机起飞时间
AROTi = [0.01,0.01,0.02]  #第i项表示为第i种航空器降落的时间
x1 = [[14.8,13,11.1],[14.8,13,11.1],[14,13,11.1]]    #两架相邻进场航空器最小距离间隔
tmin = 0.002# 起飞到达航空器的间隔规定，该间隔规定为即将到达的航空器与将要放飞的航空器提供足够的间隔，以保证空中间隔不会违反空管间隔规定

"""下面是不同模型的不同计算结果"""
CAA=con_arrival_modle(y1=y1,e=e,vi=vi,p=p,pij=pij,wij=wij,AROT=AROTi)
print("连续到达容量模型：{}".format(CAA))
CDD=con_takeoff_modle(Fij=Fij,DROTi=DROTi,pij=pij,p=p)
print("连续到达容量模型：{}".format(CDD))
CMAD0 = C_arrivals_departues(y1=y1,x1=x1,e=e,p=p,AROTi=AROTi,DROTi=DROTi,vi=vi,pij=pij,tmin=tmin,m=0)
print("到达起飞容量模型14：{}".format(CMAD0))
CMAD = C_arrivals_departues(y1=y1,x1=x1,e=e,p=p,AROTi=AROTi,DROTi=DROTi,vi=vi,pij=pij,tmin=tmin,m=m)
print("到达起飞容量模型23：{}".format(CMAD))