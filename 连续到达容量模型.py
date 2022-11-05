'''
#参数部分
y1 = 1
e = 1.5
#关于机场的一些参数
pij = [[0.2, 0.8],[0.8,0.2]] #这里是一个矩阵，用来表示第j中飞机跟在第i种飞机后降落的概率
wij=[[1,2],[2,1]] #同上，这里表示的事故前后ij的雷达尾流安全间隔规定
vi=[1,2]#表示第i种飞机的进近速度
AROT=[1,2]
p =[0.2,0.8]
'''
#下面是公式计算
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
'''CAA=con_arrival_modle(y1=y1,e=e,vi=vi,p=p,pij=pij,wij=wij,AROT=AROT)
print(CAA)'''