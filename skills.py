"""
Part 1: Discussion Questions

Runtime

1.  The workload of a function that takes in a list of integers and returns a new list of the even integers is n, the length of the list. 

2.  Runtimes in ascending order by efficiency as n approaches infinity:

    O(1)
    O(log n)
    O(n)
    O(n log n)
    O(n^2)
    O(2^n)


Stacks and Queues

1.  In the following cases, the appropriate data structure that would be better is:
    1.  The process of loading and unloading pallets on a flatbed truck
        - Stack (LIFO)
    2.  Putting bottle caps on bottles of beer as they roll down an assembly line
        - Queue (FIFO)
    3.  Calculating the solution to this mathematical expression: 2 + (7 * 4) - (3 / 2)
        - Stack (LIFO), due to order of operations (PEMDAS)

2.  Two more examples of when a queue would be an appropriate data structure:
    - Waiting in line at Starbucks to order your drink
    - Office printing machine

3.  Two more examples of when a stack would be an appropriate data structure:
    - Taking off clothing
    - Loading groceries into back of car trunk


Linked Lists

1.  The nodes are:
    - <Node Apple> which has the data "Apple" and the next pointer pointing to the node <Node Berry>
    - <Node Berry> which has the data "Berry" and the next pointer pointing to the node <Node Cherry>
    - <Node Cherry> which has the data "Cherry" and the next pointer pointing to None

    The head is <Node Apple>.

    There is no tail, as tail is not an attribute of this linked list. If there was a tail attribute, then the tail would be <Node Cherry>.

2.  For a doubly linked list, nodes have next and prev attributes (and data), but for a singly lined list, nodes have just a next attribute (and data).

3.  It is faster to append to a linked list if we keep track of the tail as an attribute because we don't have to traverse the list every time we add a node.


Trees

1.  A Breadth First Search (BFS) would look at nodes as FIFO - it would look at nodes on the same level before looking at their children.

    To find burrito using BFS for this tree, the order would be: Italian, Indian, Mexican, lasagna, pizza, tikka masala, saag, and burrito.

2.  A Depth First Search would look at nodes as LIFO - it would go to the end of a branch before going to the next branch.

    To find Chicago-style using DFS for this tree, the order would be: Mexican, enchiladas, tacos, burrito, Indian, saag, tikka masala, Italian, pizza, Sicilian, New York-style, Chicago-style.

3. A binary search tree is different from other trees because each node can only have two children.

"""

