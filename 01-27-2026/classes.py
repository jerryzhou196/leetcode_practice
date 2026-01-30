
# (0, 1), (1, 2), (2, 3), (3, 4)

# create a graph representation
# also keep track of incoming degree

def minimumSemesters(n, requisites): 
    adjacency_list = [set() for _ in range(n)]
    deg = [0 for _ in range(n)]
    for course, prereq in requisites: 
        adjacency_list[prereq].add(course)
        deg[prereq] += 1
    
    q = deque()
    
    for i in range(len(deg)):
        if deg[i] == 0:
            q.append(i)
    
    while q: 
        clss = q.popleft()
        for neighbour in adjacency_list[clss]:
            deg[neighbour] -= 1
            if deg[neighbour] == 0: 
                q.append(clss)

    
    

    

    



adjacency list
[
    0: 
    1: 0
    2: 1
    3: 2
    4: 3
]

deg: 
[
    0: 0
    1: 1
    2: 1
    3: 1
    4: 1
]


