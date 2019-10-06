
'''
| 排序算法 | 最优~平均~最坏时间复杂度 | 空间复杂度 | 稳定性 | 过程 | 
|:-------|:-------|:-------|:-------|:-------|
| 1.插入式： | - | - | - | - |
| 插入排序(Insertion)  | `O(N)`~`O(N^2)`~`O(N^2)` | `O(1)` | 稳定 | `[min,...,max | <=,....]` | 
| 希尔排序(Shell) | `O(N*logN)`~`O(N^1.3)`~`O(N^2)` | `O(1)` | 不稳定 | `[min,...,,max| <=...]` |
| 归并排序(Merge) | `O(N*logN)` | `O(N)` | 稳定 | `[ | ] <=> [][]|[][]` |
| 2.选择式： | - | - | - | - |
| 选择排序(Selection) | `O(N^2)` | `O(1)` | 不稳定 | `[min, | <=...min...]` |
| 堆排序(Heap) | `O(N*logN)` | O(1) | 不稳定 | tree: `top,left_child,right_child` |
| 3.交换式： | - | - | - | - | - | - |
| 冒泡排序(Bubble) | `O(N`)~`O(N^2)`~`O(N^2)` | `O(1)` | 稳定 | `[<=> |->,max]` |
| 快速排序(Quick) | `O(N*logN)`~`O(N*logN)`~`O(N^2)` | `O(logN)~O(N)` | 不稳定 | `{low}[...][base]` |
    
- 时间复杂度: `O(N^2)`
    + 冒泡排序: O(N)~O(N^2)~O(N^2) => 快速排序: O(N*logN)~O(N*logN)~O(N^2)
    + 插入排序: O(N)~O(N^2)~O(N^2) => 希尔排序: O(N*logN)~O(N^1.3)~O(N^2)
    + 选择排序: O(N^2)~O(N^2)~O(N^2)
    
- 时间复杂度: `O(N*logN)`
    + 归并排序
    + 堆排序
'''

##########################################
# 比较排序
# 时间复杂度: O(N),O(N*logN),O(N^2)
##########################################

