#!/usr/bin/python3

"""Developing node and singly linked list in python"""


class Node:
    """a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Members of Node
        Args:
            data: data of node
            next_node = reference to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initializing the head"""
        self.head = None

    def __repr__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
