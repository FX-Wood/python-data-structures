from TreeNode import TreeNode

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def insert(self, data, node=None):
        if not node:
            node = TreeNode(data)
        # if no root
        if not self.root:
            # make new node at root
            self.root = node
        # if root exists
        else:
        # recurse
            node = self.root
            # if left is empty and our value is still lowest,
            # we have the lowest value.
            if data < node.data and node.left == None:
                    node.left = TreeNode(data)
            # if the data at our current node is lower
            elif data < node.data:
                # recurse left
                node.left = self.insert(data, node)
            # if the data at our current node is higher and there is no right,
            # we have the highest value, make a node.
            elif data > node.data and node.right == None:
                # recurse down the right tree
                node.right = TreeNode(data)
            # if data is higher than the current node,
            elif data > node.data:
                node.right = self.insert(data, node)
            return node

    def traverse(self, type_number):
        output = []
        if type_number == 'in_order':
            self.in_order(output)
        if type_number == 'pre_order':
            self.pre_order(output)
        if type_number == 'post_order':
            self.post_order(output)
        return output


    def in_order(self, output, node=None):
        # left, root, right
        if not node:
            node = self.root
        if node:
            if node.left:
                self.in_order(output, node.left)
            output.append(node.data)
            if node.right:
                self.in_order(output, node.right)

    def pre_order(self, output, node=None):
        # root, left, right
        if not node:
            node = self.root
        if node:
            output.append(node.data)
            if node.left:
                self.pre_order(output, node.left)
            if node.right:
                self.pre_order(output, node.right)

    def post_order(self, output, node=None):
        # left, right, root
        if not node:
            node = self.root
        if node:
            if node.left:
                self.post_order(output, node)
            if node.right:
                self.post_order(output, node)
            output.append(node.data)