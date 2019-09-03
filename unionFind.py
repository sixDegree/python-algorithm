'''
并查集 Disjoint Set

应用：连接问题（Connectivity Problem)
    - 判断一个图，是否存在环（连通）
    - 判断网络中节点间的连接状态
    - 数学中集合类的实现

操作：O(h) h为树的高度
    - 查（根）  ：find_root(x)
    - 并（根）  ：union(x,y)
    - 判（集合）：isConnected(x,y)

优化：压缩查找路径 (Path Compression)
    - find_root
        + 压缩查找节点到根这条路径上的跳级节点，指向根（压缩一半）
        + 压缩查找节点到根这条路径上所有节点，都指向根（压缩到底，递归实现）
    - union
        + 基于size，选择数量多的一边的root作为根节点
        + 基于rank，选择层数小的一边的root作为根节点


Sample: find_root(4)

          0
         / 
        1
       /
      2
     /
    3
   /
  4   

=> demo1: find_root 压缩一半

      0 
     /   
    1     
   /    
  2     
 / \
3   4       


  0 
 / \
1   2    
   / \
  3   4       

=> demo2: find_root 压缩全部

     0
  / | | \
 1  2 3  4

'''


class UnionFind:

    def __init__(self,n):
        self.parent=[i for i in range(0,n)] # record each node' parent
        self.n=n

    '''
    find x's root 
    & 
    optimize: path compression (压缩查找节点到根这条路径上的跳级节点，指向根，可压缩一半)
    '''
    def find_root(self,x):
        assert(x>=0 and x<self.n)

        while self.parent[x]!=x:
            # optimize: path compression
            self.parent[x]=self.parent[self.parent[x]]
            # move to next
            x=self.parent[x]
        return x

    '''
    find x's root 
    & 
    optimize: path compression（递归实现，压缩查找节点到根这条路径上所有节点，指向根）
    '''
    def find_root2(self,x):
        assert(x>=0 and x<self.n)
        if x!=self.parent[x]:
            self.parent[x]=self.find_root2(self.parent[x])
        return self.parent[x]


    # if x's root == y's root
    def isConnected(self,x,y):
        return self.find_root(x)==self.find_root(y)

    # union x and y
    def union(self,x,y):                # find root：使用第一种路径压缩（压缩一半）
        x_root=self.find_root(x)
        y_root=self.find_root(y)
        
        if x_root==y_root:
            return False,x_root
        
        self.parent[x_root]=y_root
        return True,y_root

    def union2(self,x,y):
        x_root=self.find_root2(x)       # find root：使用第二种路径压缩（压缩到底）
        y_root=self.find_root2(y)
        
        if x_root==y_root:
            return False,x_root
        
        self.parent[x_root]=y_root
        return True,y_root

    def expand(self,size):
        self.parent+=[self.n+i for i in range(0,size)]
        self.n+=size



class UnionFindWithSize:

    def __init__(self,n):
        # record each node' parent
        self.parent = [i for i in range(0,n)] 
        self.n=n
        # record each node' nodes count
        self.size = [1 for i in range(0,n)]    

    '''
    find x's root & optimize: path compression
    '''
    def find_root(self,x):
        assert(x>=0 and x<self.n)

        while self.parent[x]!=x:
            # optimize: path compression
            self.parent[x]=self.parent[self.parent[x]]
            # move to next
            x=self.parent[x]
        return x

    # if x's root == y's root
    def isConnected(self,x,y):
        return self.find_root(x)==self.find_root(y)

    # union x and y
    def union(self,x,y):
        x_root=self.find_root(x)
        y_root=self.find_root(y)
        
        if x_root==y_root:
            return False,x_root
        
        rx_size=self.size[x_root]
        ry_size=self.size[y_root]

        # 选择元素个数多的作为根节点
        if rx_size<=ry_size:                # use y' root as root
            self.parent[x_root]=y_root
            self.size[y_root]+=rx_size
            return True,y_root
        else:                               # use x' root as root
            self.parent[y_root]=x_root
            self.size[x_root]+=ry_size
            return True,x_root

    def expand(self,size):
        self.parent+=[self.n+i for i in range(0,size)]
        self.n+=size
        self.size+=[1 for i in range(0,size)]

class UnionFindWithRank:

    def __init__(self,n):
        self.parent = [i for i in range(0,n)] # record each node' parent
        self.n=n
        # record each node' nodes count
        # rank[i] 表示以i为根的集合所表示的树的层数
        self.rank = [1 for i in range(0,n)]   

    '''
    find x's root & optimize: path compression
    注： 这里路径压缩，不会维护rank值，rank只是作为比较的标准，不是真正树的层数值
    '''
    def find_root(self,x):
        assert(x>=0 and x<self.n)

        while self.parent[x]!=x:
            # optimize: path compression
            self.parent[x]=self.parent[self.parent[x]]
            # move to next
            x=self.parent[x]
        return x

    # if x's root == y's root
    def isConnected(self,x,y):
        return self.find_root(x)==self.find_root(y)

    # union x and y
    def union(self,x,y):
        x_root=self.find_root(x)
        y_root=self.find_root(y)
        #print("x=%d,y=%d,x_root=%d,y_root=%d" % (x,y,x_root,y_root))
        
        if x_root==y_root:
            return False,x_root
        
        rx_rank=self.rank[x_root]
        ry_rank=self.rank[y_root]

        # 选择层数小的作为根节点
        if rx_rank==ry_rank:
            self.parent[x_root]=y_root
            self.rank[y_root]+=1
            return True,y_root
        elif rx_rank>ry_rank:               # use y' root as root
            self.parent[x_root]=y_root
            return True,y_root
        else:                               # use x' root as root
            self.parent[y_root]=x_root
            return True,x_root

    def expand(self,size):
        self.parent+=[self.n+i for i in range(0,size)]
        self.n+=size
        self.rank+=[1 for i in range(0,size)]


