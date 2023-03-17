
class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    def insert(self, val):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        elif val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)
            return
        else:
            if self.right:
                self.right.insert(val)
                return
            self.right = Node(val)
    def search(self, item):
        if self.val is None:
            return None
        if item == self.val:
            return self.val
        if item < self.val:
            if self.left is None:
                return None
            return self.left.search(item)
        if self.right is None:
            return None
        return self.right.search(item)
    def __in_order(self, result):
        if self.left is not None:
            result = self.left.__in_order(result)
        
        result.append(self.val)

        if self.right is not None:
            result = self.right.__in_order(result)
        return result
    def nodes(self):
        
        result = []
        result = self.__in_order(result)
        
        return result
   

