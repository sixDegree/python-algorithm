'''
二分查找
'''


# 1. 非递归实现
def binary_search(a,target):
    n=len(a)
    #print("n = %d, a = %s" % (n,a))

    isExist=False
    start,end=0,n-1
    while start<=end:
        mid=(start+end)//2
        if a[mid]==target:
            isExist=True
            break;
        elif target<a[mid]:
            end=mid-1
        else:
            start=mid+1
    
    pos=-1
    if isExist:
        pos=mid

    return isExist,pos
    

# 2. 递归实现

def do_binary_search(a,target):
    n=len(a)
    if n<=0:
        return False

    start,end=0,len(a)-1
    mid=(start+end)//2
    if a[mid]==target:
        return True
    elif target<a[mid]:
        return do_binary_search(a[:mid],target)
    else:
        return do_binary_search(a[mid+1:],target)

  
def do_binary_search2(a,start,end,target):              # [start,end)
    if start>=end:
        return False,-1

    mid=(start+end)//2
    if a[mid]==target:
        return True,mid
    elif target<a[mid]:
        return do_binary_search2(a,start,mid,target)    # [start,mid)
    else:
        return do_binary_search2(a,mid+1,end,target)    # [mid+1,end)


###################################

'''
floor & ceil:
[17,20,26,31,44,54,55,77,93], target=56

    - floor 小于等于target的最大值： a[?]<=target, 左端最靠近target的元素
        floor(a,56)=55
        最近的左子树的右孩子中的最小值（前驱）
        mid<target => 右子树的最小值
    
    - ceil  大于等于target的最小值： a[?]>=target, 右端最靠近target的元素
        ceil(a,55)=77
        最近的右子树的左孩子中的最大值（后驱）
        mid>target => 左子树的最大值

floor <= target <= ceil
'''


# floorCeil - 非递归实现
def floorCeil(a,target):
    n=len(a)

    start,end=0,n-1
    while start<=end:
        mid=(start+end)//2
        if target==a[mid]:
            return a[mid],a[mid]
        elif target<a[mid]:
            end=mid-1
        else:
            start=mid+1

    return (end>=0 and a[end] or None ),(start<n and a[start] or None)

# floorCeil - 递归实现
def do_floorCeil(a,start,end,target):
    if start>=end:
        return None,None
    
    mid=(start+end)//2
    if a[mid]==target:
        return a[mid],a[mid]
    elif target<a[mid]:
        f,c=do_floorCeil(a,start,mid,target)
        return f,c or a[mid]
    else:
        f,c=do_floorCeil(a,mid+1,end,target)
        return f or a[mid],c

# floor - 递归实现

# def floor(a,start,end,target):
#     if start>=end:
#         return (start>=1 and a[start-1] or None)

#     mid=(start+end)//2
#     if a[mid]==target:
#         return True,a[mid]

#     elif target<a[mid]:
#         return floor(a,start,mid,target)
#     else:
#         return floor(a,mid+1,end,target)


def floor(a,start,end,target):
    if start>=end:
        return False,None

    mid=(start+end)//2
    if a[mid]==target:
        # 刚好找到相等的
        return True,a[mid]
    elif target<a[mid]:
        # 缩小范围，查找左子树
        return floor(a,start,mid,target)
    else: 
        # 缩小到不能再缩小范围，开始查找其右子树
        matched,result=floor(a,mid+1,end,target)
        # 找不到，取mid(右子树的前驱)
        return matched,(result or a[mid])
        
# ceil - 递归实现
def ceil(a,start,end,target):
    if start>=end:
        return False,None

    mid=(start+end)//2
    if a[mid]==target:
        # 刚好找到相等的
        return True,a[mid]
    elif target<a[mid]:
        # 查找左子树
        matched,result=ceil(a,start,mid,target)
        # 找不到，取mid(左子树的后驱)
        return matched,result or a[mid]
    else:
        matched,result=ceil(a,mid+1,end,target)
        return matched,result


def lower_upper(a,target):
    n=len(a)

    start,end=0,n-1
    while start<=end:
        mid=(start+end)//2
        if target==a[mid]:
            # return (mid-1>=0 and a[mid-1] or None),(mid+1<n and a[mid+1],None)
            end,start=mid-1,mid+1
            break
        elif target<a[mid]:
            end=mid-1
        else:
            start=mid+1

    return (end>=0 and a[end] or None ),(start<n and a[start] or None)



'''
查找应用：在行列都排好序的矩阵（每行每列从小到大）中找数
    0,1,2,5
    2,3,4,7
    4,4,4,8
    5,7,7,9
    
    - 类似二分查找，从右上角开始，往左或往下
    - 时间复杂度: O(m+n), 额外空间复杂度: O(1)
'''

