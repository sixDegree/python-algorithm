'''
Binary Search Tree 二分搜索树
    - 二叉树（不一定完全）
    - 左孩子 < parent < 右孩子

优势：

| 数据结构   | 查找    | 插入    | 删除      |
|:---------|:-------|:--------|:---------|
| 普通数组   | O(N)   | O(N)    | O(N)     |
| 有序数组   | O(logN)| O(N)    | O(N)     |
| 二分搜索树 | O(logN) | O(logN) | O(logN) |

应用：
    查找表的实现－字典数据结构（key-value) => 优化：Trie字典树

遍历：
    - 深度优先遍历（递归，或借助栈，先进后出）：前序，中序（从小到大序列），后序（应用：释放）
    - 广度优先遍历（借助队列，先进先出）     ：层序

顺序性：
    - 最小／大节点            ： minmum,maximum
    - 某节点的前驱／后驱节点    ： predecessor,successor
    - 上下最接近或等于某值的节点 ： floor,ceil
    - 某节点的排名／某排名的节点 ： rank,select （实现思路：每个节点保存以它为根的树的节点总量）

扩展：支持重复元素
    - 给每个Node增加一个计数值
    - 或添加节点

局限性：
    同样的数据可对应不同的二分搜索树（如：插入顺序不同就可能不同），不能保证O(logN)
        3
       / \
      1   4
       \
        2

    1 
     \
      2
       \
        3
         \
          4  => 推化成链表 O(N)

    => 优化：平衡二叉树（左右子树高度差不超过1），实现：红黑树，2-3 Tree，AVL Tree，Splay Tree

'''
class Node:
    def __init__(self,key=None,value=None,lchild=None,rchild=None):
        self.key=key
        self.value=value
        self.lchild=lchild
        self.rchild=rchild

    def __str__(self):
        return "%s %s" % (self.key,self.value or "")

    def __repr__(self):
        return self.__str__()

class BinarySearchTree:
    
    def __init__(self):
        self.root=None
        self.count=0

    # 1. insert
    def __insert(self,root,node):
        if root is None:
            self.count+=1
            return node

        if node.key==root.key:
            root.value=node.value
        elif node.key<root.key:
            root.lchild=self.__insert(root.lchild,node)
        else:
            root.rchild=self.__insert(root.rchild,node)
    
        return root

    def insert(self,key,value=None):
        node=Node(key,value)
        self.root=self.__insert(self.root,node)


    # 2. search
    def __search(self,root,key):
        if root is None:
            return None

        if key==root.key:
            return root
        elif key<root.key:
            return self.__search(root.lchild,key)
        else:
            return self.__search(root.rchild,key)

    
    def search(self,key):
        return self.__search(self.root,key)

    def contain(self,key):
        return self.__search(self.root,key) is not None

    
    # 3. travel:

    # root,lchild,rchild
    def preOrder(self,root=None,result=None):
        root=root or self.root
        if root is None:
            return

        result=result or []
        result.append(root)

        if root.lchild is not None:
            self.preOrder(root.lchild,result)
        if root.rchild is not None:
            self.preOrder(root.rchild,result)

        return result

    # lchild,root,rchild => sorted sequence
    def __inOrder(self,node,result):
        if node is not None:
            self.__inOrder(node.lchild,result)
            result.append(node)
            self.__inOrder(node.rchild,result)

    def inOrder(self):
        result=[]
        self.__inOrder(self.root,result)
        return result

    # lchild,rchild,root
    def __postOrder(self,node,result):
        if node is not None:
            self.__postOrder(node.lchild,result)
            self.__postOrder(node.rchild,result)
            result.append(node)

    def postOrder(self):
        result=[]
        self.__postOrder(self.root,result)
        return result

    def levelOrder(self):
        result=[]
        q=[self.root]
        while q:
            node=q.pop(0)
            result.append(node)
            if node.lchild is not None:
                q.append(node.lchild)
            if node.rchild is not None:
                q.append(node.rchild)
        return result


    # 4. Min/Max

    def getMin(self,root=None):
        cur=root or self.root
        while cur and cur.lchild:
            cur=cur.lchild
        return cur

    def getMax(self,root=None):
        cur=root or self.root
        while cur and cur.rchild:
            cur=cur.rchild
        return cur

    # 5. remove

    def __removeMin(self,root):

        if root is None:
            return None,None

        pre=-1
        cur=root
        while cur and cur.lchild:
            pre=cur
            cur=cur.lchild

        if pre==-1:
            root=cur.rchild
        else:
            pre.lchild=cur.rchild

        cur.rchild=None
        self.count-=1

        return root,cur

    def removeMin(self):
        self.root,removedNode=self.__removeMin(self.root)
        print(self.root,removedNode)
        return removedNode


    def removeMax(self,root=None,pre=-1):
        # pre=-1
        # cur=self.root
        cur = root or self.root
        while cur and cur.rchild:
            pre=cur
            cur=cur.rchild
        
        if pre==-1:
            self.root=None
        else:
            pre.rchild=cur.lchild
        
        if cur is not None:
            cur.lchild,cur.rchild=None,None
            self.count-=1

        return cur

    '''
    查找节点 O(logN)
    
    删除节点只有一个孩子： 
       
       => 直接用孩子顶替
    
    删除节点有两个孩子：  
        
        => 选其右子树的最小值节点顶替（: <左子树，>右子树其他值）
            即选用其后驱节点：successor(node.rchild)
        
        => 或选其左子树的最大值节点顶替（: >左子树其他节点，<右子树）
            即选用其前驱节点：predecessor(node.lchild)
    '''
    def remove(self,key):
        pre=-1
        cur=self.root
        found=False
        while cur:
            if key==cur.key:
                found=True
                break
            pre=cur
            if key<cur.key:
                cur=cur.lchild
            else:
                cur=cur.rchild

        # print("found:%s, pre:%s, cur:%s" % (found,pre,cur))
        if not found:
            return

        if pre==-1:
            self.root=self.__getNextRoot(cur)
            return cur

        # print("pre : %s ( l:%s, r:%s )" % (pre,pre.lchild,pre.rchild))
        # print("cur : %s ( l:%s, r:%s )" % (cur,cur.lchild,cur.rchild))
        if pre.lchild is not None and pre.lchild.key==key:
            pre.lchild=self.__getNextRoot(cur)
            # print("pre get new lchild:",pre.lchild)
        elif pre.rchild is not None and pre.rchild.key==key:
            pre.rchild=self.__getNextRoot(cur)
            # print("pre get new rchild:",pre.rchild)

        cur.lchild,cur.rchild=None,None
        self.count-=1

        return cur


    def __getNextRoot(self,cur):
        if cur.lchild is None:
            return cur.rchild
        elif cur.rchild is None:
            return cur.lchild
        else:
            rchild_root,removed_node=self.__removeMin(cur.rchild)
            removed_node.lchild=cur.lchild
            removed_node.rchild=rchild_root
            return removed_node


    def predecessor(self,key):
        node=self.__search(self.root,key)

        # not exist
        if node is None:
            return None

        # max in left child
        if node.lchild is not None:
            return self.getMax(node.lchild)

        # on the root -> node path
        # 从根到此节点的路径上，找比key小的最大值
        return self.__predecessorFromAncestor(self.root,key)

    def __predecessorFromAncestor(self,root,key):
        if root.key==key:
            return None

        if key<root.key:
            return self.__predecessorFromAncestor(root.lchild,key)
        else:
            node=self.__predecessorFromAncestor(root.rchild,key) 
            return node or root


    def successor(self,key):
        node=self.__search(self.root,key)
        
        # not exist
        if node is None:
            return None

        # min in right child
        if node.rchild is not None:
            return self.getMax(node.rchild)

        # on the root -> node path
        # 从根到此节点的路径上，找比key大的最小值
        return self.__successorFromAncestor(self.root,key)

    # 在key的祖先中，查找比key大的最小值节点
    def __successorFromAncestor(self,root,key):
        if root.key==key:
            return None

        if key>root.key:
            return self.__successorFromAncestor(root.rchild,key)
        else:
            node=self.__successorFromAncestor(root.lchild,key) 
            return node or root


    def __floor(self,root,key):
        if root is None:
            return root

        if root.key==key:
            return root
        elif root.key>key:
            return self.__floor(root.lchild,key) 
        else:
            return self.__floor(root.rchild,key) or root

    def floor(self,key):
        return self.__floor(self.root,key)


    def __ceil(self,root,key):
        if root is None:
            return root
        
        if root.key==key:
            return root
        elif root.key<key:
            return self.__ceil(root.rchild,key)
        else:
            return self.__ceil(root.lchild,key) or root


    def ceil(self,key):
        return self.__ceil(self.root,key)



