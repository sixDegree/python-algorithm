'''
    => 遍历 Travel：图 => 树／森林
    
    1. DFS 深度优先遍历（递归）
    2. BFS 广度优先遍历（非递归）
    
    => 应用：
    
    1. 连接问题：连通
        
        - 判断：两个节点是否连通，是否形成环
        
        - 统计：区块内节点数量，统计区块数量
    
    2. 路径问题：寻路
        
        - 从节点A到节点B的路径
        
        - 完全连通的有权图
            
            + 最小生成树(Minimum Span Tree)
                
                * 找V-1条边连接V个节点，权值和最小，可能存在多个最小生成树（横切边中有权值相等的边）
                
                * Prim 算法: 每次找关联的weight最小的节点
                    O(ElogE), 借助优先队列（最小堆），每次从队列中弹出weight最小的节点，并放入其连接的节点
                    优化：其连接的节点，若路径上权值和小于它本身 维护V个节点关联的最小权值（不断更新与该节点关联的最小权值）=> O(ElogV)
        
                * Kruskal 算法: 每次找weight最小的边，且不形成环
                    O(ElogE)
            
            + 单源最短路径(Single Shortest Path Tree)
                
                * 从指定点A到其它所有点的最短路径
                
                * Dijkstra 算法: 
                    不能有负权边
                    借助优先队列 => O(ElogE)
                    借助最小索引堆 => O(ElogV)
                
                * BellmanFord 算法:
                    可以处理负权边，判别出负权环（有负权环则无最短路径）
                    O(EV)
                    判别出负权环:
                        + 原理：
                               最短路径最多经过所有`V`个顶点，`V-1`条边，
                               对所有点进行`V-1`次松弛操作，理论上就找到了从源点到其它所有点的最短路径，
                               如果还可以继续松弛，则说明图中存在负权环
                        + 实现：
                            通过对所有点多做一次松弛操作（即所有点经过2次松弛操作），
                            发现经过某个点的另外一条距离更短的路径，则表示存在负权环

            + 最小生成树 vs. 最短路径
                * 最小生成树：保证连接所有点的权值总和最小
                * 最短路径(单源）：保证所有点到起始点的距离最小（最短路径树，也是一棵生成树，但不是最小生成树）
                      => 从一点到其它各个点的最短路径（单源最短路径）


    最小生成树 -> 最短路径 子过程 ，动态规划

    '''

# n*n matrix, store edge weight
class DenseGraph:

    def __init__(self,n,directed=False):
        self.n=n
        self.directed=directed

        self.g=[ [ 0 for i in range(0,n)] for i in range(0,n)]
        self.m=0

    def addEdge(self,x,y,weight=1):
        if self.hasEdge(x,y):
            return False

        self.g[x][y]=weight
        if not self.directed:
            self.g[y][x]=weight
        self.m+=1
        return True

    def hasEdge(self,x,y):
        assert(x>=0 and x<self.n and y>=0 and y<self.n)
        return self.g[x][y]!=0

    def getWeight(self,x,y):
        assert(x>=0 and x<self.n and y>=0 and y<self.n)
        return self.g[x][y]

    def getOutNodes(self,x):
        assert(x>=0 and x<self.n)

        nodes=[]
        for i in range(0,self.n):
            if self.g[x][i]!=0:
                nodes.push(i)
        return nodes

    def getInNodes(self,x):
        assert(x>=0 and x<self.n)

        if not self.directed:
            return self.g[x]

        nodes=[]
        for i in range(0,self.n):
            if self.g[i][x]!=0:
                nodes.push(i)
        return nodes
    
    def nextNodeIter(self,x):
        assert(x>=0 and x<self.n)
        for i in range(0,self.n):
            if self.g[x][i]!=0:
                yield i

    def show(self):
        print("n * m = %d * %d" % (self.n,self.m))
        print("     ",end="")
        for i in range(0,self.n):
            print("%3s" % i,end=" ")
        print("")

        for i in range(0,self.n):
            #print(i,":",self.g[i])
            print(i,": ",end=" ")
            for j in range(0,self.n):
                if self.g[i][j]!=0:
                    print("%3s" % self.g[i][j],end=" ")
                else:
                    print("%3s" % ".",end=" ")
            print("")
            

