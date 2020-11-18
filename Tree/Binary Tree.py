class Node():
    def __init__(self,val):
        self.value = val;
        self.right = None;
        self.left = None;

class Tree():
    def __init__(self):
        self.root : Node = None;


    def remove(self,value):

        replace: Node = None;
        prev: Node = None;
        delete : Node = None;
        temp :Node = None;

        if self.root!=None:
            #root is the node to delete
            if self.root.value==value:


                if self.root.right!=None:
                    if  self.root.left==None:
                        self.root=self.root.right;
                    else:
                        if self.root.right.left==None:
                            self.root=self.root.right;
                        else:
                            prev = self.root.right;
                            while(prev.left.left != None):
                                prev = prev.left;
                            replace = prev.left;

                            #Action to Delete Root
                            replace.right = prev.left;
                            replace.right = self.root.right;
                            replace.left= self.root.left;
                            prev.left=None;
                            self.root=replace;

                else:
                    self.root=self.root.left;
            else:
                temp = self.root;
                while(True):
                    if temp.value < value:
                        if temp.right==None:
                            return "Not Found";
                        elif temp.right.value==value:
                            prev = temp;
                            delete = temp.right;

                            if delete.right.left==None:
                                prev.right = delete.right;
                                delete.right.left=delete.left;
                                delete.right =None;
                                delete.left=None;
                                break;
                            elif delete.right==None:
                                prev.right = delete.left;
                                delete=None;
                                break;
                            elif delete.left==None:
                                prev.right = delete.right;
                                delete=None;
                                break;

                            elif delete.right.left!=None:
                                temp = delete.right;
                                while(temp.left.left!=None):
                                    temp=temp.left;

                                replace = temp.left;
                                prev.right=replace;
                                replace.right=delete.right;
                                replace.left=delete.left;
                                temp.left=None;
                                break;
                        else:
                            temp = temp.right;
                    else:
                        if temp.left==None:
                            return "Not Found";
                        if temp.left.value==value:
                            prev = temp;
                            delete = temp.left;
                            if delete.left==None:
                                prev.left=delete.right;
                                break;

                            elif delete.right==None:
                                prev.left=delete.left;
                                break;
                            elif delete.right.left==None:
                                delete.right.left = delete.left;
                                prev.left = delete.right;
                                delete.left=None;
                                delete.right=Node;
                                break;

                            else:
                                temp = delete.right;
                                while(temp.left.left!=None):
                                    temp = temp.left;
                                replace = temp.left;
                                replace.right = delete.right;
                                replace.left = delete.left;
                                temp.left=None;
                                break;
                        temp = temp.left;
        else:
            print("Empty");


    def insert(self, n):
        if self.root == None:
            self.root= Node(n);
        else:
            temp = self.root;
            new = Node(n)
            while(True):
                if n < temp.value:
                    if temp.left==None:
                        temp.left=new;
                        break;
                    temp = temp.left;
                else:
                    if temp.right==None:
                        temp.right=new;
                        break;
                    else:
                        temp=temp.right;

    def TravelPre(self,temp:Node):
        if temp == None:
            return;
        print(temp.value)
        self.TravelPre(temp.left)
        self.TravelPre(temp.right)


    def TravelIn(self,temp:Node):
        if temp==None:
            return;
        self.TravelIn(temp.left)
        print(temp.value);
        self.TravelIn(temp.right);

    def TravelPost(self,temp:Node):
        if temp==None:
            return;
        self.TravelPost(temp.left)
        self.TravelPost(temp.right)
        print(temp.value)




    def Serach(self,n):
        if self.root:
            temp=self.root;
            while(temp):
                if temp.value == n:
                    print( "Found");
                    break;
                elif temp.value > n:
                    temp = temp.left;
                else:
                    temp=temp.right;
            if temp==None:
                print("Not Found");

tree = Tree();
tree.insert(20);
tree.insert(10);
tree.insert(7);
tree.insert(13);
tree.insert(5);
tree.insert(8)
tree.insert(30)
tree.insert(25)
tree.insert(35)

