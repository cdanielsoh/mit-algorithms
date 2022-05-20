class BinaryNode:
    def __init__(self, value) -> None:
        self.parent : BinaryNode = None
        self.left : BinaryNode = None
        self.right : BinaryNode = None
        self.value = value
    
    def subtree_iter(self):
        if self.left: yield from self.left.subtree_iter()
        yield self
        if self.right: yield from self.right.subtree_iter()
    
    def subtree_first(self):
        if self.left: return self.left.subtree_first()
        else: return self

    def subtree_last(self):
        if self.right: return self.right.subtree_last()
        else: return self

    def successor(self):
        if self.right: return self.right.subtree_first()
        while self.parent and (self is self.parent.right):
            self = self.parent
        return self.parent

    def predecessor(self):
        if self.left: return self.left.subtree_last()
        while self.parent and (self is self.parent.left):
            self = self.parent
        return self.parent

    def subtree_insert_before(self, node):
        if self.left:
            self = self.left.subtree_last()
            self.right, node.parent = node, self
        else:
            self.left, node.parent = node, self
        # self.maintain()

    def subtree_insert_after(self, node):
        if self.right:
            self = self.right.subtree_first()
            self.left, node.parent = node, self
        else:
            self.right, node.parent = node, self
        # self.maintain()

    def subtree_delete(self):
        if self.left or self.right:
            if self.left: inter_node = self.predecessor()
            else: inter_node = self.successor()
            self.value, inter_node.value = inter_node.value, self.value
            return inter_node.subtree_delete()
        if self.parent:
            if self.parent.left is self: self.parent.left = None
            else: self.parent.right = None
            # self.parent.maintain()
        return self

class BinaryTree:
    def __init__(self, Node_Type = BinaryNode) -> None:
        self.root = None
        self.size = 0
        self.Node_Type = Node_Type
    
    def __len__(self): return self.size
    
    def __iter__(self):
        if self.root:
            for node in self.root.subtree_iter():
                yield node.value

    def build(self, iterable):
        iter_list = [x for x in iterable]
        def build_subtree(iter_list, i, j):
            mid_val = (i + j) // 2
            root = self.Node_Type(iter_list[mid_val])
            if i < mid_val:
                root.left = build_subtree(iter_list, i, mid_val - 1)
                root.left.parent = root
            if mid_val < j:
                root.right = build_subtree(iter_list, mid_val + 1, j)
                root.right.parent = root
            return root
        self.root = build_subtree(iter_list, 0, len(iter_list) - 1)

    def tree_iter(self):
        node = self.root.subtree_first()
        while node:
            yield node
            node = node.successor()

class BST_Node(BinaryNode):
    def subtree_find(self, key):
        if self.value > key:
            if self.left: return self.left.subtree_find(key)
        if self.value < key:
            if self.right: return self.right.subtree_find(key)
        else: return self
        return None

    def subtree_find_next(self, key):
        if self.value > key:
            if self.left: return self.left.subtree_find(key)
        if self.value < key:
            if self.right: return self.right.subtree_find(key)
        else: return self
        return 

def main():
    A = range(100)
    btree = BinaryTree()
    btree.build(A)
    print([a for a in btree])
    print(len(btree))
    print(btree.root.value)
    btree.root.subtree_delete()
    print(btree.root.value)
    print([a for a in btree])
    print(len(btree))

if __name__ == '__main__':
    main()