# n dicts, store linked nodes
class SparseGraph:
    def __init__(self,n,directed=False):
        self.n=n
        self.directed=directed

        self.g=[ {} for i in range(0,n)]
        self.m=0

    def addEdge(self,x,y,weight):
        if self.hasEdge(x,y):
            return False

        self.g[x][y]=weight
        if not self.directed and x!=y:
            self.g[y][x]=weight

        self.m+=1
        return True

    def hasEdge(self,x,y):
        assert(x>=0 and x<self.n and y>=0 and y<self.n)
        return self.g[x].get(y) is not None

    def getOutNodes(self,x):
        assert(x>=0 and x<self.n)
        return self.g[x].keys()

    def getInNodes(self,x):
        assert(x>=0 and x<self.n)
        if not self.directed:
            return self.g[x]

        nodes=[]
        for i in range(0,self.n):
            if self.hasEdge(i,x):
                nodes.push(i)
        return nodes
    
    def getWeight(self,x,y):
        assert(x>=0 and x<self.n and y>=0 and y<self.n)
        assert(self.g[x].get(y) is not None)
        return self.g[x][y]

    def nextNodeIter(self,x):
        assert(x>=0 and x<self.n)
        return iter(self.g[x])

    def show(self):
        print("n * m = %d * %d" % (self.n,self.m))
        for i in range(0,self.n):
            print(i,":",self.g[i])

import random
import time
import heapq
import math

