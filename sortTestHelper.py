import random
import time

'''
生成n个元素的整型随机数组，每个元素取值范围：[rangeL,rangeR]
'''
def generateRandomArray(n,rangeL,rangeR,printArray=False):
    # random.random()          => random float: [0.0, 1.0)
    # random.uniform(a, b)     => random float: [a,b]

    # random.randint(a, b)     => random int: [a,b] = randrange(a, b+1)
    # random.randrange(start, stop[, step])

    a=[]
    for i in range(0,n):
        a.append(random.randint(rangeL,rangeR))
    if printArray:
        print(a)
    return a

def generateNearlyOrderedArray(n,swapTimes=0,printArray=False):
    a=[i for i in range(0,n)]
    for i in range(0,swapTimes):
        x=random.randint(0,n-1)
        y=random.randint(0,n-1)
        if x!=y:
            a[x],a[y]=a[y],a[x]

    if printArray:
        print(a)
    return a


def isSorted(a,n):
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            return False
    return True


def testSort(sortName,sortFunc,a,n,start=-1,printArray=False):
    startTime=time.time()
    if start>=0:
        sortFunc(a,start,start+n)
    else:
        sortFunc(a,n)
    endTime=time.time()
    result=isSorted(a,n)

    print("do : %s \tn : %g \tcost : %.3gs \tisSorted : %s" % (sortName,n,(endTime-startTime),result))
    if printArray:
        print(a)




