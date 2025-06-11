import networkx as nx
import matplotlib.pyplot as plt

def generate_dag_from_input(input_str: str):
    """
    Generates a Directed Acyclic Graph (DAG) from a formatted string input.

    The function performs the following steps:
    1.  Parses the input string to identify sequences of nodes that form directed paths.
    2.  Constructs an initial graph with these paths.
    3.  Identifies the leaf nodes (nodes with no outgoing edges) of these paths.
    4.  Sorts the leaf nodes lexicographically.
    5.  Adds directed edges between the sorted leaf nodes to connect the initial paths.

    Args:
        input_str: A string containing the node sequences, with each sequence
                   separated by a blank line.

    Returns:
        A networkx.DiGraph object representing the generated DAG.
    """
    # Create a new directed graph
    G = nx.DiGraph()

    # Split the input string into blocks of node sequences based on empty lines
    node_sequences = [block.strip().split('\n') for block in input_str.strip().split('\n\n')]

    # Add edges for each sequence to form the initial tree-like structures
    for sequence in node_sequences:
        # A sequence with a single node just adds the node to the graph
        if len(sequence) > 1:
            for i in range(len(sequence) - 1):
                u, v = sequence[i], sequence[i+1]
                if u and v:  # Ensure nodes are not empty strings
                    G.add_edge(u, v)
        elif sequence and sequence[0]:
             G.add_node(sequence[0])


    # Identify the leaf nodes (nodes with an out-degree of 0)
    leaf_nodes = [node for node in G.nodes() if G.out_degree(node) == 0]

    # Sort the leaf nodes lexicographically
    leaf_nodes.sort()

    # Add edges between consecutive leaf nodes in the sorted list
    if len(leaf_nodes) > 1:
        for i in range(len(leaf_nodes) - 1):
            G.add_edge(leaf_nodes[i], leaf_nodes[i+1])

    return G

# The input data provided by the user
input_data = """
a
ar
arc
arcs
arcsl
arcslo
arcslog
arcslogg
arcslogge
arcslogger

r
rc
rcs
rcsl
rcslo
rcslog
rcslogg
rcslogge
rcslogger

c
cs
csl
cslo
cslog
cslogg
cslogge
cslogger

s
sl
slo
slog
slogg
slogge
slogger

l
lo
log
logg
logge
logger

o
og
ogg
ogge
ogger

g
gg
gge
gger

g
ge
ger

e
er
r
"""

# Generate the graph
dag = generate_dag_from_input(input_data)

# --- Output and Visualization ---

# Print all the edges in the generated graph
print("Generated Edges:")
for edge in dag.edges():
    print(f"('{edge[0]}' -> '{edge[1]}')")

# Visualize the graph
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(dag, seed=42)  # positions for all nodes
nx.draw(dag, pos, with_labels=True, node_size=700, node_color="skyblue",
        font_size=8, font_weight="bold", arrows=True)
plt.title("Generated Directed Acyclic Graph (DAG)")
plt.show()