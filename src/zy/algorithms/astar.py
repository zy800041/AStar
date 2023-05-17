import operator
import numpy as np
import re
from src.zy.algorithms.datastructure import State


class AStar:
    def __init__(self):
        self.origin = None  # 初始状态，由用户输入
        self.dest = None  # 最终状态
        self.open = []  # open表
        self.close = []  # close表

        self.init()  # 初始化
        if self.getReverseNumber(self.origin)%2 == self.getReverseNumber(self.dest)%2:
            self.process()  # 处理八数码
        else:
            print('输入的初始数据无解。')

    # 初始化，接收初始矩阵输入
    def init(self):
        while True:
            o = input("请输入矩阵初始状态，以0代表空（以空格分隔）:")
            olist = re.split(r'\s+', o)  # 以空符号分隔
            # 防止末尾有空格
            for i in olist:
                if len(i) == 0:
                    olist.remove(i)
            # 终态
            correct = ['1', '2', '3', '8', '0', '4', '7', '6', '5']
            # 检查输入
            if (sorted(olist) == sorted(correct)):
                break
            else:
                print("输入有误！")

        origin_ = np.zeros((3, 3), dtype=int)
        dest_ = np.zeros((3, 3), dtype=int)
        for i in range(3):
            for j in range(3):
                origin_[i][j] = int(olist[i * 3 + j])
                dest_[i][j] = int(correct[i * 3 + j])
        self.origin = origin_
        self.dest = dest_

    #获得逆序数
    def getReverseNumber(self,state):
        res = 0
        s = ''
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != 0:
                    s += str(state[i][j])
        for i in range(len(s)):
            for j in range(i):
                if s[j]>s[i]:
                    res += 1
        return res

    # 处理
    def process(self):
        self.open.append(State(self.origin,self.dest))  # 将初态插入open表
        # 当open表不为空
        while self.open:
            now = self.open.pop(0)
            self.close.append(now)
            # 当该状态为终态
            if (now.state == self.dest).all():
                print('\n答案：\n')
                self.printResult(now)
                return
            #若非终态
            row, col = now.findPos(now.state,0)
            for [i,j] in [[row+1,col],[row-1,col],[row,col+1],[row,col-1]]:
                #如果没有越界
                if 0<=i<3 and 0<=j<3:
                    newState = now.move(i,j)
                    #判断新状态是否在close表
                    if self.checkInList(self.close,newState) == -1:
                        index = self.checkInList(self.open,newState)
                        #如果不在close表中，判断是否在open表中
                        if index == -1:
                            #如果不在open表中
                            self.open.append(State(newState,self.dest,now))
                        else:
                            #如果存在于open表中
                            if now.d+1 < self.open[index].d:
                                self.open.pop(index)
                                self.open.append(State(newState,self.dest,now))
            self.open.sort(key=self.cmp)

    #检查状态是否在list中
    def checkInList(self,alist,state):
        for i in range(len(alist)):
            if (alist[i].state == state).all():
                return i
        return -1

    #打印结果
    def printResult(self,node):
        tmplist = []
        tmpnode = node
        while tmpnode:
            tmplist.append(tmpnode)
            tmpnode = tmpnode.former
        tmplist.reverse()
        for i in tmplist:
            print(i)

    #排序方式
    def cmp(self,node):
        return node.f

if __name__ == '__main__':
    astar = AStar()