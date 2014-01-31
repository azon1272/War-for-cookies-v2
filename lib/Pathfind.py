# -*- coding: cp1251 -*-
import lib, numpy#�������� ��������
def pathfind(matrix, x1,y1,x2,y2,steps):#matrix-����� ������������. ������� �� ����� � ������� ������ ����� �������� �������������!
    #������������ ������ - 0, ���������� - 1
    n=len(matrix)
    m=len(matrix[0])#������ � ������ �������
    for i in range (n):
        for j in range (m):
            wavematrix[i][j] = 0
    wavematrix[x1][y1] = -1
    xb[1]=x1
    yb[1]=y1
    k=0
    lenmas=1
    flag=false
    for z in range (30): #������������ ������ �����
        waveitems=0 #���-�� ������, ������� ������.
        nextx = []
        nexty = []
        for j in range(lenmas):
            for i in range (xb[j]-1,xb[j]+1): #1 ����, ������� �����
                if i<0 or i>n:
                    continue #�� ��� ��� ��� ��� ����� ����������
                temp=(z+1)*matrix[i][yb[j]]
                if wavematrix[i][yb[j]]>temp or wavematrix[i][yb[j]]==1:
                    wavematrix[i][yb[j]]=temp
                    waveitems++
                    nextx.append(i)
                    nexty.append(yb[j])
            for i in range (yb[j]-1,yb[j]+1): #1 ����, ������� �����
                if i<0 or i>m:
                    continue #�� ��� ��� ��� ��� ����� ����������
                temp=(z+1)*matrix[x1][y1]
                if wavematrix[x1][i]==1 or wavematrix[x1][i]>temp:
                    wavematrix[x1][i]=temp
                    waveitems++
                    nextx.append(x1)
                    nexty.append(y1)
            for i in range (waveitems):
                if nextx[i] == x2 and nexty[i] == x2:#���� ����� �� ������ �����
                    flag=true#���� �� �����
                    u=z#�������� ����� �����
        if flag:
            break
        lenmas=waveitems           
        xb=nextx
        yb=nexty
    if !flag:
        #��������� �� ������, ���� ������ ������� ����� ������
    trase = [][]
    retmove = [][]
    trase[0][0]=x2
    trase[0][1]=y2
    for i in range(1,u):
        if wavematrix[(trase[i-1][0])-1][trase[i-1][1]] == wavematrix[trase[i-1][0]][trase[i-1][1]]-1:
            trase[i][0] = trase[i-1][0]-1
            trase[i][1] = trase[i=1][0]
        elif wavematrix[(trase[i-1][0])+1][trase[i-1][1]] == wavematrix[trase[i-1][0]][trase[i-1][1]]-1:
            trase[i][0] = trase[i-1][0]+1
            trase[i][1] = trase[i=1][0]
        elif wavematrix[(trase[i-1][0])][trase[i-1][1]-1] == wavematrix[trase[i-1][0]][trase[i-1][1]]-1:
            trase[i][0] = trase[i-1][0]
            trase[i][1] = trase[i=1][0]-1
        elif wavematrix[(trase[i-1][0])][trase[i-1][1]+1] == wavematrix[trase[i-1][0]][trase[i-1][1]]-1:
            trase[i][0] = trase[i-1][0]
            trase[i][1] = trase[i=1][0]+1
        #���, �������� ������� ��������.
    for i in range (steps):
        retmove[i][0] = trase[u-i][0]#�������������� ������ �������, � �������� �� ���-�� �����
        retmove[i][1] = trase[u-i][1]
