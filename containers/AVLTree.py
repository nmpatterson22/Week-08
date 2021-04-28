'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than
the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class
    declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        self.root = None
        if xs:
            self.insert_list(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all nodes have a
        balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node is None:
            return ret
        if not AVLTree._isbst_satisifed(node)
            return False
        if AVLTree._balance_factor(node) in [-1, 0, 1]:
            first = AVLTree.is_avl_satisfied(node.left)
            second = AVLTree.is_avl_satisfied(node.right)
        return ret and first and second
        else:
            return False

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is
        fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        if node is None or node.right is None:
            return node
            root_1 = Node(node.value)
            root_1.left = node.left
            root_1.right = node.right.left

            root_2 = Node(node.right.value)
            root_2.right = node.right.right
            root_2.left = root_1
        else:
            root_2 = node
        return root_2

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is
        fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        # same pattern as above but "flipped" for left nodes
        if node is None or node.left is None:
            return node
            root_1 = Node(node.value)
            root_1.right = node.right
            root_1.left = node.left.right

            root_2 = Node(node.left.value)
            root_2.left = node.left.left
            root_2.left = root_1
        else:
            root_1 = node
        return root_1

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to
        insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert
        function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if not self.root:
            self.root = Node(value)
        if value == self.root.value:
            return
        else:
            self._insert(value, self.root)
            if not self._is_avl_satisfied():
                self.root = self.rebalance(self.root)
            if not self.is_avl_satisfied():
                self.root = self.rebalance(self.root)

    @staticmethod
    def _insert(node, value):
        if node.value < value:
            if node.right:
                AVLTree._insert(node.right, value)
            else:
                node.right = Node(value)
        elif node.value > value:
            if node.left:
                AVLTree._insert(node.left, value)
            else:
                node.left = Node(value)
        if AVLTree._is_avl_satisfied(node):
            pass
        else:
            node.left = AVLTree._rebalance(node.left)
            node.right = AVLTree._rebalance(node.right)
            node = AVLTree._rebalance(node)
        return node

    def rebalance(self, begin):
        '''new function that takes parameters self and inception begin to
        help _rebalance function'''
        if begin is None:
            return
        if self._balance_factor(begin) in [-2, 2]:
            begin = self._rebalance(begin)
        else:
            begin.right = self.reabalance(begin.right)
            begin.left = self.rebalance(begin.right)
        return begin

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if node is None:
            return
        balance = AVLTree._balance_factor(node)
        if balance < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                node = AVLTree._left_rotate(node)
            else:
                node = AVLTree._left_rotate(node)
        elif balance > 0:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
                node = AVLTree._right_rotate(node)
            else:
                node = AVLTree._right_rotate(node)
            return node
