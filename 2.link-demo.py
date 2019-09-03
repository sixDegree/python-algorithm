
# Link

class LinkNode:
    def __init__(self,elem=None):
        self.elem=elem
        self.next=None

    def __str__(self):
        return self.elem

class SingleLinkList:
    def __init__(self,node=None):
        self.head=node
        self.count=0
    
    def append(self,item):
        node=LinkNode(item)
        if self.head is None:
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node
        
        self.count+=1
        return node

    def pop(self,pos=-1):
        
        if pos<0:
            pos+=self.count

        # ^         pos=0,cnt=0 return None

        # A
        # 0
        # ^         pos=0,cnt=1 => head=None,return A

        # A B C D
        # 0 1 2 3
        # ^         pos=0,cnt=4 => head=B,return A

        # A B C D
        # 0 1 2 3
        #     ^     pos=2,cnt=4 => A,B,D, return C

        # A B C D
        # 0 1 2 3
        #       ^   pos=3,cnt=4 => A,B,C, return D

        if pos>=self.count:
            return

        cur,pre,i=self.head,None,0
        while cur.next!=None and i<pos:
            pre=cur 
            cur=cur.next
            i+=1
        if pre is None:
            self.head=cur.next
        else:
            pre.next=cur.next

        self.count-=1
        return cur


    def insert(self,item,pos=0):

        if pos<0:
            pos+=self.count

        # ^         pos=0,cnt=0,head=None => head=H

        # A
        # 0
        # ^         pos=0,cnt=1,head=A => head=H,A

        # A B C D
        # 0 1 2 3
        # ^         pos=0,cnt=4,head=A => head=H,A,B,C,D

        # A B C D
        # 0 1 2 3
        #     ^     pos=2,cnt=4,head=A => A,B,H,C,D

        # A B C D
        # 0 1 2 3
        #       ^   pos=3,cnt=4,head=A => A,B,C,H,D

        # A B C D
        # 0 1 2 3
        #         ^ pos=4,cnt=4,head=A => A,B,C,D,H


        if pos>self.count:
            return
        # if pos==self.count:
        #     return self.append(item)

        node=LinkNode(item)
        if self.head is None:
            self.head=node
        else:
            cur,pre,i=self.head,None,0
            while cur.next!=None and i<pos:
                pre=cur
                cur=cur.next
                i+=1
            
            if pre is None:
                self.head=node
                node.next=cur
            elif i<pos:
                cur.next=node
            else:
                pre.next=node
                node.next=cur
        
        self.count+=1
        return node
       
        
    def remove(self,item):
        cur,pre=self.head,None
        while cur!=None:
            if cur.elem==item:
                if pre is None:
                    self.head=cur.next
                else:
                    pre.next=cur.next
                self.count-=1
                return cur
            pre=cur
            cur=cur.next
        

    def travel(self):
        result=[]
        cur=self.head
        while cur!=None:
            # print(cur.item,end=" ")
            result.append(cur.elem)
            cur=cur.next
        return result

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def clear(self):
        self.head=None
        self.count=0


def test_singleLinkList():
    print("Test SingleLinkList:")
    l=SingleLinkList()

    print("is_empty:",l.is_empty())
    print("append:",l.append('A'))
    print("append:",l.append('B'))
    print("append:",l.append('C'))
    print("append:",l.append('D'))
    print("travel:",l.travel())
    print("size:",l.size())
    print("---"*10)

    print("insert pos 0(default):",l.insert('H',0))
    print("insert pos 2:",l.insert('I',2))
    print("insert pos -1:",l.insert('J',-1))
    print("travel:",l.travel())
    print("size:",l.size())
    print("---"*10)

    print("pop pos 0:",l.pop(0))
    print("pop pos 2:",l.pop(2))
    print("pop pos -1(default):",l.pop(-1))
    print("travel:",l.travel())
    print("size:",l.size())
    print("---"*10)

    print("remove:",l.remove('B'))
    print("remove:",l.remove('C'))
    print("remove:",l.remove('A'))
    print("travel:",l.travel())
    print("size:",l.size())
    print("is_empty:",l.is_empty())
    print("---"*10)

    print("clear...")
    l.clear()
    print("is_empty:",l.is_empty())
    print("size:",l.size())

    print("insert pos 0(default):",l.insert('A',0))
    print("insert pos 0(default):",l.insert('B',0))
    print("travel:",l.travel())
    print("insert pos 1:",l.insert('C',1))
    print("travel:",l.travel())
    print("insert pos 2:",l.insert('D',2))
    print("travel:",l.travel())
    print("insert pos 4:",l.insert('E',4))
    print("travel:",l.travel())
    print("size:",l.size())

    print("pop pos 0:",l.pop(0))
    print("pop pos 0:",l.pop(0))
    print("pop pos 0:",l.pop(0))
    print("pop pos 0:",l.pop(0))
    print("pop pos 0:",l.pop(0))
    print("pop pos 0:",l.pop(0))
    print("travel:",l.travel())
    print("size:",l.size())


if __name__ == '__main__':
    
    test_singleLinkList()
    print("***"*10)


