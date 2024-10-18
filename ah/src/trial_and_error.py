import heapq

from abc import ABC, abstractmethod, ABCMeta
from typing import Optional

"""
Thinking about going object oriented with the heap
"""


class MergeableHeaps(ABC):
    @abstractmethod
    def make_heap(self):
        pass

    @abstractmethod
    def insert(self, x):
        pass

    @abstractmethod
    def get_min(self):
        pass

    @abstractmethod
    def extract_min(self):
        pass

    @abstractmethod
    def union(self, other):
        if not isinstance(other, MergeableHeaps):
            raise TypeError(f"{other} is not a descendant of MergeableHeaps")
        pass


class BinomialNode:
    def _set_degree(self, parent: 'BinomialNode', child: 'BinomialNode', sibling: 'BinomialNode'):
        if parent and parent.degree:
            return parent.degree - 1
        if child and child.degree:
            return child.degree + 1
        if sibling and sibling.degree:
            return sibling.degree
        return 0

    def __init__(
            self,
            key,
            parent: 'BinomialNode' = None,
            sibling: 'BinomialNode' = None, child:
            'BinomialNode' = None
    ):
        self.parent = parent
        self.sibling = sibling
        self.child = child
        self.key = key
        self.degree = self._set_degree(parent, child, sibling)


class BinomialHeap(MergeableHeaps):
    def __init__(self):
        self.head: Optional[BinomialNode] = None

    def heap_merge(self, other: 'BinomialHeap'):
        """ Very similar to merging two ordered linked lists.
        We override both heaps heads, and set self.head to be the new head
        of the sorted, merged heaps
        # TODO build Test
        """
        new_head = BinomialNode(0)
        curr = new_head
        while self.head and other.head:
            if self.head.degree < other.head.degree:
                curr.sibling = self.head
            else:
                curr.sibling = other.head
            curr = curr.sibling

            self.head = self.head.sibling
            other.head = other.head.sibling

        for bin_heap in [self, other]:
            while bin_heap.head:
                curr.sibling = bin_heap.head
                bin_heap.head = bin_heap.head.sibling
                curr = curr.sibling

        self.head = new_head.sibling

    def heap_union(self, other: 'BinomialHeap'):
        # This will sort the two heaps top level and set self.head to be the smallest (first)
        self.heap_merge(other)
        if not self.head:
            return self
        prev_x = None
        x = self.head
        next_x = x.sibling

    def _binomial_link(self, y: BinomialNode, z: BinomialNode):
        """ y and z are 2 nodes which represent a binomial tree of the same degree
        Time complexity: O(1)
        """
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1

    def make_heap(self):
        pass

    def insert(self, x):
        pass