##########################################
# sort usage
##########################################


'''
1. 排序：几乎有序数组，排好每个元素移动的距离<k（k相对N很小）,选择何种排序较好？
    - O(N) => 桶排序：不适用于比较排序
    - O(N^2) => Insertion Sort：与原始顺序有关 ＝> O(N*k)
    - O(N*logN) => Heap Sort: 前k个数建立小根堆，弹出堆顶，在加入第k+1调整，改进后，每得到一个数O(logk) ＝> O(N*logk)
'''
def sort_by_sub_heap(a,k):
    n=len(a)
    print("n = %d,k = %d, a = %s" % (n,k,a))

    # Heap Sort
    # heapify: top -> bottom, left -> right

    def heapify_min(a,n,i):
        i_min=i
        while i<n:
            i_left, i_right = 2*i+1, 2*i+2
            if i_left<n and a[i_left]<a[i_min]:
                i_min=i_left
            if i_right<n and a[i_right]<a[i_min]:
                i_min=i_right
            if i_min!=i:
                a[i],a[i_min]=a[i_min],a[i]
                i=i_min
            else:
                break

    def build_heap(a):
        n=len(a)
        p=(n-2)//2
        while p>=0:
            heapify_min(a,n,p)
            p-=1

    i=0
    while i<n:
        b=a[i:i+k]
        print("s = %d, e = %d, a = %s, %s, %s" % (i,i+k,a[:i],a[i:i+k],a[i+k:]))
        build_heap(b)
        a[i:i+k]=b
        i+=1

    print("Final: a =",a)

def sort_by_sub_heap_2(a,k):
    n=len(a)
    print("n = %d,k = %d, a = %s" % (n,k,a))

    # Heap Sort
    # heapify: top -> bottom, left -> right
    def heapify_min(a,start,end,i):
        i_min=i
        while i>=start and i<end:
            i_left, i_right = 2*i+1-start, 2*i+2-start
            if i_left<end and a[i_left]<a[i_min]:
                i_min=i_left
            if i_right<end and a[i_right]<a[i_min]:
                i_min=i_right
            if i_min!=i:
                a[i],a[i_min]=a[i_min],a[i]
                i=i_min
            else:
                break

    def build_heap(a,start,end):
        p=(end-start-2)//2+start
        #print("p=",p)
        while p>=start:
            heapify_min(a,start,end,p)
            p-=1

    i=0
    while i<n:
        start,end=i,i+k
        if end > n:
            end=n
        print("s = %d, e = %d, a = %s, %s, %s" % (start,end,a[:start],a[start:end],a[end:]))
        build_heap(a,start,end)
        i+=1
        #print("s = %d, e = %d, p = %s, a = %s" % (start,end,a[start:end],a))

    # for i in range(0,len(a)-k):
    #     build_heap(a,i,k)
    #     print("i = %d, a = %s" % (i,a))

    print("Final: a =",a)


'''
2. 判断：判断数组中是否有重复值，且额外的空间复杂度为O(1)
    - 空间复杂度限制  => 可使用HashTable实现, 时间 & 空间复杂度为 O(N)
    - 空间复杂度O(1) => 非递归的堆排序
'''
def is_exist_multi_value(a):
    n=len(a)
    print("n = %d, a = %s" % (n,a))

    def heapify(a,n,i):
        i_min=i
        while i<n:
            i_left, i_right = 2*i+1, 2*i+2
            if i_left<n:
                if a[i_left]<a[i_min]:
                    i_min=i_left
                elif a[i_left]==a[i_min]:
                    return True,a[i_min]
            if i_right<n:
                if a[i_right]<a[i_min]:
                    i_min=i_right
                elif a[i_right]==a[i_min]:
                    return True,a[i_min]
            if i_min!=i:
                a[i],a[i_min]=a[i_min],a[i]
                i=i_min
            else:
                break
        return False,a[i_min]

    p=(n-2)//2
    while p>=0:
        found,value=heapify(a,n,p)
        print("p=%d, (%s,%d), a=%s" % (p,found,value,a))
        if found:
            print("Found Repetition Num:",value)
            break;
        p-=1

    if not found:
        for i in range(n-1,0,-1):
            a[0],a[i]=a[i],a[0]
            found,value=heapify(a,i,0)
            print("i=%d, (%s,%d), a=%s" % (i,found,value,a))
            if found:
                print("Found Repetition Num:",value)
                break;
        if not found:
            print("Not Found Repetition Num !")


