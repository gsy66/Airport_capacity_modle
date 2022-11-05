
'''参数部分'''

'''
Fij = [[1,2],[2,1]]  #前机i后机j在连续起飞时的最小时间间隔
DROTi = [1,2]  #第i项表示第i+1种飞机起飞时间
pij = [[0.2, 0.8],[0.8,0.2]] #这里是一个矩阵，用来表示第j中飞机跟在第i种飞机后降落的概率
p =[0.2,0.8]
'''
'''建模计算部分''' 

#计算DDST的i*j矩阵
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
'''
CDD=con_takeoff_modle(Fij=Fij,DROTi=DROTi,pij=pij,p=p)
print(CDD)
'''
