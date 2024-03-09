# Graph Data structure


class Graph:
    def __init__(self, size):
        """
        Creates the `adj` matrix with the given size
        """
        self.adj = [[0] * size for i in range(size)]
        self.size = size

    def add_edge(self, orig, dest):
        """
        Adds an edge by setting the corresponding values to 1
        """
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid Edge")
        else:
            self.adj[orig - 1][dest - 1] = 1
            self.adj[dest - 1][orig - 1] = 1

    def remove_edge(self, orig, dest):
        """
        Set's the values to 0
        """
        if orig > self.size or dest > self.size or orig < 0 or dest < 0:
            print("Invalid Edge")
        else:
            self.adj[orig - 1][dest - 1] = 0
            self.adj[dest - 1][orig - 1] = 0

    def display(self):
        for row in self.adj:
            print()
            for val in row:
                print("{:4}".format(val), end="")


# # a sample Graph
# G = Graph(4)
# G.add_edge(1, 3)
# G.add_edge(3, 4)
# G.add_edge(2, 4)
# G.display()


# Singlely Linked List Data Structure


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        """
        Adds a new Node as the head of the list and
        links the previous head to it.
        """
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        """
        Iterates to the end of the list using a while loop
        and adds the new node as the link of the last node.
        """
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while n.next != None:
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end=" => ")
            n = n.next
        print()


# s = LinkedList()
# s.add_at_front(5)
# s.add_at_end(8)
# s.add_at_front(9)

# s.print_list()
# print(s.get_last_node())

# Queue Data Structure


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        """
        Adds an element at the beginning of the list
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Removes the last element of the list
        """
        return self.items.pop()

    def print_queue(self):
        print(self.items)


# q = Queue()
# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('42')
# q.print_queue()

# q.dequeue()
# q.print_queue()

# Stack Data Structure


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        """
        Adds an element at the beginning of the list
        """
        self.items.insert(0, item)

    def pop(self):
        """
        Removes the first element of the list
        """
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)


# s = Stack()
# s.push('a')
# s.push('b')
# s.push('c')
# s.print_stack()

# s.pop()
# s.print_stack()