class GraphTestHelper:

    def generateRandomGraph(self,n,m,graph,weighted=False,isPrint=False): # n=node numbers; m=edge numbers
        i=0
        while i<m:
            x=random.randrange(0,n)
            y=random.randrange(0,n)
            if weighted:
                w=round(random.random()*100) # round(random.random(),2)
            else:
                w=1
            if x==y or not graph.addEdge(x,y,w):
                continue
            i+=1
        
        if isPrint:
            graph.show()

    

    # 遍历
    def travel(self,graph):
        visited=[False for i in range(0,graph.n)]
        roots=[i for i in range(0,graph.n)]
        parents=[-1 for i in range(0,graph.n)]
        set_size=[-1 for i in range(0,graph.n)]

        conn_grp_cnt=0
        for i in range(0,graph.n):
            if not visited[i]:
                cnt=self.dfs(graph,i,visited,roots,i,parents)
                # cnt=self.bfs(graph,i,visited,roots,parents)
                set_size[i]=cnt
                conn_grp_cnt+=1
        
        print("nodes     :",[i for i in range(0,graph.n)])
        print("visited   :",[i and 1 or 0 for i in visited])
        print("roots     :",roots)
        print("parents   :",parents)
        print("set_size  :",set_size)
        print("conn_grps :",conn_grp_cnt)
        print("---"*10)


    # 深度优先遍历（递归）
    def dfs(self,graph,x,visited,roots,r,parents):
        cnt=1
        visited[x]=True
        for i in graph.nextNodeIter(x):
            if not visited[i]:
                visited[i]=True
                roots[i]=r
                parents[i]=x
                cnt+=self.dfs(graph,i,visited,roots,r,parents)
        return cnt


    # 广度优先遍历（非递归）
    def bfs(self,graph,x,visited,roots,parents):
        queue=[x]
        cnt=0
        while queue:
            p=queue.pop(0)
            if visited[p]:
                continue
            visited[p]=True
            roots[p]=x
            cnt+=1
            for i in graph.nextNodeIter(p):
                if not visited[i]:
                    queue.append(i)
                    parents[i]=p
        return cnt

    '''
    最小生成树
    '''
    def prim(self,graph):
        visited=[False for i in range(0,graph.n)]
        edges=[]
        
        x=0
        pq=[(0,None,x)]    # (weight,from,to)
        while pq:
            weight,v,w=heapq.heappop(pq)
            if visited[w]:
                continue
            edges.append((v,w,weight))      # (from,to,weight)
            visited[w]=True
            for i in graph.nextNodeIter(w):
                if not visited[i]:
                    heapq.heappush(pq,(graph.getWeight(w,i),w,i))

        print("tree :",edges)

    def prim_opt(self,graph):
        from binaryIndexHeap import BinaryIndexHeap

        visited=[False for i in range(0,graph.n)]
        edges=[]
        
        x=0
        pq=[(x,0)]    # (to,weight)
        indexHeap=BinaryIndexHeap(pq,key=lambda x:x[1],maxHeap=False,heapify=True)

        while not indexHeap.empty():
            i,(w,weight)=indexHeap.pop()
            # print("pop: w=%d,weight=%d" % (w,weight))
            if visited[w]:
                continue
            edges.append((w,weight))
            visited[w]=True
            for i in graph.nextNodeIter(w):
                if not visited[i]:
                    item=(i,graph.getWeight(w,i))
                    if indexHeap.contain(i) and indexHeap.getData(i)[1]>item[1]:
                        # print("update: i=%d,weight=%d" % item)
                        indexHeap.update(i,item)
                    else:
                        # print("push: i=%d,weight=%d" % item)
                        indexHeap.push(item)
        
        print("tree :",edges)


    def kruskal(self,graph):
        from unionFind import UnionFind

        uf=UnionFind(graph.n)
        edges=[]
        pq=[]
        for v in range(0,graph.n):
            for w in graph.nextNodeIter(v):
                heapq.heappush(pq,(graph.getWeight(v,w),v,w))   # (weight,from,to)

        while pq and len(edges) < graph.n-1:
            weight,v,w=heapq.heappop(pq)
            if uf.isConnected(v,w):
                continue
            edges.append((v,w,weight))      # (from,to,weight)
            uf.union(v,w)

        print("tree :",edges)


    '''
    最短路径
    '''

    # O(ElogE)
    def dijkstra(self,graph,x):
        parent=[i for i in range(0,graph.n)]
        distance=[0 for i in range(0,graph.n)]
        visited=set()

        pq=[]
        heapq.heappush(pq,(0,x))

        while pq:
            node=heapq.heappop(pq)
            # print("pop:",node[0],chr(node[1]+65))
            dist=node[0]
            w=node[1]
            if w in visited:
                continue
            visited.add(w)
            for i in graph.nextNodeIter(w):
                if i not in visited:
                    distance[i]=dist+graph.getWeight(w,i)
                    heapq.heappush(pq,(distance[i],i))
                    parent[i]=w

        return parent,distance

    # 优化：贪心，减少入堆数 （ 进一步优化，需使用最小索引堆 => O(ElogV) )
    def dijkstra_opt(self,graph,x):
        parent=[i for i in range(0,graph.n)]
        distance=[i!=x and math.inf or 0 for i in range(0,graph.n)]
        visited=set()

        pq=[]
        heapq.heappush(pq,(0,x))

        while pq:
            node=heapq.heappop(pq)
            # print("pop:",node[0],chr(node[1]+65))
            dist=node[0]
            w=node[1]
            if w in visited:
                continue
            visited.add(w)
            for i in graph.nextNodeIter(w):
                if i not in visited and dist+graph.getWeight(w,i)<distance[i]:
                    distance[i]=dist+graph.getWeight(w,i)
                    heapq.heappush(pq,(distance[i],i))
                    parent[i]=w

        return parent,distance

    def printPath(self,parent,distance,hasNegativeCycle=False):
        print("parent :",parent)
        print("dist   :",distance)

        if not hasNegativeCycle:
            print("path   :",end=" ")
            x=len(distance)-1
            while x!=parent[x]:
                print("%d -> " % x,end="")
                x=parent[x]
            print(x)

    # V轮对E条边做松弛操作 ＝> O(VE)
    def bellmanFord(self,graph,s):
        dist=[math.inf for i in range(0,graph.n)]
        dist[s]=0

        edges=[None for i in range(0,graph.n)]
        edges[s]=(None,s,0)                # (from,to,weight)
        parent=[i for i in range(0,graph.n)]

        for i in range(1,graph.n):      # do n-1 times Relaxtion
            for j in range(0,graph.n):  # get n-1 edges  
                for w in graph.nextNodeIter(j):
                    if not edges[w] or dist[j]+graph.getWeight(j,w)<dist[w]:
                        dist[w]=dist[j]+graph.getWeight(j,w)
                        edges[w]=(j,w,graph.getWeight(j,w))
                        parent[w]=j

        print("edges :",edges)

        # do one more time Relaxtion to distinguish if has Negative cycle
        hasNegativeCycle=False
        for j in range(0,graph.n):
            for w in graph.nextNodeIter(j):
                #print("dist[%d]=%d,weight=%d,dist[%d]=%d" % (j,dist[j],graph.getWeight(j,w),w,dist[w]))
                if edges[w] and dist[j]+graph.getWeight(j,w)<dist[w]:
                    hasNegativeCycle=True
                    break
        print("hasNegativeCycle:",hasNegativeCycle)
        return parent,dist,hasNegativeCycle


