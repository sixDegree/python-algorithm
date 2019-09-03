import math

'''
二叉索引堆

+ data  : 用于查询 data[data_index]
+ id    : 用于构建堆，比较时，使用id[heap_index]=>data_index,定位到具体data比较
+ revId : 反向索引，用于查询数据在堆中的位置，revId[data_index]=>heap_index,定位到堆

'''

class BinaryIndexHeap:

    '''
    heap_index  =>   id[h_i]     =>  data_index
    heap_index  <=   revId[d_i]  <=  data_index

    id[h]=d
    revId[d]=h
    => revId[id[h]]=h

    eg:
        i     : 0 1 2 3 4 5
        id    : 0 3 4
        revId : 0 / / 1 2 /
    
    id[0]=0,    id[1]=3,    id[2]=4
    revId[0]=0, revId[3]=1, revId[4]=2

    i           0,      1,      2,      3,      4
    data        A,      B,      C,      D,      E
    =>
        push    A,      D,      E
        id      0,      3,      4
        rev     0:0,    3:1,    4:2
    '''
    
    def __init__(self,data=[],key=lambda x:x,maxHeap=True,heapify=False):
        self.data=data
        self.key=key
        self.maxHeap=maxHeap

        if not heapify:
            self.count=0
            self.id = []     # for heap_index => data_index mapping
            self.revId = {}  # for data_index => heap_index mapping
        else:
            self.count=len(self.data)
            self.id=[i for i in range(0,self.count)]
            self.revId={ i:i for i in range(0,self.count)}
            self.__heapify()


    def __shiftUp(self,k):

        p=(k-1)//2
        while k>0 and self.__compare(self.data[self.id[k]],self.data[self.id[p]])==1:
            # print("p=%d,k=%d,id[p]=%d,id[k]=%d,data[id[p]]=%d,data[id[k]]=%d" % (k,p,self.id[k],self.id[p],self.data[self.id[k]],self.data[self.id[p]]))
            self.id[p],self.id[k]=self.id[k],self.id[p]
            self.revId[self.id[p]]=p
            self.revId[self.id[k]]=k
            k=p
            p=(k-1)//2

    def __shiftDown(self,k):
        
        while k<self.count:
            l=2*k+1
            r=l+1
            max_index=k
            if l<self.count and self.__compare(self.data[self.id[l]],self.data[self.id[k]])==1:
                max_index=l
            if r<self.count and self.__compare(self.data[self.id[r]],self.data[self.id[max_index]])==1:
                max_index=r
            if max_index!=k:
                self.id[k],self.id[max_index]=self.id[max_index],self.id[k]
                self.revId[self.id[k]]=k
                self.revId[self.id[max_index]]=max_index
                k=max_index
            else:
                break

    def __compare(self,a,b):
        result=0
        if self.key(a)>self.key(b):
            result=1
        else:
            result=-1

        if self.maxHeap:
            return result
        else:
            return result*(-1)

    # 堆化：构建最大／最小堆
    def __heapify(self):
        k=self.count-1
        p=(k-1)//2
        while p>=0:
            self.__shiftDown(p)
            p-=1

    def contain(self,data_index):
        return self.revId.get(data_index) is not None

    def empty(self):
        return self.count==0

    # 入队：自底向上
    def push(self,val,data_index=None):
        if data_index is None:
            self.data.append(val)
            data_index=len(self.data)-1

        #print(self.revId,self.count,data_index,self.contain(data_index))
        assert(not self.contain(data_index))
        self.id.append(data_index)
        self.revId[self.id[self.count]]=self.count
        self.__shiftUp(self.count)
        self.count+=1


    # 出队：自顶向下
    def pop(self):
        # print("data :",self.data)
        # print("id :",self.id)

        if self.count==0:
            return

        item=(self.id[0],self.data[self.id[0]])

        self.id[0],self.id[self.count-1]=self.id[self.count-1],self.id[0]
        self.revId[self.id[0]]=0
        self.revId[self.id[self.count-1]]=self.count-1
        self.count-=1
        self.__shiftDown(0)

        del self.revId[self.id[self.count]]
        del self.id[self.count]
        
        return item

    def update(self,data_index,newVal):
        assert(self.contain(data_index))
        self.data[data_index]=newVal
        self.__shiftDown(self.revId[data_index])
        self.__shiftUp(self.revId[data_index])


    # print for check result
    def printTree(self):
        n=self.count
        d=int(math.log(n,2))+1
        print("n=%d,d=%d" % (n,d))

        for i in range(0,d):
            # print("\t"*(d-i),end="")
            for j in range(0,2**i):
                k=2**i+j-1
                if k<n:
                    # print(self.data[k],end="\t\t")
                    print("%d(%d:%s)" % (self.revId[self.id[k]]
                        ,self.id[k]
                        #,self.data[self.id[k]])
                        ,self.key(self.data[self.id[k]]))
                    ,end=", ")
            print("")
        print("---"*20)

    def printResult(self):
        print("index:",[ i for i in range(0,self.count)])
        print(" data:",self.data)
        print("   id:",self.id)
        print("revId:",self.revId)
        print("level: [",end="")
        for i in range(0,self.count):
            print(self.data[self.id[i]],end=", ")
        print("]")


if __name__ == '__main__':

    a=[61,90,31,5,51,78,20,4,94,67]

    print("1. initial:")
    heap=BinaryIndexHeap(a,maxHeap=True,heapify=True)
    heap.printResult()
    heap.printTree()
    
    print("2. push: item=70")
    heap.push(70)
    heap.printResult()
    heap.printTree()

    print("3. push: item=100")
    heap.push(100)
    heap.printResult()
    heap.printTree()

    print("4. push: exist item")
    a.append(45)
    a.append(77)
    n=len(a)
    heap.push(a[n-2],n-2)
    heap.printResult()
    heap.printTree()
    
    print("5. pop:")
    result=heap.pop()
    print("pop:",result)
    heap.printResult()
    heap.printTree()

    print("6. update:")
    index,newVal=1,97
    print("a[%d]=%d -> %d" % (index,a[index],newVal))
    heap.update(index,newVal)
    heap.printResult()
    heap.printTree()

    print("7. pop & push:")
    print("pop:---")
    for i in range(0,heap.count):
        print(heap.pop(),end="")
    print("")
    heap.printResult()

    print("push:---")
    heap.push(60)
    heap.push(30)
    heap.push(50)
    heap.push(80)
    heap.printResult()
    heap.printTree()

    print("***"*20)

    # a=[(61,"B"),(90,"C"),(31,"A"),(5,"E"),(51,"F"),(78,"D"),(20,"M"),(4,"N"),(94,"H"),(67,"J")]
    # print("1. initial:")
    # heap=BinaryIndexHeap(a,key=lambda x:x[1],maxHeap=False)
    # heap.printResult()
    # heap.printTree()
    
    # print("2. heapify:")
    # heap.heapify()
    # heap.printResult()
    # heap.printTree()
    
    # print("3. push: (70,'I')")
    # heap.push(item=(70,"I"))
    # heap.printResult()
    # heap.printTree()

    # print("4. push: (100,'G')")
    # heap.push(item=(100,"G"))
    # heap.printResult()
    # heap.printTree()
    
    # print("4. pop:")
    # result=heap.pop()
    # print("pop:",result)
    # heap.printResult()
    # heap.printTree()

    # print("5. update:")
    # index,newVal=1,(100,"K")
    # print("a[%d]=%s -> %s" % (index,a[index],newVal))
    # heap.update(index,newVal)
    # heap.printResult()
    # heap.printTree()


    








