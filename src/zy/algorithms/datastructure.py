class State:
    def __init__(self,state,dest,former = None):
        self.state = state  #矩阵状态，3*3矩阵
        self.f = 0  #启发函数，f(n)=d(n)+w(n)
        self.d = 0  #d为深度
        self.w = 0  #w为不在位状态数量
        self.former = None  #上一个状态
        if former != None:
            self.former = former
            self.d = former.d+1
        #计算有多少和终态不一样
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] != dest[i][j]:
                    self.w = self.w+1
        self.f = self.d+self.w

    def findPos(self,target,num):
        for i in range(len(target)):
            for j in range(len(target[i])):
                if target[i][j] == num:
                    return i, j

    def move(self,x,y):
        x0, y0 = self.findPos(self.state,0)
        newState = (self.state).copy()
        tmp = newState[x0][y0]
        newState[x0][y0] = newState[x][y]
        newState[x][y] = tmp
        return newState

    def __str__(self):
        s = '估价函数F:'+str(self.f)+'\n实际步数D:'+str(self.d)+'\n启发信息W:'+str(self.w)+'\n状态矩阵:\n'
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                s = s+str(self.state[i][j])+' '
            s = s+'\n'
        return s