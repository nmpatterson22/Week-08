'''
This file implements the Node and BinaryTree classes.
These two classes are the building blocks for the BST, AVLTree, and
Heap data structures.
It is crucial to get these implemented correctly in order to be able to
implement the other data structures.
'''


class Node():
    '''
    You do not have to implement anything within this class.
    Given a node t, you can visualize the node by running str(t) in the
    python interpreter.
    This is a key method to perform debugging,
    so you should get familiar with how to visualize these strings.
    '''

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left    # NOTE: left should always be a Node
        self.right = right  # NOTE: right should always be a Node

    def __str__(self):
        ret = '('
        ret += str(self.value)
        ret += ' - '
        if self.left:
            ret += str(self.left)
            ret += ' '
        ret += '- '
        if self.right:
            ret += str(self.right)
            ret += ' '
        ret += ')'
        return ret


class BinaryTree():
    '''
    This class is relatively useless by itself,
    but it is the superclass for the BST, AVLTree, and Heap classes,
    and it provides important helper functions for these classes.
    If you don't implement all of the functions in this class correctly,
    it will be impossible to implement those other classes.
    '''

    def __init__(self, root=None):
        '''
        Construct a BinaryTree, possibly with a single element in it.
        Note that for an ordinary BinaryTree, we cannot insert more than one
        element in the constructor,
        but for the BST (and other tree types) we can.
        '''
        if root:
            self.root = Node(root)
        else:
            self.root = None

    def __str__(self):
        '''
        We can visualize a tree by visualizing its root node.
        '''
        return str(self.root)

    def print_tree(self, traversal_type):
        '''
        There are three primary types of tree traversals: preorder,
        inorder, and postorder.
        All three of these traversals are implemented for you as a
        reference on how to write recursive functions on
        recursive data structures.
        '''
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        else:
            raise ValueError(+ str(traversal_type) + 'is not supported.')

    def preorder_print(self, start, traversal):
        '''
        Prints the nodes using a preorder traversal.
        '''
        if start:
            traversal += str(start.value) + '-'
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        '''
        Prints the nodes using a inorder traversal.
        '''
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + '-'
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        '''
        Prints the nodes using a postorder traversal.
        '''
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + '-'
        return traversal

    def to_list(self, traversal_type):

        if traversal_type == 'preorder':
            return self.preorder(self.root, [])
        elif traversal_type == 'inorder':
            return self.inorder(self.root, [])
        elif traversal_type == 'postorder':
            return self.postrder(self.root, [])
        else:
            raise ValueError(str(traversal_type) + 'is no good!')

    def preorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions above.
        '''
        if start:
            traversal.append(start.value)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        '''
        FIXME:
        Implement this function by modifying the _print functions
        above.
        '''
        # this set of function moves the append "across" the tree
        if start:
            traversal = self.preorder(start.left, traversal)
            traversal.append(start.value)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start:
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def __len__(self):
        '''
        Returns the number of elements contained in the tree.
        Recall that `tree.__len__()` will desugar to `size(len)`.
        '''
        return BinaryTree.__len__helper(self.root)

    @staticmethod
    def __len__helper(node):
        '''
        FIXME:
        Implement this function.

        HINT:
        The pseudocode is:
        add 1 for the current node;
        if a left child exists, add the result of
        __len__helper on the left child;
        if a right child exists, add the result of
        __len__helper on the right child;
        return the sum of these three steps
        '''
        if node:
            # Pseudo: If result 1 (left) add result of hekper function + 1 to
            l_child = BinaryTree.__len__helpter(node.left) + 1
            r_child = BinaryTree.__len__helper(node.right)
            return l_child + r_child
        else:
            return 0

    def height(self):
        '''
        Returns the height of the tree.
        Recall that the height is the maximum length from the
        root to a leaf node.

        FIXME:
        Implement this function.

        HINT:
        See how the __len__ method calls its helper staticmethod.
        '''
        return BinaryTree._heigh(self.root)

    @staticmethod
    def _height(node):
        '''
        FIXME:
        Implement this function.

        HINT:
        The pseudocode is:
        if a left child exists, calculate the _height of the left child;
        if a right child exists, calculate the _height of the right child;
        return 1 (for the current node) plus the max of the left and
        right _heights calculated above
        '''
        if node is None:
            return -1
        left_height = BinaryTree._heigh(node.left)
        right_height = BinaryTree._height(node.right)
        # Return the calcualted hieghs of left_height + right_height

        return 1 + max(left_height + right_height)
