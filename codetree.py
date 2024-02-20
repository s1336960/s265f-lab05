from graphviz import Graph

num_node = 0

class Node:
    def __init__(self, ch, freq, left, right):
        global num_node
        self.id = str(num_node)
        num_node += 1
        self.ch = ch     # None for internal nodes
        self.freq = freq
        self.left = left   # None for leaf nodes
        self.right = right # None for leaf nodes

class CodeTree:
    def __init__(self):
        self.last = None  # the root is the last created Node
        self.tree = Graph()

        a = Node("a", 5, None, None)
        b = Node("b", 3, None, None)
        c = Node("c", 2, None, None)
        d = Node("d", 1, None, None)
        n1 = Node(None, a.freq + b.freq, a, b)
        n2 = Node(None, n1.freq + c.freq, n1, c)
        self.last = Node(None, n2.freq + d.freq, n2, d)

        self.traverse(self.last)

    def traverse(self, node):
        # Complete by yourself

    def showTree(self):
        self.tree.view()

def main():
    tree = CodeTree()
    tree.showTree()

if __name__ == "__main__":
    main()