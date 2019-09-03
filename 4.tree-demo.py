
# Tree 

class TreeNode:
    def __init__(self,elem=None,lchild=None,rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild

class Tree:
    def __init__(self,root=None):
        self.root=root

    def append(self,elem):
        node=TreeNode(elem)
        q=[self.root]
        while q:
            cur=q.pop(0)
            if cur is None:
                self.root=node
                return node
            elif cur.lchild is None:
                cur.lchild=node
                return node
            elif cur.rchild is None:
                cur.rchild=node
                return node
            else:
                q.extend([cur.lchild,cur.rchild])

    def extend(self,elems):
        for i in elems:
            self.append(i)

    # 广度搜索遍历：队列(先进先出),层级遍历
    def breadth_travel(self):
        result=[]
        q=[self.root]
        while q:
            cur=q.pop(0)        # 头部出
            if cur is None:
                break
            #print(cur.elem,end=" ")
            result.append(cur.elem)

            if cur.lchild is not None:
                q.append(cur.lchild)
            if cur.rchild is not None:
                q.append(cur.rchild)

        return result
    
    
    # 深度搜索遍历：堆栈(先进后出) = 先序遍历
    def deepth_travel(self):
        result=[]
        q=[self.root]
        while q:
            cur=q.pop()        # 尾部出
            if cur is None:
                break;
            
            #print(cur.elem,end=" ")
            result.append(cur.elem)
            
            if cur.rchild is not None:
                q.append(cur.rchild)
            if cur.lchild is not None:
                q.append(cur.lchild)

        return result

   
    # 先序：根 -> 左 -> 右
    def preorder_travel(self,node=None,result=[]):
        if node is None and self.root is not None:
            node=self.root

        #print(node.elem,end=" ")
        result.append(node.elem)
        
        if node.lchild is not None:
            self.preorder_travel(node.lchild)

        if node.rchild is not None:
            self.preorder_travel(node.rchild)

        return result

    # 中序：左 -> 根 -> 右
    def inorder_travel(self,node=None,result=[]):
        if node is None and self.root is not None:
            node=self.root

        if node.lchild is not None:
            self.inorder_travel(node.lchild)
        
        #print(node.elem,end=" ")
        result.append(node.elem)
        
        if node.rchild is not None:
            self.inorder_travel(node.rchild)

        return result


    # 后序：左 -> 右 -> 根
    def postorder_travel(self,node=None,result=[]):
        if node is None and self.root is not None:
            node=self.root

        if node.lchild is not None:
            self.postorder_travel(node.lchild)
        if node.rchild is not None:
            self.postorder_travel(node.rchild)
        
        #print(node.elem,end=" ")
        result.append(node.elem)
        return result


# Test

def test_tree():
    print("Test Tree:")
    t=Tree()
    t.extend(['A','B','C','D','E','F'])
    print(r'''
            A
        /        \
       B          C
     /   \       / 
    D     E    F  
    ''')

    print("广度（＝层级）:", t.breadth_travel())
    print("深度（＝先序）:", t.deepth_travel())

    print("先序(＝根左右):", t.preorder_travel())
    print("中序(＝左根右):", t.inorder_travel())
    print("后序(＝左右根):", t.postorder_travel())




if __name__ == '__main__':

    test_tree()
    print("***"*10)