def sorted_matrix_search(a,target):
    m=len(a)
    n=len(a[0])
    print("m * n = %d * %d" % (m,n))
    for i in range(0,len(a)):
        print(a[i])

    i,j=0,n-1,
    found=False
    while i<m and j>=0:
        print("a[%d][%d]=%d" % (i,j,a[i][j]))
        if target>a[i][j]:
            i+=1
        elif target<a[i][j]:
            j-=1
        else:
            found=True
            break;

    if found:
        print("Found %d in (%d,%d)" % (target,i,j))
    else:
        print("Not Found %d" % target)



if __name__=='__main__':

    a = [17, 20, 26, 31, 44, 54, 55, 77, 93]    # sorted
    n=len(a)
    print("n = %d, a = %s" % (n,a))
    

    # 1. binarySearh - 非递归实现
    isExist,pos=binary_search(a,26)
    print("search 26:",isExist,pos)
    print("***"*10)
    
    isExist,pos=binary_search(a,88)
    print("search 88:",isExist,pos)
    print("***"*10)

    # 2. binarySearch - 递归实现1
    isExist=do_binary_search(a,26)
    print("do search 26:",isExist)
    print("***"*10)
    
    isExist=do_binary_search(a,88)
    print("do search 88:",isExist)
    print("***"*10)

    # 2. binarySearch - 递归实现2
    isExist,pos=do_binary_search2(a,0,n,26)
    print("do search2 26:",isExist,pos)
    print("***"*10)
    
    isExist,pos=do_binary_search2(a,0,n,88)
    print("do search2 88:",isExist,pos)
    print("***"*10)

    # 3. floorCeil - 非递归实现
    print("26 floorCeil:",floorCeil(a,26))
    print("31 floorCeil:",floorCeil(a,31))
    print("55 floorCeil:",floorCeil(a,55))
    
    print("17 floorCeil:",floorCeil(a,17))
    print("93 floorCeil:",floorCeil(a,93))
    
    print("56 floorCeil:",floorCeil(a,56))
    print("15 floorCeil:",floorCeil(a,15))
    print("95 floorCeil:",floorCeil(a,95))
    print("***"*10)

    # 4. floorCeil - 递归实现
    print("26 do_floorCeil:",do_floorCeil(a,0,n,26))
    print("31 do_floorCeil:",do_floorCeil(a,0,n,31))
    print("55 do_floorCeil:",do_floorCeil(a,0,n,55))
    
    print("17 do_floorCeil:",do_floorCeil(a,0,n,17))
    print("93 do_floorCeil:",do_floorCeil(a,0,n,93))
    
    print("56 do_floorCeil:",do_floorCeil(a,0,n,56))
    print("15 do_floorCeil:",do_floorCeil(a,0,n,15))
    print("95 do_floorCeil:",do_floorCeil(a,0,n,95))
    print("***"*10)

    # 5. floor - 递归实现
    print("26 floor:",floor(a,0,n,26))
    print("31 floor:",floor(a,0,n,31))
    print("55 floor:",floor(a,0,n,55))
    
    print("17 floor:",floor(a,0,n,17))
    print("93 floor:",floor(a,0,n,93))
    
    print("56 floor:",floor(a,0,n,56))
    print("15 floor:",floor(a,0,n,15))
    print("95 floor:",floor(a,0,n,95))
    print("***"*10)

    # 6. ceil - 递归实现
    print("26 ceil:",ceil(a,0,n,26))
    print("31 ceil:",ceil(a,0,n,31))
    print("55 ceil:",ceil(a,0,n,55))
    
    print("17 ceil:",ceil(a,0,n,17))
    print("93 ceil:",ceil(a,0,n,93))
    
    print("56 ceil:",ceil(a,0,n,56))
    print("15 ceil:",ceil(a,0,n,15))
    print("95 ceil:",ceil(a,0,n,95))
    print("***"*10)

    # 7. lower & upper
    print("26 lower_upper:",lower_upper(a,26))
    print("31 lower_upper:",lower_upper(a,31))
    print("55 lower_upper:",lower_upper(a,55))
    
    print("17 lower_upper:",lower_upper(a,17))
    print("93 lower_upper:",lower_upper(a,93))
    
    print("56 lower_upper:",lower_upper(a,56))
    print("15 lower_upper:",lower_upper(a,15))
    print("95 lower_upper:",lower_upper(a,95))
    print("***"*10)

    # 8. 在行列都排好序的矩阵（每行每列从小到大）中找数
    # a=[[0,1,2,5],
    # [2,3,4,7],
    # [4,4,4,8],
    # [5,7,7,9]]
    # sorted_matrix_search(a,3)

