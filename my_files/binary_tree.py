class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTee:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        msg = "{} has been inserted.".format(data)
        if self.root == None:
            self.root = new_node
            return print(msg)
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    #Go left
                    if not current_node.left:
                        current_node.left = new_node
                        return print(msg)
                    else:
                        current_node = current_node.left
                else:
                    #Go right
                    if not current_node.right:
                        current_node.right = new_node
                        return print(msg)
                    else:
                        current_node = current_node.right
    
    def lookup(self, data):
        pt = self.root
        while True:
            if not pt:
                print("{} is not in the true.".format(data))
                return False
            elif pt.data == data:
                print("{} is in the tree!".format(data))
                return True
            elif data < pt.data:
                pt = pt.left
            elif data > pt.data:
                pt = pt.right
    
    def remove(self, data):
        succ = "{} removed!".format(data)
        pt = self.root
        parent = pt
        while True:
            if not pt:
                return print("{} is not in the tree.".format(data))
            elif pt.data == data:
                #Case 1: No children
                if not pt.left and not pt.right:
                    if data == parent.left.data:
                        parent.left = None
                        return print(succ)
                    elif data == parent.right.data:
                        parent.right = None
                        return print(succ)
                
                #Case 2: One child
                elif not (pt.left and pt.right):
                    if data == parent.right.data:
                        parent.right = pt.right if pt.right != None else pt.left
                        return print(succ)
                    elif data == parent.left.data:
                        parent.left = pt.right if pt.right != None else pt.left
                        return print(succ)
                
                #Case 3: Two children
                else:
                    #Go to right child of node to be removed
                    sub_pt = pt.right
                    while True:
                        #find the left-most child in subtree
                        if sub_pt.left == None:
                            if data == parent.right.data:
                                rhs_smallest = sub_pt
                                self.remove(sub_pt.data)
                                parent.right.data = rhs_smallest.data
                                return print(succ)

                            elif data == parent.left.data:
                                rhs_smallest = sub_pt
                                self.remove(sub_pt.data)
                                parent.left.data = rhs_smallest.data
                                return print(succ)
                        sub_pt = sub_pt.left

            elif data < pt.data:
                parent = pt
                pt = pt.left
            elif data > pt.data:
                parent = pt
                pt = pt.right

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
#Inorder Traversal (We get sorted order of elements in tree)

    def printt(self,curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)

bt = BinaryTee()

bt.insert(15)
bt.insert(10)
bt.insert(60)
bt.insert(7)
bt.insert(12)
bt.insert(30)
bt.insert(69)
bt.insert(2)
bt.insert(8)
bt.insert(11)
bt.insert(14)
bt.insert(20)
bt.insert(40)
bt.insert(65)
bt.insert(1)
bt.insert(4)
bt.insert(13)
bt.insert(16)
bt.insert(24)
bt.insert(23)
bt.insert(26)
bt.insert(22)
bt.insert(25)
bt.insert(27)
bt.remove(69)
bt.remove(24)

print("\n---TREE---")
bt.print_tree()
            

    

