
'''参数部分'''
'''
m = 1 #到达航班对之间插入m架起飞航空器数
DROTi = [0.016,0.016]  #第i项表示第i种飞机起飞时间
AROTi = [0.01,0.01]  #第i项表示为第i种航空器降落的时间
pij = [[0.2, 0.8],[0.8,0.2]] #这里是一个矩阵，用来表示第j中飞机跟在第i种飞机后降落的概率
p =[0.2,0.8]      #表示机场每种飞机出现的概率
vi=[360,360]         #表示第i种飞机的进近速度
y1 = 1     #跑道清空时，最后进近的航空器距离跑道入口的距离
e = 1.5    #距离间隔裕度
x1 = [[10,20],[20,10]]    #两架相邻进场航空器最小距离间隔
tmin = 0.002

'''

'''计算函数部分'''
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


'''
CMAD=C_arrivals_departues23(y1=y1,e=e,p=p,AROTi=AROTi,DROTi=DROTi,vi=vi,m=m)
print(CMAD)
'''