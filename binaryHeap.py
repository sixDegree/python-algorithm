import math

'''
堆 － 树形结构

应用：
    1. 优先队列：动态地选择优先级高的任务先执行, 入队／出队 => O(logN)
    
    2. N个选择前M个: 构建M个元素的最小堆 => O(N*logM)
    
    2. 多路归并排序（d叉堆）=> 当d=n时，退化为MergeSort


二叉堆：
    
    1. 完全二叉树（除最后一层可能只有左叶子，其他层都是有左右子节点）
    
    2. All Node Value: Parent>=Child => 最大堆
        or
       All Node Value: Parent<=Child => 最小堆
    
    3. 存储：可用数组存储二叉堆，从上到下，左到右，按层序存放
        parent          (i-1)/2
        left_child      2*i+1
        right_child     2*i+2
'''

class MaxHeap:

    def __init__(self,data=[]):
        self.data=data
        self.count=len(data)

    def __shiftUp(self,k):
        p=(k-1)//2
        while k>0 and self.data[p]<self.data[k]:
            self.data[p],self.data[k]=self.data[k],self.data[p]
            k=p
            p=(k-1)//2

    def __shiftDown(self,k):
        
        while k<self.count:
            l=2*k+1
            r=l+1
            max_index=k
            if l<self.count and self.data[l]>self.data[k]:
                max_index=l
            if r<self.count and self.data[r]>self.data[max_index]:
                max_index=r
            if max_index!=k:
                self.data[k],self.data[max_index]=self.data[max_index],self.data[k]
                k=max_index
            else:
                break

        # while 2*k+1<self.count:
        #     l=2*k+1
        #     r=l+1
        #     max_index=l
        #     if r<self.count and self.data[l]<self.data[r]
        #         max_index=r
        #     if self.data[k]<self.data[max_index]:
        #         self.data[k],self.data[max_index]=self.data[max_index],self.data[k]
        #         k=max_index
        #     else:
        #         break


    # 入队：自底向上
    def insert(self,item):
        self.data.append(item)
        self.__shiftUp(self.count)
        self.count+=1

    # 出队：自顶向下
    def extractMax(self):
        if self.count==0:
            return

        item=self.data[0]
        self.data[0],self.data[self.count-1]=self.data[self.count-1],self.data[0]
        self.count-=1
        self.__shiftDown(0)
        
        return item

    # 堆化：构建最大／最小堆
    def heapify(self):
        k=self.count-1
        p=(k-1)//2
        while p>=0:
            self.__shiftDown(p)
            p-=1

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
                    print(self.data[k],end=",")
            print("")
        print("---"*30)

'''
扩展：
'''
class BinaryHeap:

    def __init__(self,data=[],key=lambda x:x,maxHeap=True):
        self.data=data
        self.count=len(data)
        self.key=key
        self.maxHeap=maxHeap

    def __shiftUp(self,k):
        p=(k-1)//2
        while k>0 and self.__compare(self.data[k],self.data[p])==1:
            self.data[p],self.data[k]=self.data[k],self.data[p]
            k=p
            p=(k-1)//2

    def __shiftDown(self,k):
        
        while k<self.count:
            l=2*k+1
            r=l+1
            max_index=k
            if l<self.count and self.__compare(self.data[l],self.data[k])==1:
                max_index=l
            if r<self.count and self.__compare(self.data[r],self.data[max_index])==1:
                max_index=r
            if max_index!=k:
                self.data[k],self.data[max_index]=self.data[max_index],self.data[k]
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


    # 入队：自底向上
    def push(self,item):
        self.data.append(item)
        self.__shiftUp(self.count)
        self.count+=1

    # 出队：自顶向下
    def pop(self):
        if self.count==0:
            return

        item=self.data[0]
        self.data[0],self.data[self.count-1]=self.data[self.count-1],self.data[0]
        self.count-=1
        self.__shiftDown(0)

        del self.data[self.count]

        return item

    # 堆化：构建最大／最小堆
    def heapify(self):
        k=self.count-1
        p=(k-1)//2
        while p>=0:
            self.__shiftDown(p)
            p-=1

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
                    print(self.data[k],end=",")
            print("")
        print("---"*20)

if __name__ == '__main__':

    # a=[61,90,31,5,51,78,20,4,94,67]
    # heap=MaxHeap(a)
    # heap.printTree()

    # heap.heapify()
    # heap.printTree()

    # heap.insert(70)
    # heap.printTree()

    # result=heap.extractMax()
    # print(result)
    # heap.printTree()


    # heap2=MaxHeap()
    # heap2.insert(20)
    # heap2.insert(30)
    # heap2.insert(10)
    # heap2.insert(15)
    # heap2.insert(35)
    # heap2.insert(5)
    # heap2.printTree()

    print("***"*20)

    a=[61,90,31,5,51,78,20,4,94,67]
    heap=BinaryHeap(a,maxHeap=False)
    heap.printTree()

    heap.heapify()
    heap.printTree()

    for i in range(0,heap.count):
        print(heap.pop(),end=" ")
    print("")
    print(heap.data)

    heap.push(70)
    heap.push(30)
    heap.push(50)
    heap.push(80)
    heap.printTree()

    heap2=BinaryHeap(key=lambda x:x[1], maxHeap=False)
    heap2.push((20,0.35))
    heap2.push((30,0.89))
    heap2.push((10,0.55))
    heap2.push((15,0.23))
    heap2.push((35,0.78))
    heap2.push((5,0.94))
    heap2.printTree()








