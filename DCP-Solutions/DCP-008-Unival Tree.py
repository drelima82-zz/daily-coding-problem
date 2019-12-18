# Problem #8

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#             0
#      1             0
#               1            0
#           1       1


class Node():
    
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

    def __repr__(self):
            return str(self.data)
            
    def add_node(self, data):
        if self.data:
            if data > self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add_node(data)
            elif data <= self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add_node(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

def count_unival_trees(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left and root.data == root.right.data:
        return 1 + count_unival_trees(root.right)
    elif not root.right and root.data == root.left.data:
        return 1 + count_unival_trees(root.left)
    
    child_counts = count_unival_trees(root.left) + count_unival_trees(root.right)
    current_node_count = 0
    if root.data == root.left.data and root.data == root.left.data:
        current_node_count = 1

    return current_node_count + child_counts

##This solution does not works with Binary Tree because it uses balanced tree to split values
# It means that All 1´s go to the right and all 2´s go to left
#In this scenario is better using approach from GitHub, commented below, because it links the node manually.
#Despite "count_unival_trees" keep working in this approach
tree = Node(1)
tree.add_node(2)
tree.add_node(1)
tree.add_node(2)
tree.add_node(1)

tree.PrintTree()

assert count_unival_trees(None) == 0
assert count_unival_trees(tree) == 4
print("\n")
tree.add_node(1)
tree.PrintTree()
assert count_unival_trees(tree) == 5


###########################
# GITHUB SOLUTION
###########################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
    
#     def __repr__(self):
#         return str(self.data)

#     def aaa(self):
#         if self.left:
#             aaa(self.left)
#         print(self.data)
#         if self.right:
#             aaa(self.right)

# def count_unival_trees(root):
#     if not root:
#         return 0
#     elif not root.left and not root.right:
#         return 1
#     elif not root.left and root.data == root.right.data:
#         return 1 + count_unival_trees(root.right)
#     elif not root.right and root.data == root.left.data:
#         return 1 + count_unival_trees(root.left)
    
#     child_counts = count_unival_trees(root.left) + count_unival_trees(root.right)
#     current_node_count = 0
#     if root.data == root.left.data and root.data == root.left.data:
#         current_node_count = 1

#     return current_node_count + child_counts


# node_a = Node('0')
# node_b = Node('1')
# node_c = Node('0')
# node_d = Node('1')
# node_e = Node('0')
# node_f = Node('1')
# node_g = Node('1')
# node_a.left = node_b
# node_a.right = node_c
# node_c.left = node_d
# node_c.right = node_e
# node_d.left = node_f
# node_d.right = node_g

# assert count_unival_trees(None) == 0
# assert count_unival_trees(node_a) == 5
# assert count_unival_trees(node_c) == 4
# assert count_unival_trees(node_g) == 1
# assert count_unival_trees(node_d) == 3