from graph2 import Graph
from util2 import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for item in ancestors:
        graph.add_vertex(item[0])
        graph.add_vertex(item[1])

        graph.add_edge(item[1], item[0])
    
    earliest_ancestor = -1
    max_len = 1
    veritces = graph.vertices

    queue = Queue()
    queue.enqueue([starting_node])

    while queue.size() > 0:
        path = queue.dequeue()
        current_vertice = path[-1]
        print(f'Current Vertice: {current_vertice}')


        if (len(path) > max_len) or (len(path) == max_len and current_vertice < earliest_ancestor):
            earliest_ancestor = current_vertice
            max_len = len(path)
        for item in veritces[current_vertice]:
            copy_of_path = list(path)
            copy_of_path.append(item)
            queue.enqueue(copy_of_path)
        print(f'Path: {path}')
        
        
    return earliest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 9))