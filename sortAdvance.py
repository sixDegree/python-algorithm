import sortTestHelper
import sortBasic
import random

'''
高级排序

平均时间复杂度：O(N*logN)

1. 归并排序 Merge Sort
2. 快速排序 Quick Sort
3. 堆排序 Heap Sort

O(N*logN) 比 O(N^2) 快多少：

|  N   |  N^2  | N*logN  | 差倍数 |
|:-----|:------|:--------|:------|
| 10   | 10^2  | 33      | 3     |
| 10^2 | 10^4  | 664     | 15    |
| 10^3 | 10^6  | 9966    | 100   |
| 10^4 | 10^8  | 132877  | 753   |
| 10^5 | 10^10 | 1660964 | 6020  |

算法比较：

|   Sort         | 平均时间复杂度 | 原地 | 额外空间复杂度 | 稳定 |
|:---------------|:------------|:-----|:------------|:----|
| Insertion Sort | O(N^2)      | Y    | O(1)        | Y   |
| Merge Sort     | O(N*logN)   | N    | O(N+logN)   | Y   |
| Quick Sort     | O(N*logN)   | Y    | O(logN)     | N   |
| Heap Sort      | O(N*logN)   | Y    | O(1)        | N   |

'''

def merge_sort(a,n):
    '''
    归并排序 －－ 递归实现
    
    时间复杂度：O(N*logN)
    
    额外空间辅助：O(N)
    '''

    if n<=1:
        return a
    
    # 1. seperate
    mid=n//2
    # print("p_left=",a[:mid],", p_right=",a[mid:])
    a_left=merge_sort(a[:mid],mid)         # [0,mid)
    a_right=merge_sort(a[mid:],n-mid)      # [mid,n)
    # print("n_left=",a_left,", n_right=",a_right)

    # 2. merge
    i,left_len=0,len(a_left)
    j,right_len=0,len(a_right)
    for k in range(0,n):
        if i>=left_len:
            a[k:]=a_right[j:]
            break
        elif j>=right_len:
            a[k:]=a_left[i:]
            break
        if a_left[i]<a_right[j]:
            a[k]=a_left[i]
            i+=1
        else:
            a[k]=a_right[j]
            j+=1
    # print("a=",a)
    return a


def merge_sort_optimize(a,n):
    '''
    归并排序 －－ 优化（非数量级上的优化，但让性能更优）

    1. 序列分到比较小时，近乎有序的概率比较大，使用插入排序更优
        插入排序：O(n^2); 归并排序：O(n*logn) 
        插入排序的O(n^2)系数比归并排序的O(n*logn)小
        n 小到一定程度时，插入排序比较快

    2. 前后段已经有序，可直接合并返回（对完全随机的序列效果不是很明显）
    '''

    if n<=1:
        return a

    # optimize1: 序列分到比较小时，近乎有序的概率比较大，使用插入排序
    if n<=10:
        sortBasic.insertion_sort_optimize(a,0,n)
        return a
    
    # 1. seperate
    mid=n//2
    # print("p_left=",a[:mid],", p_right=",a[mid:])
    a_left=merge_sort_optimize(a[:mid],mid)         # [0,mid)
    a_right=merge_sort_optimize(a[mid:],n-mid)      # [mid,n)
    # print("n_left=",a_left,", n_right=",a_right)

    # 2. merge
    i,left_len=0,len(a_left)
    j,right_len=0,len(a_right)

    # optimize2: 前后段已经有序，可直接合并返回
    if a_left[mid-1]<=a_right[0]:
        a[0:]=a_left+a_right
        return a

    for k in range(0,n):
        if i>=left_len:
            a[k:]=a_right[j:]
            break
        elif j>=right_len:
            a[k:]=a_left[i:]
            break
        if a_left[i]<a_right[j]:
            a[k]=a_left[i]
            i+=1
        else:
            a[k]=a_right[j]
            j+=1
    # print("a=",a)
    return a

###############################################

