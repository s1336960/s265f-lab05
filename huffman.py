from sys import stdin
from graphviz import Graph

num_node = 0

# Task 1: Make Node totally ordered
class Node:
    def __init__(self, ch, freq, left, right):
        global num_node
        self.id = str(num_node)
        num_node += 1
        self.ch = ch     # None for internal nodes
        self.freq = freq
        self.left = left   # None for leaf nodes
        self.right = right # None for leaf nodes

class Huffman:
    def __init__(self, ch_freq):
        self.h = [] # a list of Node objects
        self.last = None  # keep the last created Node
        self.tree = Graph()
        self.code = {}

        for ch, freq in ch_freq:
            # Task 2: Create leaf nodes for self.h
            
        # Construct the Huffman tree 
        while len(self.h) >= 2:
            # Task 3: Combine two min. freq. nodes and update self.h 
        self.traverse(self.last, "")

    def traverse(self, node, c):
        if node.left == None:
            self.tree.node(node.id, label=node.ch+"/"+str(node.freq))
            self.code[node.ch] = c
        else:
            self.tree.node(node.id, label=str(node.freq))
            self.tree.edge(node.id, node.left.id, label="0")
            self.tree.edge(node.id, node.right.id, label="1")
            self.traverse(node.left, c+"0")
            self.traverse(node.right, c+"1")

    def getCode(self):
        return self.code

    def showTree(self):
        self.tree.view()

def main():
    ch_freq = []
    for line in stdin:
        ch, freq = line.split()
        ch_freq.append( (ch,int(freq)) )

    huffman = Huffman(ch_freq)
    huffman.showTree()
    print(huffman.getCode())

if __name__ == "__main__":
    main()