'''
3. 归并排序：将两个有序数组A & B，合并为一个有序数组（第一个数组A，空间刚好可容纳两个数组的元素）
    - A & B从后往前比较
    - 从A尾往前，按序插入
'''
def merge_sorted_seq(a,b):
    n_a=len(a)
    n_b=len(b)
    print("a = %s, len = %d" % (a,n_a))
    print("b = %s, len = %d" % (b,n_b))

    k=n_a+n_b-1
    
    a+=[0]*len(b)
    result,i,j=a,n_a-1,n_b-1

    while k>=0 and i>=0 and j>=0:
        if a[i]>=b[j]:
            result[k]=a[i]
            i-=1
            #print("choose a, ",result)
        else:
            result[k]=b[j]
            j-=1
            #print("choose b, ",result)
        k-=1
    # print("k=%d,i=%d,j=%d" % (k,i,j))
    if i>=0:
        result[:k+1]=a[:i+1]
    elif j>=0:
        result[:k+1]=b[:j+1]

    print("Final: a = %s, len = %d" % (a,len(a)))


'''
4. 排序：荷兰国际问题，只包含0，1，2的整数数组（只有3种数）排序（要求使用交换，原地排序，不利用计数排序）
    - 类似QuickSort划分partition过程
    - `{0区}[...]{2区}`
        + 遇到1，跳到下一个
        + 遇到0，与{0区}外第一个数进行交换，0区向右扩一个位置
        + 遇到2，与{2区}外第一个数进行交换，2区向左扩一个位置
    - 时间复杂度: O(N), 额外空间复杂度: O(1)

    {}[ 1, 1, 0, 0, 2, 1, 1, 0 ]{}
              *
    {0,  }[ 1, 1, 0, 2, 1, 1, 0 ]{}
               *--*
    {0, 0, }[ 1, 1, 2, 1, 1, 0 ]{}
                 *--*
    {0, 0, }[ 1, 1, 0, 1, 1 ]{ ,2}
                    *
    {0, 0, 0, }[ 1, 1, 1, 1 ]{ ,2}
                    *
'''
def partition_sort(a):
    n=len(a)
    print("n = %d, a = %s" % (n,a))
    
    k=1
    i,j=0,n-1
    while i<n and j>=0 and i<=j and k<=j:
        if a[k]==0:
            a[k],a[i]=a[i],a[k]
            i+=1
        elif a[k]==2:
            a[k],a[j]=a[j],a[k]
            j-=1
        else:
            k+=1
        print(a)


'''
5. 一个无序数组排序后，相邻两数的最大差值
    7，9，3，4，2，1，8 => 1,2,3,4,7,8,9 => 7-4=3
    
    - 类似桶排序
    - 第一次遍历，找出最大最小值，[min,max)等量分成n个区间,max值单独一个桶，共计n+1个桶
    - 将n个数依次放入各个桶区间
    - n个数，n+1个桶，必然会出现空桶
    - 同一个桶的数的差值不会大于桶区间，只需考虑桶与桶之间数的差值，而空桶两侧的差值一定大于桶区间
'''
def max_sorted_distance(a):
    n=len(a)
    print("n = %d, a = %s" % (n,a))
    max_a=max(a)
    min_a=min(a)
    interval=(max_a-min_a)/n
    print("min = %d, max = %d, interval = %f" % (min_a,max_a,interval))

    buckets=[[] for i in range(0,n+1)]
    for i in range(0,n):
        k=int((a[i]-min_a)/interval)
        buckets[k].append(a[i])
    print(buckets)

    max_b,b,max_d=0,0,0
    for i in range(0,n+1):
        if not buckets[i]:
            b+=1
        else:
            if b>max_b:
                max_b=b
                max_d=min(buckets[i])-max(buckets[i-max_b-1])
                #print(buckets[i],buckets[i-max_b-1],max_d)
            b=0
    print("max distance:",max_d)


