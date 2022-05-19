from __future__ import annotations

from typing import Optional, Any, Callable


class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every node, its value is >= all items stored in its left
    subtree, and <= all items stored in its right subtree.
    """
    # === Private Attributes ===
    # The item stored at the root of the tree, or None if the tree is empty.
    _root: Optional[Any]
    # The left subtree, or None if the tree is empty.
    _left: Optional[BinarySearchTree]
    # The right subtree, or None if the tree is empty.
    _right: Optional[BinarySearchTree]

    def __init__(self, root: Optional[Any]) -> None:
        """Initialize a new BST containing only the given root value.

        If <root> is None, initialize an empty BST.
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)  # self._left is an empty BST
            self._right = BinarySearchTree(None)  # self._right is an empty BST

    def __str__(self) -> str:
        """Return a string representation of this BST.

        This string uses indentation to show depth.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this BST.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            answer = depth * '  ' + str(self._root) + '\n'
            answer += self._left._str_indented(depth + 1)
            answer += self._right._str_indented(depth + 1)
            return answer

    def is_empty(self) -> bool:
        """Return whether this BST is empty.
        """
        return self._root is None

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this BST.
        """
        if self.is_empty():
            return False
        elif item == self._root:
            return True
        elif item < self._root:
            return item in self._left  # or, self._left.__contains__(item)
        else:
            return item in self._right  # or, self._right.__contains__(item)

    def delete(self, item: Any) -> None:
        """Remove *one* occurrence of <item> from this BST.

        Do nothing if <item> is not in the BST.
        """
        if self.is_empty():
            pass
        elif self._root == item:
            self.delete_root()
        elif item < self._root:
            self._left.delete(item)
        else:
            self._right.delete(item)

    def delete_root(self) -> None:
        if self._left.is_empty() and self._right.is_empty():
            self._root = None
            self._left = None
            self._right = None
        elif self._left.is_empty():
            # "Promote" the right subtree.
            self._root, self._left, self._right = \
                self._right._root, self._right._left, self._right._right
        elif self._right.is_empty():
            # "Promote" the left subtree.
            self._root, self._left, self._right = \
                self._left._root, self._left._left, self._left._right
        else:
            self._root = self._left.extract_max()

    def extract_max(self) -> object:
        """Remove and return the maximum item stored in this tree.

        Precondition: this tree is *non-empty*.
        """
        if self._right.is_empty():
            max_item = self._root
            # Once again, "Promote" the left subtree.
            self._root, self._left, self._right = \
                self._left._root, self._left._left, self._left._right
            return max_item
        else:
            return self._right.extract_max()

    def items(self) -> list:
        if self.is_empty():
            return []
        else:
            return self._left.items() + [self._root] + self._right.items()

    def insert(self, item: Any):
        if self.is_empty():
            self._root = item
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)
        elif item < self._root:
            self._left.insert(item)
        else:
            self._right.insert(item)

    def inorder_visit(self, act: Callable[[BinarySearchTree], None]) -> None:
        if self.is_empty():
            return
        self._left.inorder_visit(act)
        act(self)
        self._right.inorder_visit(act)

    def mirror(self) -> None:
        if self._left is None and self._right is None:
            return
        else:
            self._left, self._right = self._right, self._left
            self._left.mirror()
            self._right.mirror()


if __name__ == '__main__':
    pass
