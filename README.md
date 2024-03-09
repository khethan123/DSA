# Data Structures and Algorithms (DSA)

## Stack

A stack is a simple data structure that adds and removes elements in a particular order. Every time an element is added, it goes on the "top" of the stack. Only an element at the top of the stack can be removed, just like a stack of plates. This behavior is called LIFO (Last In, First Out).

<div style="text-align:center"><img src="link_to_stack_image" alt="Stack" /></div>

### Terminology

- Adding a new element onto the stack is called **push**.
- Removing an element from the stack is called **pop**.

### Applications

Stacks can be used to create undo-redo functionalities, parsing expressions (infix to postfix/prefix conversion), and much more.

> [!NOTE]
> A stack can be implemented using a list in Python.

## Queue

A queue is similar to a stack, but defines a different way to add and remove elements. The elements are inserted from one end, called the rear, and deleted from the other end, called the front. This behavior is called FIFO (First in First Out).

<div style="text-align:center"><img src="link_to_linked_list_image" alt="Queue" /></div>

### Terminology

- The process of adding new elements into the queue is called **enqueue**.
- The process of removal of an element from the queue is called **dequeue**.

### Applications

Queues are used whenever we need to manage objects in order starting with the first one in. Scenarios include printing documents on a printer, call center systems answering people on hold, and so on.

> [!NOTE]
> A Python list is the easiest way to implement a queue functionality.

## Linked List

A linked list is a sequence of nodes where each node stores its own data and a link to the next node. One node links to another forming what can be thought of as a linked chain:

<div style="text-align:center"><img src="link_to_linked_list_image" alt="Linked List" /></div>

The first node is called the head, and it's used as the starting point for any iteration through the list. The last node must have its link pointing to None to determine the end of the list.

Unlike stacks and queues, you can insert and remove nodes in any position of the linked list (similar to a standard list).

### Applications

Linked lists are useful when your data is linked. For example when you need undo/redo functionality, the nodes can represent the state with links to the previous and next states. Another example would be a playlist of music, where each clip is linked with the next one.

> [!NOTE]
> Linked lists can also be used to create other data structures, such as stack, queues, and graphs.

## Graph

Graphs are used to represent many real-life applications like networks, transportation paths of a city, and social network connections.

A graph is a set of connected nodes where each node is called a Vertex and the connection between two of them is called an Edge.

<div style="text-align:center"><img src="link_to_graph_image" alt="Graph" /></div>

This can represent, for example, connections on a social network, where each Vertex represents a person and the Edges represent connections.

A graph can be represented using a square matrix, where each element represents the edges: 0 indicates no edge, while 1 indicates an edge. The rows and columns represent the vertices.

For example:
```
0 1 1
1 0 0
1 0 0
```

---

## Source

This README content is based on the [Python Data Structures course on SoloLearn](https://www.sololearn.com/en/). The information has been adapted for use in this repository.
