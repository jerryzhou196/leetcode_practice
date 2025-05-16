"""Simple implementation of Kruskal's algorithm using a disjoint set"""

from collections import namedtuple


Edge = namedtuple("Edge", "weight start end")


class DisjointSet:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0

    def find_root(self):
        if self.parent is not self:
            self.parent = self.parent.find_root()
        return self.parent

    def union(self, other):
        x = self.find_root()
        y = other.find_root()
        if x is y:  # They're in the same set already
            return
        if x.rank < y.rank:
            x.parent = y
        elif x.rank > y.rank:
            y.parent = x
        else:
            y.parent = x
            x.rank += 1


def kruskal(nodes, edges):
    """Given a graph, yield the edges in its minimum spanning tree."""
    forest = dict((n, DisjointSet(n)) for n in nodes)
    for edge in sorted(edges):
        x = forest[edge.start].find_root()
        y = forest[edge.end].find_root()
        if x is not y:
            yield edge
            x.union(y)


test_nodes = "ABCDEFG"
test_edges = """
7 A B
5 A D
8 B C
9 B D
7 B E
5 C E
15 D E
6 D F
8 E F
9 E G
11 F G
""".strip()


def parse_edge_data(s):
    for line in s.split("\n"):
        weight, start, end = line.split()
        yield Edge(int(weight), start, end)


def main():
    for edge in kruskal(test_nodes, parse_edge_data(test_edges)):
        print(edge)


if __name__ == "__main__":
    main()
