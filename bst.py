class Tree:

    def __init__(self,key=None,value=None):
        self.key=key
        self.left=None
        self.right=None
    
    def insert(self,key,value):
        if self.key==key:
            self.value=value
            return
        if self.key==None:
            self.key=key
            self.value=value
            return
        if key<self.key:
            if self.left==None:
                self.left=Tree()
            self.left.insert(key,value)
            return
        if self.right==None:
            self.right=Tree()
        self.right.insert(key,value)
    
    def search(self,key):
        if self.key==None:
            return None
        if self.key==key:
            return self
        if key<self.key:
            if self.left==None:
                return None
            return self.left.search(key)
        if key>self.key:
            if self.right==None:
                return None
            return self.right.search(key)

    def max(self):
        if self.right==None:
            return self
        return self.max(self.right)
    
    def min(self):
        if self.left==None:
            return self
        return self.min(self.left)

    def __getitem__(self, key):
        return self.search(key).value
    
    def __setitem__(self, key, value):
        self.insert(key,value)
    
    def __contains__(self,key):
        return self.search(key)!=None

    def delete(self, key):
        """ delete the node with the given key and return the 
        root node of the tree """

        if self.key == key:
    
            if self.right and self.left: 

                [psucc, succ] = self.right._findMin(self)

                # splice out the successor
                # (we need the parent to do this) 

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                # reset the left and right children of the successor

                succ.left = self.left
                succ.right = self.right

                return succ                

            else:
                # "easier" case
                if self.left:
                    return self.left    # promote the left subtree
                else:
                    return self.right   # promote the right subtree 
        else:
            if self.key > key:          # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                # else the key is not in the tree 

            else:                       # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)

        return self

    def _findMin(self, parent):
        """ return the minimum node in the current tree and its parent """

        # we use an ugly trick: the parent node is passed in as an argument
        # so that eventually when the leftmost child is reached, the 
        # call can return both the parent to the successor and the successor

        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]

    def __delitem__(self, key) -> None:
        x=self.delete(key)
        self.key=x.key
        self.value=x.value
        self.left=x.left
        self.right=x.right