"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if v1 not in self.vertices:
        #     self.add_vertex(v1)
        #     self.vertices[v1]
        # if v2 not in self.vertices:
        #     self.add_vertex(v2)
        #     self.vertices[v2]
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def add_bidirectional_edge(self, v1, v2):
        self.add_edge(v1, v2)
        self.add_edge(v2, v1)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            print("That vertex does not yet exist")
            return
        else:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create an empty Queue and enqueue the starting_vertex
        queue = Queue()
        queue.enqueue(starting_vertex)
    
        # Create an empty set to track visited verticies
        visited_vertices = set()
        
        # while queue is not empty:
        while queue:
            # Get the current vertex (dequeue from queue)
            current_vertex = queue.dequeue()

            # Check to see if the current vertex has not been visited. If it hasn't been visited:
            if current_vertex not in visited_vertices:
                # Print the current vertex
                print(current_vertex)
                # Mark the current vertex as being visited
                    # Add the current vertex to a visted_set
                visited_vertices.add(current_vertex)
                # Queue up all the neighbors of the current vertex (So we can visit them next)
                neighbors = self.get_neighbors(current_vertex)

                for neighbor in neighbors:
                    if neighbor not in visited_vertices:
                        queue.enqueue(neighbors)

            # If the current vertex has been visited:
            if current_vertex in visited_vertices:
                # Pop it off of the queue
                queue.dequeue()


        ########################## Without other class methods ##########################
        # # Create an empty Queue and enqueue the starting_vertex
        # queue = []
        # starting_vertex = self.vertices[starting_vertex]
        # queue.append(starting_vertex)
        # # Create an empty set to track visited verticies
        # visited_set = set()
        
        # # while queue is not empty:
        # while queue:
        #     # Get the current vertex (dequeue from queue)
        #     current_vertex = queue.pop(0)

        #     # Check to see if the current vertex has not been visited. If it hasn't been visited:
        #     if current_vertex not in visited_set:
        #         # Print the current vertex
        #         print(current_vertex)
        #         # Mark the current vertex as being visited
        #             # Add the current vertex to a visted_set
        #         visited_set.add(current_vertex)
        #         # Queue up all the neighbors of the current vertex (So we can visit them next)
        #         current_neighbors = self.get_neighbors(current_vertex)
        #         queue.append(current_neighbors)
        #     # If the current vertex has been visited:
        #     if current_vertex in visited_set:
        #         # Pop it off of the queue
        #         queue.pop(0)
        


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

        # Create an empty stack and stack the starting_vertex
        stack = []
        # Create an empty set to track visited verticies
        visted_set = set()
        
        # while stack is not empty:
        while stack:
            # Get the current vertex (un-stack from stack)
            current_vertex = starting_vertex

            # Check to see if the current vertex has not been visited. If it hasn't been visited:
                # Print the current vertex
                # Mark the current vertex as being visited
                    # Add the current vertex to a visted_set
                # stack up all the neighbors of the current vertex (So we can visit them next)
            # If the current vertex has been visited:
                # Pop it off of the stack



    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
        #**** Check the code for bft and augment a few things ****#

        # Create an empty Queue and enqueue the PATH TO THE starting_vertex
        # queue = []
        # Create an empty set to track visited verticies
        # visted_set = set()
        
        # while queue is not empty:
        # while queue:
            # Get the current vertex PATH (dequeue from queue)
            # SET THE CURRENT VERTEX TO THE LAST ELEMENT OF THE PATH

            # Check to see if the current vertex has not been visited. If it hasn't been visited:
                # CHECK IF THE CURRENT VERTEX IS THE DESTINATION
                # IF IT IS, STOP AND RETURN

                # Mark the current vertex as being visited
                    # Add the current vertex to a visted_set

                # Queue up NEW PATHS WITH EACH NEIGHBOR:
                    # TAKE CURRENT PATH
                    # APPEND THE NEIGHBOR TO IT
                    # QUEUE UP NEW PATH


        # If the current_path[len(current_path -1)] == destination_vertex:
            # return current_path


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # # graph.dft(1)
    # # graph.dft_recursive(1)

    # # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
