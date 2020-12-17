"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# Copied over from the read me line 12-17 in the graphs folder
'''{
    '0': {'1', '3'},
    '1': {'0'},
    '2': set(),
    '3': {'0'}
}'''

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:  # If the vertex is already in the dictionay
            return                      # Return it to end the function. You could also just do "not in" on line 24
        self.vertices[vertex_id] = set()    # Add a new vertex the same way we always add things to a dictionary. The dictionary is declared on line 18

    # Scrapped code
    # def add_edge(self, v1, v2): # So using this would look like add_edge(1, 2)
    #     """
    #     Add a directed edge to the graph.
    #     """
    #     if self.vertices[v1] == set():      # If it's just an empty set with no values, like on line 10
    #         self.vertices[v1] = {v2}      # Find v1 in the dictionary and make a new dictionary (with v2 as its key) as its value
    #     else:                           #If there's a dictionary there as its value (meaning there are already some edges)
    #         # We want to add the the dictionary that is v1's value
    #         # self.vertices[v1] = {}
    #         self.vertices[v1]

    # Doc's code
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:     # If both v1 and v2 are in the dictionary (check to see if the vertexes exist)
            self.vertices[v1].add(v2)                       # add v2 to v1's value to make the edge
        else:                                                  # If they don't exist
            raise IndexError("That vertex does not exist!")     # Return an error saying that the vertex doesn't exist

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]     # Return the values (edges) of the key (vertex) we pass into the function

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
    # Code from the Old TK, being used as pseudo code
    # BFS(graph, startVert):
        # for v of graph.vertexes:
        #     v.color = white         # Make all of the vertexes white    (Haven't visited or interacted)
        # startVert.color = gray      # Make the starting vertex gray (Visited, haven't interacted)
        #     queue.enqueue(startVert)    # Enqueue the starting vertex
        # while !queue.isEmpty():             # As long as the queue isn't empty, run the while loop
        #     u = queue[0]  # Peek at head of the queue, but do not dequeue!  # Grab the first item in the queue. The first time the loop runs, this is the starting vertex
        #     for v of u.neighbors:       # For every vector connected to the one we're looking at (so every "neighbor" of the vertex)
        #         if v.color == white:    # If the vector is white (If it's not white, then it's already been visited and doesn't need to be added to the queue)
        #             v.color = gray          # Set its color to gray (visited)
        #             queue.enqueue(v)        # And enqueue it
        #     queue.dequeue()         # This is the actual interaction with the vertex, when we dequeue it. Once we dequeue it, all of its neighbors are still in the queue
        #     u.color = black         # Now that we've interacted with it, change the color to black

        # Side note: Every tree is a graph, but not every graph is a tree. Basically like how every square is a rectangle but not every rectangle is a square

        # Code during Zoom w/ Josh (Scrapped bc of the colors)
        # vertex_queue = []  # Create our own queue, we're not using the built in one so that we can learn
        # for vertex in self.vertices: # For every vertex in our dictionary
        #     vertex.color = "white"      # Give it a color attribute set to white. The color attribute did not exist before this line, we made it just now.
        # starting_vertex.color = "gray"  # Turn the starting vertex gray (Visited and enqueued)
        # vertex_queue.append(starting_vertex)    # Add it to the queue
        # while len(vertex_queue) != 0:           # As long as the queue isn't empty
        #     current = vertex_queue[0]           # Grab the first vertex in the queue
        #     for neighbor in self.vertices[current]:     # Iterate through all of the neighbors of the current vertex
        #         if neighbor.color == "white":       # If the neighbor is unvisited
        #             neighbor.color = "gray"         # Change it to gray to mean visited but not interacted with
        #             vertex_queue.append(neighbor)   # Add it to the queue. Note: Fun times! COlors don't seem to work this way, we'll see what we'll do about that 
        #     vertex_queue.pop(0)                     # Remove our current vertex from the queue, aka the first one
        #     current.color = "black"                 # Change the color of current to black because we've interacted with it

        # Doc's code :)
        q = Queue()                     # Create a queue
        q.enqueue(starting_vertex)      # Enqueue our starting vertex, making it the first item
        visited = set()                 # Create a set called visited to track what nodes we've visited
        while q.size() > 0:             # While the length of the queue isn't zero
            v = q.dequeue()             # Dequeue the first item in the queue and grab it to track the current vertex (v = current)
            if v not in visited:        # If we haven't already visited this vertex
                print(v)                    # Print the vertex
                visited.add(v)              # Add it to the visited set 
                for next_vert in self.get_neighbors(v):     # For every neighbor of the current vertex (v)
                    q.enqueue(next_vert)                        # Enqueue the neighbor
            


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO

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

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