def quick_sort_one_partition(a,n):
    
    '''
    partition: 分一块，左边为小于v的，剩下则为大于等于v的
    （一个指针j指向左边为小于v的最后一个）

    －－－－－－－－－－－－－－－－－
    |v|  <v  |   >=v  |e|      |
    －－－－－－－－－－－－－－－－－
     l      j j+1      i        r

    a[l+1,j] < v <= a[j+1,i-1]

    v   : a[l]
    <v  : a[l+1,j]
    >=v : a[j+1,i-1]
    e   : a[i,r-1]

    j: 指向小于v的最后一个元素, initial: j=l
    i: 指向待判断元素, initial: i=l+1

    i in [l+1,r-1] :
        a[i]<v      =>  a[j+1]<->a[i],j++
        a[i]>=v     =>  /
    => j
    => a[l]<->a[j]
    => 返回j,分界点
    '''
    def one_partition(a,l,r):

        v=a[l]
        j=l
        for i in range(l+1,r):
            if a[i]<v:
                a[j+1],a[i]=a[i],a[j+1]
                j+=1
        a[l],a[j]=a[j],a[l]
        return j

    def do_quick_sort(a,l,r):
        if l>=r-1:
            return
        j=one_partition(a,l,r)
        do_quick_sort(a,l,j)
        do_quick_sort(a,j+1,r)


    do_quick_sort(a,0,n)


def quick_sort_two_partition(a,n):
    '''
    partition: 分两块，左端为小于等于v的，中间为待判别元素，右端为大于等于v的
    (等于v的分散在左右两侧，左右i,j两指针）
    
    －－－－－－－－－－－－－－－－－------
    |v|    <=v    |e|      |    >=v  |
    －－－－－－－－－－－－－－－－－------
     l             i      j j+1       r

    a[l+1,i-1] <= v <= a[j+1,r-1]

    v   : a[l]
    <=v : a[l+1,i-1]
    >=v : a[j+1,r-1]
    e   : a[i,j]

    i: 指向待判断的第一个元素, initial: i=l+1
    j: 指向待判断的最后一个元素, initial: j=r-1
    
    while True:
        # 不使用等号 a[i]<=v,a[j]>=v
        # eg: [5,3,2,5,5,5,7,8] 有多个连续相同的值
        # 多了等号会将这些值归到其中一边，造成两颗子树不平衡 => [3,2]5[5,5,7,8]
        # 不使用等号，分到中间，两颗子树更平衡 => [3,2,5]5[5,5,7,8]
        while i<r and a[i]<v : i++
        while j>l and a[j]<v : j--
        if i>=j:
            break
        a[i]<->a[j],i++,j--
    => j
    => a[l]<->a[j]
    => 返回j,分界点
    '''
    def two_partition(a,l,r):
        v=a[l]
        
        i,j=l+1,r-1
        while True:
            while i<r and a[i]<v:
                i+=1
            while j>l and a[j]>v:
                j-=1
            if i>=j:
                break
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1

        a[l],a[j]=a[j],a[l]
        return j

    def do_quick_sort(a,l,r):
        if l>=r-1:
            return
        j=two_partition(a,l,r)
        # print(a[l:j],a[j],a[j+1:r])
        do_quick_sort(a,l,j)
        do_quick_sort(a,j+1,r)

    do_quick_sort(a,0,n)


def quick_sort_three_partition(a,n):
    '''
    partition: 分三块，左端为小于v的，然后是等于v的，中间为待判别元素，右端为大于v的
    (左lt指针，相对于分一块方式，多了一个gt指针）
    
    －－－－－－－－－－－－－－－－－-------------
    |v|    <v    |   =v   |e|      |    >v  |
    －－－－－－－－－－－－－－－－－-------------
     l         lt          i        gt       r

    a[l+1,lt], a[lt+1,i-1], a[i,gt-1], a[gt,r-1]
        <v          =v         e         >v

    lt: 指向小于v的最后一个元素
    gt: 指向大于v的第一个元素

    i in [l+1,r-1]:
        a[i]<v      =>  a[i]<->a[lt], lt++, i++
        a[i]==v     =>  i++
        a[i]>v      =>  a[i]<->a[gt], gt--, /
        i==gt       =>  break
    => lt,gt
    => a[l]<->a[lt]
    => 返回lt,gt,分界点
    '''
    def three_partition(a,l,r):
        v=a[l]
        lt,gt=l,r
        i=l+1
        while i<r:
            if a[i]<v:
                a[i],a[lt+1]=a[lt+1],a[i]
                lt+=1
                i+=1
            elif a[i]>v:
                a[i],a[gt-1]=a[gt-1],a[i]
                gt-=1
            else:
                i+=1
            if i>=gt:
                break
        a[l],a[lt]=a[lt],a[l]
        return lt,gt

    def do_quick_sort(a,l,r):
        if l>=r-1:
            return

        lt,gt=three_partition(a,l,r)
        # print(a[l:lt],a[lt:gt],a[gt:r])
        do_quick_sort(a,l,lt)         # [l,lt-1]
        do_quick_sort(a,gt,r)         # [gt,r-1]

    do_quick_sort(a,0,n)


