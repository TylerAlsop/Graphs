    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        visited_vertices = set()

        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        while queue.size() > 0:
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            if current_vertex not in visited_vertices:

                if current_vertex == destination_vertex:
                    return current_path

                visited_vertices.add(current_vertex)

                for neighbor_vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)

                    queue.enque({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                        })



    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()
        visited_vertices = set()

        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })

        while stack.size() > 0:
            current_obj = stack.pop()
            current_path = current_obj['path']
            current_vertex = current_obj['current_vertex']

            if current_vertex not in visited_vertices:

                if current_vertex == destination_vertex:
                    return current_path

                visited_vertices.add(current_vertex)

                for neighbor_vertex in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)

                    stack.push({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                        })