if __name__=='__main__':
    
    a=[20,30,10,5,15,2,8,12,17,14,13,25,3]
    
    tree=BinarySearchTree()

    # 1. insert
    for item in a:
        tree.insert(item)
    
    # travel
    print("inOrder    :",tree.inOrder())
    print("postOrder  :",tree.postOrder())
    print("preOrder   :",tree.preOrder())
    print("levelOrder :",tree.levelOrder())

    # search
    print("search 2 :",tree.search(2))
    print("search 9 :",tree.search(9))
    print("contain 15 :",tree.contain(15))
    print("contain 20 :",tree.contain(20))
    print("contain 9 :",tree.contain(9))

    # min/max
    print("min :",tree.getMin())
    print("max :",tree.getMax())

    # remove min/max
    print("remove min:",tree.removeMin())
    print("remove max:",tree.removeMax())

    print("inOrder :",tree.inOrder())
    print("levelOrder :",tree.levelOrder())

    # remove by key
    result=tree.remove(10)
    print("remove :",result)
    print("inOrder :",tree.inOrder())
    print("levelOrder :",tree.levelOrder())

    result=tree.remove(15)
    print("remove :",result)
    print("inOrder :",tree.inOrder())
    print("levelOrder :",tree.levelOrder())

    result=tree.remove(5)
    print("remove :",result)
    print("inOrder :",tree.inOrder())
    print("levelOrder :",tree.levelOrder())

    result=tree.remove(20)
    print("remove :",result)
    print("inOrder :",tree.inOrder())
    print("levelOrder :",tree.levelOrder())

    # floor,ceil
    print("floor 12:",tree.floor(12))
    print("ceil  12:",tree.ceil(12))

    print("floor 11:",tree.floor(11))
    print("ceil  11:",tree.ceil(11))

    # predecessor,successor
    print("predecessor 3:",tree.predecessor(3))
    print("successor  3:",tree.successor(3))

    print("predecessor 11:",tree.predecessor(11))
    print("successor  11:",tree.successor(11))

    print("predecessor 12:",tree.predecessor(12))
    print("successor  12:",tree.successor(12))

    print("predecessor 17:",tree.predecessor(17))
    print("successor  17:",tree.successor(17))






