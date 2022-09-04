#!/usr/bin/python3
""" Define Class Node"""


class Node:

    """ Node Class """
    def __init__(self, data, next_node=None):

        """ initialize new Node object
        Args:
            data(int): new node data
            next_node(Node): next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):

        """ Get Node Data"""
        return self.__data

    @data.setter
    def data(self, value):

        """ set Node data
        Args:
            value(int): node data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):

        """ Get Next Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):

        """ set next Node
        Args:
            value(Node): next Node
        """
        if not(isinstance(value, Node) or value is None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" Define SinglyLinkedList Class"""


class SinglyLinkedList:

    """ Class of SinglyLinkedList"""
    def __init__(self):

        """ initialize singly_linked_list"""
        self.__head = None

    def sorted_insert(self, value):

        """ insert new node into correct sorted order
        Args:
            value(int): new node data
        """
        newNode = Node(value)
        newNode.next_node = None
        cur = self.__head
        prev = self.__head
        if cur is None:
            self.__head = newNode
            return
        while (cur is not None) and cur.data < value:
            prev = cur
            cur = cur.next_node
        if cur is None:
            prev.next_node = newNode
        elif cur == self.__head:
            newNode.next_node = cur
            self.__head = newNode
        else:
            newNode.next_node = cur
            prev.next_node = newNode

    def __str__(self):

        """ string representation of singly_linked_list"""
        str_rep = []
        cur = self.__head
        while cur is not None:
            str_rep.append(cur.data)
            str_rep.append("\n")
            cur = cur.next_node
        if str_rep != []:
            str_rep.pop()
        return "".join([str(i) for i in str_rep])
