from __future__ import annotations

from typing import Any, Optional


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self, items: list) -> None:
        """Initialize a new empty linked list containing the given items.

        Note: this is the inefficient version of the initializer from the
        lecture notes. Feel free to replace it with your own version from Lab 5!
        """
        self._first = None
        for item in items:
            self.append(item)

    def __len__(self):
        curr = self._first
        length = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def is_empty(self) -> bool:
        """Return whether this linked list is empty.

        >>> LinkedList([]).is_empty()
        True
        >>> LinkedList([1, 2, 3]).is_empty()
        False
        """
        return self._first is None

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.
        """
        curr = self._first
        curr_index = 0

        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1

        assert curr is None or curr_index == index

        if curr is None:
            raise IndexError
        else:
            return curr.item

    def __contains__(self, item):
        curr = self._first
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next
        return False

    def append(self, item: Any) -> None:
        """Append <item> to the end of this list.

        >>> lst = LinkedList([1, 2, 3])
        >>> str(lst)
        '[1 -> 2 -> 3]'
        >>> lst.append(4)
        >>> str(lst)
        '[1 -> 2 -> 3 -> 4]'
        """
        if self._first is None:
            self._first = _Node(item)
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next
            curr.next = _Node(item)

    def insert(self, index: int, item: Any) -> None:
        """Insert a the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.

        # >>> lst = LinkedList([1, 2, 10, 200])
        # >>> lst.insert(2, 300)
        # >>> str(lst)
        # '[1 -> 2 -> 300 -> 10 -> 200]'
        # >>> lst.insert(5, -1)
        # >>> str(lst)
        # '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        # >>> lst.insert(100, 2)
        # Traceback (most recent call last):
        # IndexError
        """
        # Create new node containing the item
        new_node = _Node(item)
        if index < 0:
            raise IndexError
        elif index == 0:
            self._first, new_node.next = new_node, self._first
        else:
            # Iterate to (index-1)-th node.
            curr = self._first
            curr_index = 0
            while curr is not None and curr_index < index - 1:
                curr = curr.next
                curr_index += 1

            if curr is None:
                raise IndexError
            else:
                # Update links to insert new node
                curr.next, new_node.next = new_node, curr.next

    def __iter__(self) -> LinkedListIterator:
        """Return an iterator for this linked list.

        It should be straightforward to initialize the iterator here
        (see the class documentation below). Just remember to initialize
        it to the first node in this linked list.
        """
        return LinkedListIterator(self._first)

    def __eq__(self, other: LinkedList):
        curr1 = self._first
        curr2 = other._first

        # if len(self) != len(other):
        #     return False

        while curr1 is not None and curr2 is not None:
            if curr1.item != curr2.item:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        if curr1 is not None or curr2 is not None:
            return False

        return True

    def pop_at_index(self, index):
        if index < 0:
            raise IndexError
        elif index == 0:
            x = self._first.item
            self._first = self._first.next
            print("Deleted element: ", x)
        else:
            curr = self._first
            i = 0
            while curr is not None and i < index - 1:
                curr = curr.next
                i += 1

            if curr is None or i == len(self) - 1:
                raise IndexError
            else:
                x = curr.next.item
                curr.next = curr.next.next
                print("Deleted element: ", x)


if __name__ == '__main__':
    pass
