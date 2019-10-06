
def binary_search(a,target):
    print("二分查找：非递归实现")
    n=len(a)
    print("n = %d, a = %s" % (n,a))

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

    if isExist:
        print("Found %s in position %d " % (target,mid))
    else:
        print("Not Found %s" % target)
    

def binary_search_recur(a,target):
    print("二分查找：递归实现")
    n=len(a)
    print("n = %d, a = %s" % (n,a))

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

    isExist=do_binary_search(a,target)
    if isExist:
        print("Found %s " % target)
    else:
        print("Not Found %s" % target)
    

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
    
    binary_search(a,26)
    print("***"*10)
    binary_search(a,88)
    print("***"*10)

    binary_search_recur(a,26)
    print("***"*10)
    binary_search_recur(a,88)
    print("***"*10)

    a=[[0,1,2,5],
    [2,3,4,7],
    [4,4,4,8],
    [5,7,7,9]]
    sorted_matrix_search(a,3)

