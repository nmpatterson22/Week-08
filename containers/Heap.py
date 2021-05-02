from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if xs is not None:
            for x in xs:
                self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string
        that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap will
        have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete
        functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        place_left = True
        place_right = True
        if node is None:
            return True
        if node.left:
            if node.value > node.left.value:
                return False
            else:
                place_left = Heap._is_heap_satisfied(node.left)
        if node.right:
            if node.value > node.right.value:
                return False
            else:
                place_right = Heap._is_heap_satisfied(node.right)
        return place_left and place_right

    def insert(self, value):
        '''
        Inserts value into the heap.

        FIXME:
        Implement this function.

        HINT:
        The pseudo code is
        1. Find the next position in the tree using the binary representation
        of
        the total number of nodes
        1. You will have to explicitly store the size of your heap in a
        variable (rather than compute it) to maintain the O(log n) runtime
        1. Recursively swap value with its parent until the
        heap property is satisfied

        HINT:
        Create a @staticmethod helper function,
        following the same pattern used in the BST and AVLTree
        insert functions.
        '''
# Storing positional argument
        if self.root:
            new_count = self.__len__()
            next = "{0:b}".format(new_count + 1)[1:]
            self.root = Heap._insert(value, self.root, next)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value, next):
        if next[0] == '0':
            if not node.left:
                node.left = Node(value)
            else:
                node.left = Heap._insert(node.left, value, next[1:])

        if next[0] == '1':
            if not node.right:
                node.right = Node(value)
            else:
                node.right = Heap._insert(node.right, value, next[1:])

        if next[0] == '0':
            if node.left.value < node.value:
                temp_value = node.value
                node.value = node.left.value
                node.left.value = temp_value
                return node
            else:
                return node

        if next[0] == '1':
            if node.right.value < node.value:
                temp_value = node.value
                node.value = node.right.value
                node.right.value = temp_value
                return node
            else:
                return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        return self.root.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.

        HINT:
        The pseudocode is
        1. remove the bottom right node from the tree
        2. replace the root node with what was formerly the bottom right
        3. "trickle down" the root node: recursively swap it
        with its largest child until the heap property is satisfied

        HINT:
        I created two @staticmethod helper functions:
        _remove_bottom_right and _trickle.
        It's possible to do it with only a single helper (or no helper at all
        but I personally found dividing up the code into two made the most
        sense.
        '''
        if not self.root:
            pass
        else:
            new_count = self.__len__()
            next = "{0:b}".format(new_count)[1:]
            last, self.root = Heap._remove_bottom_right(
                self.root, next)
            if self.root:
                self.root.value = last
            print(str(self.root))
            self.root = Heap._trickle(self.root)

    @staticmethod
    def _remove_bottom_right(node, next):
        new_removed_value = ""
        if len(next) == 0:
            return None, None
        if next[0] == '0':
            if len(next) == 1:
                new_removed_value = node.left.value
                node.left = None
            else:
                new_removed_value, node.left = Heap._remove_bottom_right(
                    node.left, next[1:])

        if next[0] == '1':
            if len(next) == 1:
                new_removed_value = node.right
                node.right = None
            else:
                new_removed_value, node.right = Heap._remove_bottom_right(
                    node.right, next[1:])
        print(new_removed_value, str(node))
        return new_removed_value, node

    @staticmethod
    def _trickle(node):
        if Heap._is_heap_satisfied(node):
            pass
        else:
            if not node.left and node.right:
                temp_value = node.value
                node.value = node.right.value
                node.right.value = temp_value
                node.right = Heap._trickle(node.right)
            elif node.left and node.right:
                temp_value = node.value
                node.value = node.left.value
                node.left.value = temp_value
                node.left = Heap._trickle(node.left)
            elif node.left.value >= node.right.value:
                temp_value = node.value
                node.value = node.right.value
                node.right.value = temp_value
                node.right = Heap._trickle(node.right)
            elif node.left.value <= node.right.value:
                temp_value = node.value
                node.value = node.left.value
                node.left.value = temp_value
                node.left = Heap._trickle(node.left)
            else:
                pass
            return node
