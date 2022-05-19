from __future__ import annotations

from typing import Optional, Any, Union


class Tree:
    """A recursive tree data structure.
    """
    # === Private Attributes ===
    # The item stored at this tree's root, or None if the tree is empty.
    _root: Optional[Any]
    # The list of all subtrees of this tree.
    _subtrees: list[Tree]

    # === Representation Invariants ===
    # - If self._root is None then self._subtrees is an empty list.
    #   This setting of attributes represents an empty tree.
    #
    #   Note: self._subtrees may be empty when self._root is not None.
    #   This setting of attributes represents a tree consisting of just one
    #   value.
    # - self._subtrees does not contain any empty trees.

    def __init__(self, root: Optional[Any], subtrees: list[Tree]) -> None:
        """Initialize a new tree with the given root value and subtrees.

        If <root> is None, this tree is empty.
        Precondition: if <root> is None, then <subtrees> is empty.
        """
        self._root = root
        self._subtrees = subtrees

    def is_empty(self) -> bool:
        """Return whether this tree is empty.

        >>> t1 = Tree(None, [])
        >>> t1.is_empty()
        True
        >>> t2 = Tree(3, [])
        >>> t2.is_empty()
        False
        """
        return self._root is None

    def __len__(self) -> int:
        """Return the number of items contained in this tree.

        >>> t1 = Tree(None, [])
        >>> len(t1)
        0
        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        """
        if self.is_empty():         # tree is empty
            return 0
        elif not self._subtrees:  # tree is a single item
            return 1
        else:                       # tree has at least one subtree
            size = 1  # count the root
            for subtree in self._subtrees:
                size += subtree.__len__()
            return size

    def _str_indented(self, depth: int=0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + str(self._root) + '\n'
            for subtree in self._subtrees:
                # Note that the 'depth' argument to the recursive call is
                # modified.
                s += subtree._str_indented(depth + 1)
            return s

    def __str__(self) -> str:
        """Return a string representation of this tree.
        """
        return self._str_indented(0)

    def _delete_root(self) -> None:
        """Remove the root item of this tree.

        Precondition: this tree has at least one subtree.
        """
        # Get the last subtree in this tree.
        chosen_subtree = self._subtrees.pop()

        self._root = chosen_subtree._root
        self._subtrees.extend(chosen_subtree._subtrees)

    def delete_item(self, item: Any) -> bool:

        if self.is_empty():
            return False              # item is not in the tree
        elif not self._subtrees:
            if self._root != item:    # item is not in the tree
                return False
            else:                     # resulting tree should be empty
                self._root = None
                return True
        else:
            if self._root == item:
                self._delete_root()   # delete the root
                return True
            else:
                for subtree in self._subtrees:
                    deleted = subtree.delete_item(item)
                    if deleted and subtree.is_empty():
                        # The item was deleted and the subtree is now empty.
                        # We should remove the subtree from the list of subtrees.
                        # Note that mutating a list while looping through it is
                        # EXTREMELY DANGEROUS!
                        # We are only doing it because we return immediately
                        # afterwards, and so no more loop iterations occur.
                        self._subtrees.remove(subtree)
                        return True
                    elif deleted:
                        # The item was deleted, and the subtree is not empty.
                        return True
                    else:
                        # No item was deleted. Continue onto the next iteration.
                        # Note that this branch is unnecessary; we've only shown it
                        # to write comments.
                        pass

                # If we don't return inside the loop, the item is not deleted from
                # any of the subtrees. In this case, the item does not appear
                # in <self>.
                return False

    def to_nested_lst(self):
        """Converts the tree to a nested list"""
        if self.is_empty():
            return []
        elif not self._subtrees:
            return [self._root]
        else:
            result = [self._root]
            for subtree in self._subtrees:
                result.append(subtree.to_nested_lst())
            return result

    def leaves(self) -> list:
        """ Returns the leaves of the tree
        >>> t1 = Tree(1, [])
        >>> t2 = Tree(2, [])
        >>> t3 = Tree(3, [])
        >>> t4 = Tree(4, [t1, t2, t3])
        >>> t5 = Tree(5, [])
        >>> t6 = Tree(6, [t4, t5])
        >>> t6.leaves()
        [1, 2, 3, 5]
        """
        if self.is_empty():
            return []
        elif not self._subtrees:
            return [self._root]
        else:
            lst = []
            for subtree in self._subtrees:
                lst.extend(subtree.leaves())
            return lst

    def _get_all_node_values(self) -> list[float]:
        """Returns a list of the the values of the nodes in the tree"""
        nodes = [self._root]
        if self.is_empty():
            return [0.0]
        elif not self._subtrees:
            return [self._root]
        else:
            for subtree in self._subtrees:
                nodes.extend(subtree._get_all_node_values())
        return nodes

    def average(self) -> float:
        """ Return the average of all values in the tree
        >>> new_tree = Tree(1, [Tree(2, []), Tree(3, [])])
        >>> new_tree.average()
        2.0
        """
        temp = self._get_all_node_values()
        return sum(temp) / len(temp)


def to_tree(obj: Union[int, list]):
    """Converts a nest listed into a tree."""
    if isinstance(obj, int):
        return None
    elif not obj:
        return Tree(None, [])
    else:
        potential_root = obj[0]
        potential_subtrees = obj[1:]
        if isinstance(potential_root, list):
            return None

        subtrees = []
        for sublist in potential_subtrees:
            subtree = to_tree(sublist)
            if subtree is None:
                return None
            elif not subtree.is_empty():
                subtrees.append(subtree)

        return Tree(potential_root, subtrees)


if __name__ == "__main__":
    pass