import random
import time
class UnionFindTestHelper:

    def __init__(self,n,m):                 # n=node numbers; m=edge numbers
        # generateRandomEdges
        edges=[]
        for i in range(0,m):
            x=random.randrange(0,n,2)       # 0,2,4,6,...
            y=random.randrange(1,n,2)      # 1,3,5,7,...
            edges.append([x,y])

        self.edges=edges
        self.n=n
        self.m=m
        #print(self.edges)

    def union(self,uf):
        for i in range(0,self.m):
            uf.union(self.edges[i][0],self.edges[i][1])

    def find_root(self,uf):
        # for i in range(0,self.m):
        #     uf.find_root(self.edges[i][0],self.edges[i][1])
        for i in range(1,self.n):
            uf.find_root(i)

    def isConnected(self,uf):
        for i in range(1,self.n):
            uf.isConnected(i,i-1)

    def getMaxDeepth(self,uf):
        parents=uf.parent
        maxDeepth=-1
        for i in range(0,n):
            p=i
            deepth=1
            while p!=parents[p]:
                p=parents[p]
                deepth+=1
            if maxDeepth<deepth:
                maxDeepth=deepth
        return maxDeepth

    def printPath(self,uf):
        parents=uf.parent
        visited=[False for i in range(0,n)]
        for i in range(0,n):
            if visited[i]:
                continue
            p=i
            while p!=parents[p]:
                print("%d -> " % p ,end="")
                visited[p]=True
                p=parents[p]
            visited[p]=True
            print(p)


    def doTest(self,uf,ufName,funcName,isPrint=False):
        testFunc=getattr(self,funcName)

        startTime=time.time()
        testFunc(uf)
        endTime=time.time()

        maxDeepth=self.getMaxDeepth(uf)

        print("%s (%d*%d) \tdo : %s \tcost : %.3gs \tmaxd : %d" % (ufName,self.n,self.m,funcName,(endTime-startTime),maxDeepth))
        
        if isPrint:
            print("edges  :",self.edges)
            print("nodes  :",[i for i in range(0,self.n)])
            print("parent :",uf.parent)
            self.printPath(uf)
        


if __name__=='__main__':

    '''
      0 - 1
         / \
        2   3
       / | /
      5   4
    '''
    # edges=[
    #     [0,1]
    #     ,[1,2],[1,3]
    #     ,[2,4],[2,5]
    #     #,[3,4]
    # ]

    # n,m=6,len(edges)

    # # UnionFind - union (use find_root)
    # uf=UnionFind(n)
    # for i in range(0,m):
    #     success,root=uf.union(edges[i][0],edges[i][1])
    #     if not success:
    #         break
    # print(success and "No cycle found." or "Cycle detected!")

    # newEdge=[3,4]
    # print("add edge:",newEdge)
    # uf.expand(1)
    # success,root=uf.union(newEdge[0],newEdge[1])
    # print(success and "No cycle found." or "Cycle detected!")
    # print("---"*10)

    # # UnionFind - union2 (use find_root2)
    # uf2=UnionFind(n)
    # for i in range(0,m):
    #     success,root=uf2.union2(edges[i][0],edges[i][1])
    #     if not success:
    #         break
    # print(success and "No cycle found." or "Cycle detected!")

    # newEdge=[3,4]
    # print("add edge:",newEdge)
    # uf2.expand(1)
    # success,root=uf2.union2(newEdge[0],newEdge[1])
    # print(success and "No cycle found." or "Cycle detected!")
    # print("---"*10)


    # # UnionFindWithSize
    # uf=UnionFindWithSize(n)
    # for i in range(0,m):
    #     success,root=uf.union(edges[i][0],edges[i][1])
    #     if not success:
    #         break
    # print(success and "No cycle found." or "Cycle detected!")

    # newEdge=[3,4]
    # print("add edge:",newEdge)
    # uf.expand(1)
    # success,root=uf.union(newEdge[0],newEdge[1])
    # print(success and "No cycle found." or "Cycle detected!")
    # print("---"*10)

    # # UnionFindWithRank
    # uf=UnionFindWithRank(n)
    # for i in range(0,m):
    #     success,root=uf.union(edges[i][0],edges[i][1])
    #     if not success:
    #         break
    # print(success and "No cycle found." or "Cycle detected!")

    # newEdge=[3,4]
    # print("add edge:",newEdge)
    # uf.expand(1)
    # success,root=uf.union(newEdge[0],newEdge[1])
    # print(success and "No cycle found." or "Cycle detected!")
    # print("---"*10)

    #########################

    n,m=10**5,9*(10**4)
    unionTester=UnionFindTestHelper(n,m)
    
    uf_list=[UnionFind(n),UnionFindWithSize(n),UnionFindWithRank(n)]

    for uf_inst in uf_list:
        inst_name=uf_inst.__class__.__name__
        unionTester.doTest(uf_inst,inst_name,"union",isPrint=False)
        for i in range(0,5):
            unionTester.doTest(uf_inst,inst_name,"find_root",isPrint=False)
        print("----"*10)

    