def quick_sort_optimize(a,n):
    '''
    优化：
    
    1. 小序列时，采用插入排序
    
    2. 快爬无法保证partition可以对分，时间复杂度无法保证为O(N*logN)
        
        近乎有序数组时，树的平衡度很差，无法保证树高度为logN
        极端情况下，有序数组，则树的一边高度即为N，时间复杂度退化到O(N^2)
        比归并排序O(N*logN)慢的多
        
        solution:
            随机选择标定元素，交换到数组头(a[l])后再进行partition
            (退化到O(N^2)的概率降低了很多)

    3. 对于有很多重复元素的序列
        可使用2路快排（重复元素分散到左右子树）
        或进一步3路快排（划分出相等的元素块，不用对重复元素做重复操作）

    4. 使用赋值操作减少交换操作

    '''

    def two_partition(a,l,r):

        # optimize2: 随机选择标定元素(对于近乎有序数组，平衡左右子树，减少到退化到O(N^2)的概率)
        # i=random.randint(l,r-1)   # 耗时
        i=(l+r)//2
        a[i],a[l]=a[l],a[i]

        v=a[l]

        '''
        # optimize: 等于v的分散在左右两侧
        '''
        i,j=l+1,r-1
        while True:
            while i<r and a[i]<v:
                i+=1
            while j>l and a[j]>v:
                j-=1
            if i>=j:
                break
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        a[l],a[j]=a[j],a[l]
        
        '''
        optimize: 使用赋值操作减少交换操作
            尾部指针，从后往前，找到比基准小的值，拷贝数据到头指位置
            头部指针，从前往后，找到比基准大的值，拷贝数据到尾指位置
            头尾部指针交替运行，直到相遇，拷贝基准值到该位置
        => 等于v的会集中在某一侧
        => 有大量重复元素时，不推荐
        '''
        # i,j=l,r-1
        # while i<j:
        #     while j>i and a[j]>=v:
        #         j-=1
        #     a[i]=a[j]
        #     while i<j and a[i]<v:
        #         i+=1
        #     a[j]=a[i]
        # a[j]=v

        return j

    def do_quick_sort(a,l,r):
        if l>=r-1:
            return

        # optimize1: 使用插入排序(小序列，近乎有序)
        # if r-l<=10:
        #     sortBasic.insertion_sort_optimize(a,l,r)

        # optimize3: 使用2/3路快排(大量重复元素)
        j=two_partition(a,l,r)
        #print(a[l:j],a[j],a[j+1:r])
        do_quick_sort(a,l,j)
        do_quick_sort(a,j+1,r)

    do_quick_sort(a,0,n)


###############################################


def heap_sort(a,n):
    
    # 1. build maxHeap
    # 自底向上，找到第一个非叶子节点，逐个往前，每个做shiftDown
    # 第一个非叶子节点 = (last_index-1)//2, 几乎从半数开始，更快
    def heapify(a,n):
        p=(n-2)//2
        while p>=0:
            shiftDown(a,n,p)
            p-=1

    def shiftDown(a,n,i):
        while i<n:
            l=2*i+1
            r=l+1
            max_c=l
            if l>=n:
                break
            if r<n and a[l]<a[r]:
                max_c=r
            if a[i]<a[max_c]:
                a[i],a[max_c]=a[max_c],a[i]
                i=max_c
            else:
                break

    # 2. pop max => sorted
    def extractMax(a,n):
        for i in range(n-1,0,-1):    # [n-1,1]
            a[0],a[i]=a[i],a[0]
            shiftDown(a,i,0)

    heapify(a,n)
    extractMax(a,n)


