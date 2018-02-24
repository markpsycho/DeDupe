# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 07:52:53 2018

@author: tomcr00se
"""

import pandas as pd
import numpy as np
import sys
num=1
def dist(seq1, seq2):  
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in xrange(size_x):
        matrix [x, 0] = x
    for y in xrange(size_y):
        matrix [0, y] = y

    for x in xrange(1, size_x):
        for y in xrange(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
#    print (matrix)
    return (matrix[size_x - 1, size_y - 1])

def concat(list1):
    result= ''
    for element in list1:
        result += element
    return result                    
    
def stringDist(x,y):
    #tokenize 
    X=x.split()
    Y=y.split()
    m=len(X)
    n=len(Y)
    b=[]
    dist1=0.0
    matchIndex=1
    #removing exact matches
    for i in xrange(0,m):
        for j in xrange(0,n):
            if X[i]== Y[j]:
                b+=[X[i]]
                
    for i in xrange(0,len(b)):
        X.remove(b[i])
        Y.remove(b[i])
        matchIndex+=1*(len(b[i]))
        
    #dist_abbriviate
    x=[]
    y=[]

    for i in xrange(0,len(X)):
        for j in xrange(0,len(Y)):
            if len(X[i])==1 or len(Y[j])==1 :
                if X[i][0]==Y[j][0]:
                    x+=[X[i]]
                    y+=[Y[j]]

    for i in xrange(0,len(x)):
        X.remove(x[i])
        Y.remove(y[i])
        matchIndex+=1*(max(len(x[i]),len(y[i])))

        #calculating distance rules out of 1
    xstr = concat(X)
    ystr = concat(Y)
    dist1 = float(dist(xstr,ystr))/matchIndex
    
    return dist1


def grid_update(grid2,x,y):
    grid1=grid2            
    for i in xrange(0,len(grid1)):
        for j in xrange(0,len(grid1)):
            if i==x :
                grid1[x][j]=min(grid1[x][j],grid1[y][j])
            elif j==x:
                grid1[i][x]=min(grid1[i][x],grid1[i][y])
            
            else:
                pass
    

    grid1=grid1[:y]+grid1[y+1:]    
    for i in xrange(0,len(grid1)):
        grid1[i]=grid1[i][:y]+grid1[i][y+1:]
    return grid1
        
def find(grid,threshold):
    mini = 100
    index= -1
    for i in xrange(0,len(grid)):
        for j in xrange(i+1,len(grid)):
            if grid[i][j] <= threshold and grid[i][j]<=mini:
                mini = grid[i][j]
                index=i*len(grid)+j    
    return index
            
def retClusters(X,threshold):
    Clusters=[]
    grid=X
    for i in range(0,len(X)):
        Clusters+=[[i]]
        
    index=find(X,threshold)
    if index==-1:
        return Clusters
    i = index/len(X)
    j = index%len(X)
    min_dist = X[i][j]
    while(min_dist<=threshold ):
        Clusters[i]=Clusters[i]+Clusters[j]
        Clusters = Clusters[:j]+Clusters[j+1:]
        grid=grid_update(grid,i,j)
        #print grid
        index=find(grid,threshold)
        if index==-1:
            return Clusters
        #print len(grid)
        i = index/len(grid)
        j = index%len(grid)
        min_dist = grid[i][j]
    return Clusters

def print_initial(X):
    for i in xrange(0,len(X)):
        print X[i][0],X[i][1],X[i][2],X[i][3]
def print_final(Clusters,X):
    global num
    print ">>>>>>>> with DOB: ",X[0][1]
    for j in xrange(0,len(Clusters)):
        print "Cluster: ",num
        #print "    index: "
        for i in Clusters[j]:
            print "      ",int(X[i][4]),X[i][0],X[i][1],X[i][2],X[i][3]
        num+=1
        print "\n"    
    print "----------------------------------------------"
def retUnique(X,threshold):
    
    #initial processing assuming uniqueness by M/F then dob
    M = []
    F = []
    for i in xrange(0,len(X)):
        #print X[i]
        if X[i][2] == "F":
            F+=[X[i]]
        else:            
            M+=[X[i]]
   
    Mdob = {}
    Fdob = {}
    
    for i in xrange(0,len(M)):
        try:
            Mdob[M[i][1]]+=[M[i]]
        except KeyError:
            Mdob[M[i][1]]=[M[i]]
    
    for i in xrange(0,len(F)):
        try:
            Fdob[F[i][1]]+=[F[i]]
        except KeyError:
            Fdob[F[i][1]]=[F[i]]
    
    #start clustering
    print "###### Females #####################################################"
    for key in Fdob:        
        grid=[]
        for i in xrange(0,len(Fdob[key])):
            gridrow=[]
            for j in xrange(0,len(Fdob[key])):
                gridrow+=[stringDist(Fdob[key][i][0],Fdob[key][j][0])+stringDist(Fdob[key][i][3],Fdob[key][j][3])]
            grid+=[gridrow]
        
        #print_initial(Fdob[key])
    
        print_final(retClusters(grid,1),Fdob[key])
            #h=0


    
    print "###### Males #######################################################"
    for key in Mdob:        
        grid=[]
        for i in xrange(0,len(Mdob[key])):
            gridrow=[]
            for j in xrange(0,len(Mdob[key])):
                gridrow+=[stringDist(Mdob[key][i][0],Mdob[key][j][0])+stringDist(Mdob[key][i][3],Mdob[key][j][3])]
            grid+=[gridrow]
        
        #print_initial(Mdob[key])
    
        print_final(retClusters(grid,1),Mdob[key])
            #h=0
         
    
        
try:
    df=pd.read_csv(sys.argv[1])
except:
    df=pd.read_csv("Deduplication-Problem-Sample-Dataset.csv")
    
trainingsetX = df.as_matrix()
trainingsetX=np.concatenate((trainingsetX,np.ones((len(trainingsetX),1))),axis=1)
for i in xrange(0,len(trainingsetX)):
    trainingsetX[i][4]+=i
retUnique(trainingsetX,1)