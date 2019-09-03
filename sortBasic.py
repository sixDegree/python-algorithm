import sortTestHelper

'''
基础排序

平均时间复杂度：O(N^2)

1. 选择排序 Selection Sort
2. 插入排序 Insertion Sort -> 4. 希尔排序 Shell Sort
3. 冒泡排序 Bubble Sort
'''

def selection_sort(a,n):
    '''
    2层循环都必须执行完成，时间复杂度为O(N^2)
    '''
    for j in range(0,n-1):              # j: [0,n-2]
        min_index=j
        for i in range(j+1,n):          # i: [j+1,n-1]
            if a[min_index]>a[i]:
                min_index=i
        a[j],a[min_index]=a[min_index],a[j]


def insertion_sort(a,n):
    '''
    似打牌时整理牌

    2层循环，内层循环可提前终止，对近乎有序的效率更高

    时间复杂度：O(N^2), 有序时近乎 O(N) -- 内层循环很快退出
    '''
    for j in range(1,n):                # j: [1,n-1]
        for i in range(j,0,-1):         # i: [j,1]
            if a[i]<a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
            else:
                break

# def insertion_sort_optimize(a,n):
#     '''
#     1次交换，相当于3次赋值（temp暂存）－－ 优化：使用赋值来代替交换
#     '''
#     for j in range(1,n):                # j: [1,n-1]
#         t=a[j]
        
#         # i=j-1                         # i: [j-1,0]
#         # while i>=0 and a[i]>t:
#         #     a[i+1]=a[i]
#         #     i-=1
#         # a[i+1]=t

#         i=j                             # i: [j,1]
#         while i>0 and a[i-1]>t:
#             a[i]=a[i-1]
#             i-=1
#         a[i]=t

def insertion_sort_optimize(a,l,r):         # [l,r-1]
    '''
    1次交换，相当于3次赋值（temp暂存）－－ 优化：使用赋值来代替交换
    '''
    for j in range(l+1,r):                # j: [l+1,r-1]
        t=a[j]
        
        # i=j-1                             # i: [j-1,l]
        # while i>=l and a[i]>t:
        #     a[i+1]=a[i]
        #     i-=1
        # a[i+1]=t

        i=j                             # i: [j,l+1]
        while i>l and a[i-1]>t:
            a[i]=a[i-1]
            i-=1
        a[i]=t


def shell_sort(a,n):
    '''
    升级版的插入排序

    时间复杂度：O(N*logN)~O(N^2)，根据step不同而不同，统计平均：O(N^1.5)
    
    每次都和之前第step个元素比较
    step逐渐缩小到1，一步一步地将无序数组变成近乎有序地数组
    step为1时，则为普通的插入排序，排完，则得到最终有序数组
    （有序性强的数组，使用插入排序法，更快）
    '''
    step=n//2
    while step!=0:
        for j in range(step,n):             # j: [step,n-1]
            t=a[j]
            i=j
            while i>=step and a[i-step]>t:  # i:[j,1]
                a[i]=a[i-step]
                i-=step
            a[i]=t
        step=step//2


def bubble_sort(a,n):
    # for j in range(n-1,0,-1):                # j: [n-1,1]
    #     for i in range(0,j):                 # i: [0,j-1]
    #         if a[i]>a[i+1]:
    #             a[i],a[i+1]=a[i+1],a[i]

    for j in range(n-1,0,-1):                # j: [n-1,1]
        swap_cnt=0
        for i in range(0,j):                 # i: [0,j-1]
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                swap_cnt+=1
        if swap_cnt==0:
            break


if __name__ == '__main__':

    # n=10
    # a=sortTestHelper.generateRandomArray(n,0,100,printArray=True)
    # a=sortTestHelper.generateNearlyOrderedArray(n,swapTimes=10,printArray=False)
    # sortTestHelper.testSort("Selection Sort",selection_sort,a+[],n,printArray=False)
    # sortTestHelper.testSort("Insertion Sort",insertion_sort,a+[],n,printArray=False)
    # sortTestHelper.testSort("Insertion Sort(Opt)",insertion_sort_optimize,a+[],n,start=0,printArray=True)
    # sortTestHelper.testSort("Shell Sort",shell_sort,a+[],n,printArray=False)
    # sortTestHelper.testSort("Bubble Sort",bubble_sort,a+[],n,printArray=False)


    print("#### random array ### ")
    for i in range(2,5):
        n=10**i
        a=sortTestHelper.generateRandomArray(n,0,100)
        sortTestHelper.testSort("Selection Sort",selection_sort,a+[],n)
        sortTestHelper.testSort("Insertion Sort",insertion_sort,a+[],n)
        sortTestHelper.testSort("Insertion Sort(Opt)",insertion_sort_optimize,a+[],n,start=0)
        sortTestHelper.testSort("Shell Sort",shell_sort,a+[],n)
        sortTestHelper.testSort("Bubble Sort",bubble_sort,a+[],n)
        print("---"*10)
    
    print("#### random nearly ordered array ### ")
    for i in range(2,5):
        n=10**i
        a=sortTestHelper.generateNearlyOrderedArray(n,swapTimes=int(n*0.05))
        sortTestHelper.testSort("Selection Sort",selection_sort,a+[],n)
        sortTestHelper.testSort("Insertion Sort",insertion_sort,a+[],n)
        sortTestHelper.testSort("Insertion Sort(Opt)",insertion_sort_optimize,a+[],n,start=0)
        sortTestHelper.testSort("Shell Sort",shell_sort,a+[],n)
        sortTestHelper.testSort("Bubble Sort",bubble_sort,a+[],n)
        print("---"*10)