if __name__ == '__main__':

    testHelper=GraphTestHelper()
    
    # n,m=5,4
    # graph=DenseGraph(n,directed=False)
    # testHelper.generateRandomGraph(n,m,graph,weighted=True,isPrint=True)
    # testHelper.travel(graph)

    # eg1
    # n=5
    # graph=DenseGraph(n,directed=False)
    # graph.addEdge(0,3,46)
    # graph.addEdge(3,2,62)
    # graph.addEdge(2,4,61)
    # graph.addEdge(3,4,90)
    # graph.show()

    # eg2
    # n=6
    # graph=SparseGraph(n,directed=False) # graph = DenseGraph(n,directed=False)
    # graph.addEdge(0,1,5)
    # graph.addEdge(0,2,1)
    # graph.addEdge(1,2,2)
    # graph.addEdge(1,3,1)
    # graph.addEdge(2,3,4)
    # graph.addEdge(2,4,8)
    # graph.addEdge(3,4,3)    #  graph.addEdge(3,4,6), graph.addEdge(3,4,10)
    # graph.addEdge(3,5,6)
    # graph.show()

    # testHelper.travel(graph)

    '''
    Sparse Graph Run Result:

    n * m = 6 * 8
    0 : {1: 5, 2: 1}
    1 : {0: 5, 2: 2, 3: 1}
    2 : {0: 1, 1: 2, 3: 4, 4: 8}
    3 : {1: 1, 2: 4, 4: 3, 5: 6}
    4 : {2: 8, 3: 3}
    5 : {3: 6}

    nodes     : [0, 1, 2, 3, 4, 5]
    visited   : [1, 1, 1, 1, 1, 1]
    roots     : [0, 0, 0, 0, 0, 0]
    parents   : [-1, 0, 1, 2, 3, 3]
    set_size  : [6, -1, -1, -1, -1, -1]
    conn_grps : 1

    -------------------------------------

    Dense Graph Run Result: 

    n * m = 6 * 8
           0   1   2   3   4   5
    0 :    .   5   1   .   .   .
    1 :    5   .   2   1   .   .
    2 :    1   2   .   4   8   .
    3 :    .   1   4   .   3   6
    4 :    .   .   8   3   .   .
    5 :    .   .   .   6   .   .
    nodes     : [0, 1, 2, 3, 4, 5]
    visited   : [1, 1, 1, 1, 1, 1]
    roots     : [0, 0, 0, 0, 0, 0]
    parents   : [-1, 0, 1, 2, 3, 3]
    set_size  : [6, -1, -1, -1, -1, -1]
    conn_grps : 1
    '''
    
    #===========================================

    # testHelper.prim(graph)
    # testHelper.prim_opt(graph)
    # testHelper.kruskal(graph)

    # parent,dist=testHelper.dijkstra(graph,0)
    # testHelper.printPath(parent,dist)

    # parent,dist=testHelper.dijkstra_opt(graph,0)
    # testHelper.printPath(parent,dist)
    
    # parent,dist=testHelper.bellmanFord(graph,0)
    # testHelper.printPath(parent,dist)

    print("---"*20)

    n=5
    graph=SparseGraph(n,directed=True)
    graph.addEdge(0,1,5)
    graph.addEdge(2,0,2)
    graph.addEdge(2,0,2)
    graph.addEdge(0,3,6)
    graph.addEdge(1,2,-4)
    graph.addEdge(1,4,2)
    graph.addEdge(2,4,5)
    graph.addEdge(2,3,3)
    graph.addEdge(4,3,-3)

    graph.show()
    testHelper.travel(graph)
    parent,dist,hasNegativeCycle=testHelper.bellmanFord(graph,0)
    testHelper.printPath(parent,dist,hasNegativeCycle)
   
    print("---"*20)

    graph=SparseGraph(n,directed=True)
    graph.addEdge(0,1,-5)   # graph.addEdge(0,1,5)
    graph.addEdge(0,2,2)    # graph.addEdge(2,0,2)
    graph.addEdge(2,0,2)
    graph.addEdge(0,3,6)
    graph.addEdge(1,2,-4)
    graph.addEdge(1,4,2)
    graph.addEdge(2,4,5)
    graph.addEdge(2,3,3)
    graph.addEdge(4,3,-3)

    graph.show()
    testHelper.travel(graph)
    parent,dist,hasNegativeCycle=testHelper.bellmanFord(graph,0)
    testHelper.printPath(parent,dist,hasNegativeCycle)
   




    