'''
6. 查找：一个数组需要排序的最短子数组长度，尽量时间复杂度: O(N), 额外空间复杂度: O(1)
    [1,5,4,3,2,6,7] 
        => [5,4,3,2] 
        => min: 4
    [1,5,4,3,2,6,7,10,9,8,10,12] 
        => [5,4,3,2] & [10,9,8] 
        => min: 3
    [1,3,5,7,9,10,12,6,8,14,16,18,20,22,24,17,21,19,25]
        => [7,9,10,12,6,8]
        => [18,20,22,24,17,21,19]
        => 6
    
    - 从左往右，求无序时最右的位置: 记录最大值，记录比它小的数的最后位置
        + max: 1,3,5,7,9,10,12,| 14,16,18,20,22,24,| 25
        + l: 6,8,| 17,21,19 => 19 a[17]
    - 从右往左，求无序时最左的位置: 记录最小值，记录比它大的数的最后位置 
        + min: 25,19,| 17,| 16,14,8,6,| 5,3,1
        + l: 21,| 24,22,20,18,| 12,10,9,7 => 7 a[3]
    - 两个位置相减+1得结果
        + => 15
        + 注：此算法无法排除无序子表中正确位置的元素，所以结果为15，不是6 ！最准确的还是先排序后比较
'''
def min_unsorted_sequence(a):
    print("a=",a)
    n=len(a)
    max_a,L_to_R=a[0],0
    min_a,R_to_L=a[n-1],n-1

    for i in range(1,n):
        if a[i]>max_a:
            max_a=a[i]
        else:
            L_to_R=i
    print("max_a=%d,L_to_R=%d,a[L]=%d" % (max_a,L_to_R,a[L_to_R]))

    for i in range(n-2,-1,-1):
        if a[i]<min_a:
            min_a=a[i]
        else:
            R_to_L=i
    print("min_a=%d,R_to_L=%d,a[R]=%d" % (min_a,R_to_L,a[R_to_L]))

    print("sub to sort len:%d" % (L_to_R-R_to_L+1) )
    print("sub to sort seq:%s" % a[R_to_L:L_to_R+1] )

def get_min_unsorted_sequence(a):
    
    b=a+[]
    print("unsorted:",a)

    # 1. quick sort
    def quick_sort(a,start,end):
        if start>=end:
            return
        base,l,r=a[start],start,end
        while l!=r:
            while a[r]>=base and l<r:
                r-=1
            a[l]=a[r]
            
            while a[l]<base and l<r:
                l+=1
            a[r]=a[l]
        a[l]=base
        # print("b = %s, a = %s" % (base,a))
        quick_sort(a,start,l-1)
        quick_sort(a,l+1,end)

    n=len(a)
    quick_sort(a,0,n-1)
    print("sorted : ",a)

    # 2. compare
    cnt=0
    min_cnt=len(a)
    for i,item in enumerate(a):
        if item!=b[i]:
            cnt+=1
        else:
            if cnt<min_cnt and cnt!=0:
                min_cnt=cnt
                min_seq=a[i-cnt:i]
            cnt=0

    print("min_cnt: %d, min_seq: %s" % (min_cnt,min_seq))



if __name__=='__main__':

    # a = [54,26,93,17,77,31,44,55,20]
    # a = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]

    # # 1. 排好每个元素移动的距离<k,使用改进版堆排序：
    # a = [1,5,2,3,4,6,7,10,9,8,12,11]
    # sort_by_sub_heap(a,4)       # sort_by_sub_heap_2(a,4)

    # # 2. 判断数组中是否有重复值
    # a = [54,26,77,17,77,31,44,55,20]
    # a = [54,54,77,17,77,31,44,55,20]
    # is_exist_multi_value(a)

    # # 3. 将两个有序数组A & B，合并为一个有序数组到A
    # a,b=[5,9,11,13,15],[1,2,6,8,10,12,14,16]
    # merge_sorted_seq(a,b)

    # # 4. 对只包含0，1，2的整数(只有3种数)数组排序
    # a = [1, 1, 0, 0, 2, 1, 1, 0]
    # a = [1, 2, 0, 0, 2, 1, 1, 0]
    # a = [2, 1, 0, 2, 1, 1, 2,0,1,1,0,0,2,0]
    # partition_sort(a)

    # # 5. 无序数组排序后，相邻两数的最大差值
    # a=[7,9,5,4,2,1,8,10,13,17,34,38]
    # max_sorted_distance(a)

    # # 6. 获取一个数组需要排序的最短子数组
    a=[1,3,5,7,9,10,12,6,8,14,16,18,20,22,24,17,21,19,25]
    # min_unsorted_sequence(a)
    get_min_unsorted_sequence(a)
    


