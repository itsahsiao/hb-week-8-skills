"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node %s>" % self.data

    def get_num_children(self):
        """Get number of children.

        For example::

            >>> a = Node("A", [Node("B"), Node("C")])
            >>> a.get_num_children()
            2
        """

        # FIXME

        return len(self.children)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root=%s>" % self.root

    def depth_first_search(self, data):
        """Return node object with this data, traversing the tree depth-first.

        Start at the root, and return None if not found.
        """

        # FIXME

        # DFS = LIFO
        # Start at the root - check if root.data matches the data argument passed in
        # If not, add its children to list of nodes to look at
        # Check the last node in this list
        # If this node's data does not match the data argument passed in, add this last node's children to the list
        # Continue checking based on last node added to the list
        # We are basically looking further down a branch at a time

        to_look_at = [self.root]

        while to_look_at is not None:
            node = to_look_at.pop()

            if node.data == data:
                return node

            to_look_at.extend(node.children)

    def breadth_first_search(self, data):
        """Return node object with this data, traversing the tree breadth-first.

        Start here (on this node), and return None if not found.

        Let's make a tree where we have two "B" nodes, but where one is far down an
        earlier branch and the other is higher-up in an earlier branch. Since this is
        a BFS, we should find the b2 node for "B"::

                       A
                     /   \
                    C     E
                   /       \
                  D        B2
                 /
                B1

            >>> a = Node("A")
            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> c = Node("C")
            >>> d = Node("D")
            >>> e = Node("E")
            >>> a.children = [c, e]
            >>> c.children = [d]
            >>> d.children = [b1]
            >>> e.children = [b2]
            >>> tree = Tree(a)

            >>> tree.depth_first_search("B") is b2
            True

        """

        to_visit = [self.root]

        while to_visit:
            node = to_visit.pop(0)

            if node.data == data:
                return node

            to_visit.extend(node.children)