if __name__ == '__main__':

    # n=20
    # a=[61,90,31,5,51,78,20,4,94,67]
    # a=[5,3,2,5,5,5,5,5,7,8]
    # a=sortTestHelper.generateRandomArray(n,0,100,printArray=False)
    # a=sortTestHelper.generateNearlyOrderedArray(n,swapTimes=10,printArray=False)
    # sortTestHelper.testSort("Merge Sort",merge_sort,a+[],n,printArray=False)
    # sortTestHelper.testSort("Merge Sort(Opt)",merge_sort_optimize,a+[],n,printArray=False)
    # sortTestHelper.testSort("Quick Sort(1)",quick_sort_one_partition,a+[],n,printArray=False)
    # sortTestHelper.testSort("Quick Sort(2)",quick_sort_two_partition,a+[],n,printArray=False)
    # sortTestHelper.testSort("Quick Sort(3)",quick_sort_three_partition,a+[],n,printArray=False)
    # sortTestHelper.testSort("Quick Sort(Opt)",quick_sort_optimize,a+[],n,printArray=False)
    # sortTestHelper.testSort("Heap Sort",heap_sort,a+[],n,printArray=False)

    # print("#### random array ### ")
    # for i in range(4,6):
    #     n=10**i
    #     a=sortTestHelper.generateRandomArray(n,0,100)
    #     # sortTestHelper.testSort("Selection Sort",sortBasic.selection_sort,a+[],n)
    #     # sortTestHelper.testSort("Insertion Sort(Opt)",sortBasic.insertion_sort_optimize,a+[],n,start=0)
    #     # sortTestHelper.testSort("Shell Sort",sortBasic.shell_sort,a+[],n)
        
    #     # sortTestHelper.testSort("Merge Sort",merge_sort,a+[],n)
    #     # sortTestHelper.testSort("Merge Sort(Opt)",merge_sort_optimize,a+[],n)
        
    #     # sortTestHelper.testSort("Quick Sort(1)",quick_sort_onepartition,a+[],n)
    #     sortTestHelper.testSort("Quick Sort(2)",quick_sort_two_partition,a+[],n)
    #     sortTestHelper.testSort("Quick Sort(3)",quick_sort_three_partition,a+[],n)
    #     sortTestHelper.testSort("Quick Sort(Opt)",quick_sort_optimize,a+[],n)

    #     sortTestHelper.testSort("Heap Sort",heap_sort,a+[],n)
    #     print("---"*10)
    
    # print("#### random nearly ordered array ### ")
    # for i in range(4,6):
    #     n=10**i
    #     a=sortTestHelper.generateNearlyOrderedArray(n,swapTimes=int(n*0.05))
    #     # sortTestHelper.testSort("Selection Sort",sortBasic.selection_sort,a+[],n)
    #     # sortTestHelper.testSort("Insertion Sort(Opt)",sortBasic.insertion_sort_optimize,a+[],n,start=0)
    #     # sortTestHelper.testSort("Shell Sort",sortBasic.shell_sort,a+[],n)
        
    #     # sortTestHelper.testSort("Merge Sort",merge_sort,a+[],n)
    #     # sortTestHelper.testSort("Merge Sort(Opt)",merge_sort_optimize,a+[],n)

    #     # sortTestHelper.testSort("Quick Sort(1)",quick_sort_one_partition,a+[],n)
    #     sortTestHelper.testSort("Quick Sort(2)",quick_sort_two_partition,a+[],n)
    #     sortTestHelper.testSort("Quick Sort(3)",quick_sort_three_partition,a+[],n)
    #     sortTestHelper.testSort("Quick Sort(Opt)",quick_sort_optimize,a+[],n)
        
    #     sortTestHelper.testSort("Heap Sort",heap_sort,a+[],n)
    #     print("---"*10)