'''
1.1 冒泡排序(Bubble Sort): O(N)~O(N^2)~O(N^2)
`[<=> |->,max]` , 稳定
'''
def bubble_sort(a):
    print("冒泡排序(Bubble Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))
    
    for j in range(n-1,0,-1):
        change_cnt=0
        for i in range(0,j):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                change_cnt+=1
        print("j = %d, a = %s" % (j,a))
        if change_cnt==0:       # 时间复杂度最优 O(N)
            break;
        
    print("Final: a =",a)


'''
1.2 快速排序(Quick Sort): O(N*logN)~O(N*logN)~O(N^2)
`{low}[...][base]`, 不稳定
'''
def quick_sort(a):
    print("快速排序(Quick Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))
    
    def do_quick_sort(a,start,end):
        if start>=end:
            return
        
        base,l,r=a[start],start,end
        while l!=r:
            # for i in range(r,l,-1):
            #     if a[i]<base
            #         r=i
            #         break
            while a[r]>=base and l<r:
                r-=1
            a[l]=a[r]
            
            while a[l]<base and l<r:
                l+=1
            a[r]=a[l]
        a[l]=base
        print("b = %s, a = %s" % (base,a))

        do_quick_sort(a,start,l-1)
        do_quick_sort(a,l+1,end)


    do_quick_sort(a,0,n-1)
    print("Final: a =",a)


'''
2.1 插入排序(Insertion Sort): O(N)~O(N^2)~O(N^2)
`[min,...,max | <=,....]` , 不稳定
'''
def insertion_sort(a):
    print("插入排序(Insertion Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))
    
    # for j in range(1,n):
    #     i=j
    #     # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
    #     while i>=1:
    #         if a[i]<a[i-1]:
    #             a[i],a[i-1]=a[i-1],a[i]
    #             i-=1
    #         else:
    #             break
    #     print("j = %d, a = %s" % (j,a))

    for j in range(1,n):
        for i in range(j,0,-1):
            if a[i]<a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
            else:
                break
        print("j = %d, a = %s" % (j,a))

    print("Final: a =",a)
    

'''
2.2 希尔排序(Shell Sort): O(N*logN)~O(N^1.3)~O(N^2)
`[min,...,,max| <=...]` , 不稳定
'''
def shell_sort(a):
    print("希尔排序(Shell Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))
    
    step=n//2
    while step!=0:
        for j in range(step,n):     # 按步长进行插入排序
            i=j    
            while i>=step:
                if a[i]<a[i-step]:
                    # print("a[%d]=%d,a[%d]=%d" % (i,a[i],i-step,a[i-step]))
                    a[i],a[i-step]=a[i-step],a[i]
                    i-=step
                else:
                    break
            # print("j = %d, a = %s" % (j,a))

        print("g = %d, a = %s" % (step,a))
        step=step//2

    print("Final: a =",a)


'''
3. 选择排序(Selection Sort): O(N^2)
`[min, | <=...min...]` , 不稳定
'''
def selection_sort(a):
    print("选择排序(Selection Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))
    
    for j in range(0,n-1):
        min_index=j
        for i in range(j+1,n):
            if a[min_index]>a[i]:
                min_index=i
        a[j],a[min_index]=a[min_index],a[j]
        print("j = %d, a = %s" % (j,a))

    print("Final: a =",a)
    

'''
4. 归并排序(Merge Sort): O(N*logN)
`[ | ] <=> [][]|[][]` , 稳定
'''
def merge_sort(a):
    print("归并排序(Merge Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))

    def do_merge_sort(a):
        if len(a)<=1:
            return a
        mid=len(a)//2
        a_left=do_merge_sort(a[:mid])
        a_right=do_merge_sort(a[mid:])
        
        result,i,j=[],0,0
        while i<len(a_left) and j<len(a_right):
            if a_left[i]<a_right[j]:
                result.append(a_left[i])
                i+=1
            else:
                result.append(a_right[j])
                j+=1
        if i<len(a_left):
            result+=a_left[i:]
        else:
            result+=a_right[j:]

        print(a_left,a_right,"=>",result)
        return result

    a=do_merge_sort(a)
    print("Final: a =",a)
  

'''
5. 堆排序(Heap Sort): O(N*logN)
`left_child <- top -> right_child` , 不稳定
Heap: 
    complete binary tree
        parent=(i-1)/2
        left_child=2i+1
        right_child=2i+2
    parent>child
'''
def heap_sort(a,n=None):
    print("堆排序(Heap Sort)")
    if n is None:
        n=len(a)
    print("n = %d, a = %s" % (n,a))

    # heapify: top -> bottom, left -> right
    
    def heapify_max_recursion(a,n,i):
        if i>=n:
            return

        i_max, i_left, i_right = i, 2*i+1, 2*i+2
        if i_left<n and a[i_left]>a[i_max]:
            i_max=i_left
        if i_right<n and a[i_right]>a[i_max]:
            i_max=i_right
        if i_max!=i:
            a[i],a[i_max]=a[i_max],a[i]
            heapify_max_recursion(a,n,i_max)

    def heapify_max(a,n,i):
        i_max=i
        while i<n:
            i_left, i_right = 2*i+1, 2*i+2
            if i_left<n and a[i_left]>a[i_max]:
                i_max=i_left
            if i_right<n and a[i_right]>a[i_max]:
                i_max=i_right
            if i_max!=i:
                a[i],a[i_max]=a[i_max],a[i]
                i=i_max
            else:
                break

    def build_heap(a,n):
        p=(n-2)//2
        while p>=0:
            heapify_max(a,n,p)  # heapify_max_recursion(a,n,p)
            p-=1

    
    build_heap(a,n)
    print("Initial a =",a)
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        heapify_max(a,i,0)
        print('heapify a =',a)

    print("Final: a =",a)



'''
Start Test
'''

if __name__=='__main__':

    a = [54,26,93,17,77,31,44,55,20]
    # a = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    # a = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
    
    ############
    # 基于比较
    ############

    # # 1.1 冒泡排序(Bubble Sort)
    # bubble_sort(a+[])
    # print("***"*10)

    # # 1.2 快速排序(Quick Sort) 
    # quick_sort(a+[])
    # print("***"*10)

    # # 2.1. 插入排序(Insertion Sort) 
    # insertion_sort(a+[])
    # print("***"*10)

    # # 2.2 希尔排序(Shell Sort) 
    # shell_sort(a+[])
    # print("***"*10)

    # # 3. 选择排序(Selection Sort) 
    # selection_sort(a+[])
    # print("***"*10)

    # # 4 归并排序(Merge Sort) 
    # merge_sort(a+[])
    # print("***"*10)

    # # 5. 堆排序(Heap Sort) 
    # a=[4,10,3,5,1,2]
    # heap_sort(a+[])
    # print("***"*10)


