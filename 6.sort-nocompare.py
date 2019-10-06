##########################################
# 不基于比较的排序
# 时间复杂度: O(N) ; 空间复杂度 O(M) 
##########################################

'''
1. 桶排序(bucket sort)
buckets: 最大最小平均间隔的桶（每个桶表示一个范围）
  [min_a,min_a+intervel),[...),[...),...,[max_a]
  intervel = (max_a-min_a)//n
  count = n+1
'''
def bucket_sort(a):
    print("桶排序(bucket Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))

    max_a=max(a)
    min_a=min(a)
    interval=(max_a-min_a)/n
    print("max_a = %d, min_a = %d, interval = %s" % (max_a,min_a,interval))

    # buckets use []
    buckets=[ [] for i in range(0,n+1)]
    for i in range(0,n):
        k=int((a[i]-min_a)/interval)
        print("a[%d] = %d, k = %d" % (i,a[i],k))
        buckets[k].append(a[i])
    print("buckets:",buckets,",len:",len(buckets))
    a.clear()
    for i in range(0,n+1):
        if buckets[i]:
            buckets[i].sort()
        a+=buckets[i]

    print("Final: a =",a)


'''
2 计数排序(Counting Sort)
 buckets: 从小到大所有数（每个桶为固定的一个数）
   [min],[min+1],[min+2],....,[max]
   intervel = 1
   count = max_a-min_a+1
''' 
def counting_sort(a):
    print("计数排序(Counting Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))

    max_a=max(a)
    min_a=min(a)
    print("max_a = %d, min_a = %d" % (max_a,min_a))

    # method1: buckets use []
    # buckets_cnt=max_a-min_a+1
    # buckets=[0]*buckets_cnt
    # for i in range(0,n):
    #     buckets[a[i]-min_a]+=1
    # print("buckets:",buckets)

    # a.clear()
    # for b in range(0,buckets_cnt):
    #     a+=[min_a+b]*buckets[b]

    # method2: buckets use {}
    buckets={ i:0 for i in range(min_a,max_a+1)}
    for i in range(0,n):
        buckets[a[i]]+=1
    print("buckets:",buckets,"len:",len(buckets))

    a.clear()
    for b in range(min_a,max_a+1):
        a+=[b]*buckets[b]

    print("Final: a =",a)


'''
3. 基数排序(Radis Sort)
buckets: 0～9余数做桶，逐各个位放入桶排序（循环轮数：最大数的位数）
  [0],[1],[2],[3],...,[8],[9]
  intervel = 1
  count = 10
'''
def radix_sort(a):
    print("基数排序(Radix Sort)")
    n=len(a)
    print("n = %d, a = %s" % (n,a))

    max_a_len=1
    max_a=max(a)
    while max_a>10**max_a_len:
        max_a_len+=1
    print("max_a = %d, max_a_len = %d" % (max_a,max_a_len))

    for k in range(0,max_a_len):
        buckets={ i:[] for i in range(0,10) }
        for i in range(0,n):
            buckets[int(a[i]/(10**k)%10)].append(a[i])
        # print("buckets = %s" % buckets)
        a.clear()
        for b in range(0,10):
            a+=buckets[b]
        print("k = %d, a = %s" % (k,a))

    print("Final: a =",a)



'''
Start Test
'''

if __name__=='__main__':

    a = [54,26,93,17,77,31,44,55,20]
    # a = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    # a = [13,14,94,33,82,25,59,94,65,23,45,27,73,25,39,10]
    
    ############
    # 不基于比较
    ############
   
    # # 1. 桶排序(Bucket Sort) 
    # a=[7,9,3,4,2,1,8]
    # bucket_sort(a+[])
    # print("***"*10)

    # # 2. 计数排序(Counting Sort) 
    # counting_sort(a+[])
    # print("***"*10)

    # # 3. 基数排序(Radix Sort) 
    # a=[23,1,101,72,84,11]
    # radix_sort(a+[])
    # print("***"*10)


        