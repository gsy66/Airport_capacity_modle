import random
import numpy as np
from math import sqrt
class WX:
    '''卫星等的结构体，用来表示卫星三维坐标位置和检测到的距离'''
    def __init__(self) -> None:
        self.x=''
        self.y=''
        self.z=''
        self.distence=''

dist=random.randint(0,100)
x0=random.randint(0,100)
y0=random.randint(0,100)
z0=random.randint(0,100)#随机生成一个初始坐标，及我们要求的准确坐标
xyz0=[x0,y0,z0]
def Wx_init(x,y,z):
    #输入参数为卫星初始坐标
    w=WX()
    w.x=x
    w.y=y
    w.z=z
    w.distence=sqrt((x-x0)**2+(y-y0)**2+(z-z0)**2)
    print("该卫星坐标为（{0} ,{1} ,{2}),距对应点{3}的距离：{4}".format(w.x,w.y,w.z,xyz0,w.distence))
    return w
def WX_error(w=WX()):
    temp1=random.random()*(0.5) #可人为设定误差量级
    if(random.random()>0.5):    #随机正负误差值
        temp2=1
    else:
        temp2=-1
    print(temp1)
    print(temp2)
    w.distence=w.distence+temp2*temp1

def Solve():
    jsz=[54,96,66]
    xyz=[[5,5,5],[5,5,5],[5,5,5],[5,5,5]]
    Di=[120,120,120,120]
    v=np.zeros((4,1))
    A=np.zeros((4,3))
    L=np.zeros((4,1))
    D0i=np.zeros((4,1))
  #  for i in range(0,len(Di)-1):
    print(A[0,1])



w1=Wx_init(0,5,100)
w2=Wx_init(100,88,0)
w3=Wx_init(50,5,58)
w4=Wx_init(0,99,36)
#WX_error(w1)
print('[{} {} {};{} {} {};{} {} {};{} {} {}]'.format(w1.x,w1.y,w1.z,w2.x,w2.y,w2.z,w3.x,w3.y,w3.z,w4.x,w4.y,w4.z))
print("[{} {} {} {}]\n".format(w1.distence,w2.distence,w3.distence,w4.distence))