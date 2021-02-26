import random
# from projects.graph.util import Stack
from collections import deque
class Stack(deque):
    def push(self, value):
        self.append(value)
    # def pop_off(self):
    #     return self.pop()
    def size(self):
        return len(self)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)    #add edges between friends
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):      # gotta get the number being their given us a number of users
            self.add_user(f"user{i}")   # add the user and give them a name

        # Create friendships
        friendships = []
        for user_id in self.users:          # For every use
            for friend_id in range(user_id + 1, self.last_id + 1):      # We came up with potential friendships
                friendships.append((user_id, friend_id))                # And then added those tuples to frienships

        # Shuffle the friendships to randomly distribute them
        random.shuffle(friendships)

        for i in range(0, num_users * avg_friendships // 2):    #ex, 7 users, 7 avg_friendships, means we make 7 edges/connections
            friendship = friendships[i]                         # grab the firendship
            self.add_friendship(friendship[0], friendship[1])   # Add a specific friendship
            

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Solution code: Chaz

        #helper function for bfs
        #returns shortest path from starting_vertex to destination_vertex
        def bfs(graph, starting_vertex, destination_vertex):
            q = deque() # use deque as queue
            q.append([starting_vertex]) # append (to end)
            visited = set()

            while len(q) > 0: # While queue isn't empty
                path = q.popleft() # take from start, built in method of deque
                vert = path[-1] # last node in path

                if vert not in visited:
                    if vert == destination_vertex:  # if we've reached the destination
                        return path # then we've we'e found the path, so return

                    visited.add(vert) #add vert to visited

                    # add all possible paths to queue
                    for next_vert in graph[vert]:
                        new_path = list(path)
                        new_path.append(next_vert)
                        q.append(new_path)

        # dfs for get_all_social_paths
        stack = deque() # use deque as stack
        stack.append([user_id]) # append (to the end)
        friend_paths = {} # friend_paths dict (visited dict)
        while len(stack) > 0:   # while stack is not empty
            path = stack.pop() # remove from the end
            vert = path[-1]     # grab the last node from the path
            if vert not in friend_paths:    # If we haven't visited the node yet
                friend_paths[vert] = bfs(self.friendships, user_id, vert)

                for vert_friend in self.friendships[vert]:
                    new_path = list(path)
                    new_path.append(vert_friend)
                    stack.append(new_path)

        return friend_paths


        # visited = {}  # Note that this is a dictionary, not a set
        # # !!!! IMPLEMENT ME

        # s = Stack()

        # def get_neighbors(id):      # Internal function
        #     return self.friendships[id]

        # s.push(user_id)

        # while s.size() > 0:
        #     user = s.pop()

        #     if user not in visited:
        #         visited[user] = [] # add user to visitor as a key with an empty list as a value

        #         for neighbor in get_neighbors(user): # use our internal function
        #             s.push(neighbor)    # add neighbor to stack
        #             visited[user].append(neighbor)  # append the neighbor to the value, remember a singular vertex can have multiple edges

        # return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
