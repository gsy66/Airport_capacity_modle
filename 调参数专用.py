
import numpy as np
import matplotlib.pyplot as plt
'''参数部分
这里定义了一些全局变量
'''
y1 = 0.3   #0.3     #跑道清空时，最后进近的航空器距离跑道入口的距离
e = 1.5  #0.01    #距离间隔裕度
m = 1      #到达航班对之间插入m架起飞航空器数
Fij = [[0.03,0.05,0.06],[0.03,0.05,0.06],[0.03,0.05,0.06]]  #前机i后机j在连续起飞时的最小时间间隔
wij=[[0,0,0],[10,0,0],[12,10,8]] #同上，这里表示的事故前后ij的雷达尾流安全间隔规定
vi=[251,263,278]    #表示第i种飞机的进近速度
DROTi = [0.05,0.05,0.08]  #第i项表示第i种飞机起飞时间
AROTi = [0.01,0.01,0.02]  #第i项表示为第i种航空器降落的时间
x1 = [[0,0,0],[10,0,0],[12,10,8]]    #两架相邻进场航空器最小距离间隔
tmin = 0.002# 起飞到达航空器的间隔规定，该间隔规定为即将到达的航空器与将要放飞的航空器提供足够的间隔，以保证空中间隔不会违反空管间隔规定

"""下面是不同模型的不同计算结果"""
'''
def main():

    CAA=con_arrival_modle(y1=y1,e=e,vi=vi,p=p,pij=pij,wij=wij,AROT=AROTi)
    print("连续到达容量模型：{}".format(CAA))
    CDD=con_takeoff_modle(Fij=Fij,DROTi=DROTi,pij=pij,p=p)
    print("连续到达容量模型：{}".format(CDD))
    CMAD0 = C_arrivals_departues(y1=y1,x1=x1,e=e,p=p,AROTi=AROTi,DROTi=DROTi,vi=vi,pij=pij,tmin=tmin,m=0)
    print("到达起飞容量模型14：{}".format(CMAD0))
    CMAD = C_arrivals_departues(y1=y1,x1=x1,e=e,p=p,AROTi=AROTi,DROTi=DROTi,vi=vi,pij=pij,tmin=tmin,m=m)
    print("到达起飞容量模型23：{}".format(CMAD))
'''

def con_arrival_modle(y1,e,vi,p,pij,wij,AROT):
    PiVi = 0
    PiPjWij =0
    AAST=[]
    for i in range(0,len(pij)):
        PiVi=PiVi+p[i]*vi[i]
        temp=[]
        for j in range(0,len(pij)):
            PiPjWij=p[i]*p[j]*wij[i][j]+PiPjWij
            aastij =(PiPjWij+e)/PiVi
            temp.append(aastij)
        AAST.append(temp)
    Tij =[]
    for i in range(0,len(AAST)):
        ATi= (y1+e)/vi[i]+AROT[i]
        temp = []
        for j in range(0,len(AAST[0])):
            if ATi>AAST[i][j]:
                t = ATi
            else:
                t = AAST[i][j]
            temp.append(t)
        Tij.append(temp)
    ETAA=0
    for i in range(0,len(Tij)):
        for j in range(0,len(Tij)):
            ETAA=ETAA+pij[i][j]*Tij[i][j]
    return 1/ETAA



def C_arrivals_departues23(y1,e,p,AROTi,DROTi,vi,m):
    temp1 = 0    #计算式分子
    temp2 = 0    #计算式分母
    for i in range(0,len(p)):
        temp1 = temp1 +p[i]*vi[i]*(AROTi[i]+m*DROTi[i])
        temp2 = temp2 +p[i]*vi[i]
    temp1 = temp1 + y1+e
    temp2 = temp2*(1+m)
    return temp2/temp1

def C_arrivals_departues14(vi,pij,AROTi,DROTi,y1,x1,tmin):
    ETB=0
    nij=[]
    NPIJ =0
    for i in range(0,len(pij)):
        T=[]
        for j in range(0,len(pij[0])):
            if vi[i] > vi[j]:
                temp = AROTi[i]+y1/((1/vi[j])-(1/vi[i]))+x1[i][j]/vi[j]
            else:
                temp = x1[i][j]/vi[j]+AROTi[j]
            if temp- tmin>0:
                nij_t = int((temp-tmin)/DROTi[0]+1)
            else:
                nij_t=0
            ETB = ETB+ pij[i][j]*temp
            NPIJ = NPIJ+pij[i][j]*nij_t
            T.append(nij_t)
        nij.append(T)     
    Carr= 1/ETB
    TG = int(Carr-1)
    Cdep = TG*NPIJ
    return [Carr,Cdep]


def C_arrivals_departues(y1,x1,e,p,AROTi,DROTi,vi,m,pij,tmin):
    if m != 0:
        CMAD=C_arrivals_departues23(y1=y1,e=e,p=p,AROTi=AROTi,DROTi=DROTi,vi=vi,m=m)
    else:
        a=C_arrivals_departues14(vi=vi,pij=pij,AROTi=AROTi,DROTi=DROTi,y1=y1,x1=x1,tmin=tmin)
        CMAD = a[0]+a[1]
    return CMAD


def con_takeoff_modle(Fij,DROTi,pij,p):

    DT = DROTi.copy()
    DDSTij=[]
    for i in range(0,len(Fij)):
        temp=[]
        for j in range(0,len(Fij[0])):
            t = p[i]*p[j]*Fij[i][j]
            temp.append(t)
        DDSTij.append(temp)

    #下面计算TT的i*j型矩阵
    Tij2=[]
    for i in range(0,len(DDSTij)):
        temp=[]
        for j in range(0,len(DDSTij[0])):
            if DT[i]>DDSTij[i][j]:
                t = DT[i] 
            else:
                t = DDSTij[i][j]
            temp.append(t)
        Tij2.append(temp)

    ETDD=0
    for i in range(0,len(pij)):
        for j in range(0,len(pij)):
            ETDD=ETDD+pij[i][j]*Tij2[i][j]
    return 1/ETDD

def draw_picture():
    listy=[]
    listx=[]
    for i in np.arange(0.02,1,0.02):
        listx.append(i)
        a = (1-i)*51/98
        b = (1-i)*47/98
        pij = [[i*i,a*i,b*i],[i*a,a*a,b*a],[i*b,a*b,b*b]]
        p = [i,a,b]
        #CAA=con_arrival_modle(y1=y1,e=e,vi=vi,p=p,pij=pij,wij=wij,AROT=AROTi)
        #print("连续到达容量模型：{}".format(CAA))
        #CDD=con_takeoff_modle(Fij=Fij,DROTi=DROTi,pij=pij,p=p)
        #print("连续到达容量模型：{}".format(CDD))
    
    for c in np.arange(0.02,1,0.02):
        a = (1-c)*2/53
        b = (1-c)*51/53
        pij = [[a*a,a*b,a*c],[a*b,b*b,b*c],[a*c,b*c,c*c]]
        p = [a,b,c]
        CAA=con_arrival_modle(y1=y1,e=e,vi=vi,p=p,pij=pij,wij=wij,AROT=AROTi)
        listy.append(CAA)
    plt.plot(listx,listy)
    plt.show()
draw_picture()