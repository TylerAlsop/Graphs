import random

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
            self.friendships[user_id].add(friend_id)
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
        # !!!! IMPLEMENT THE TWO ITEMS BELOW:
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i+1}")
        # Create friendships
        #** Generate ALL possible friendships (Be sure to avoid duplicate friendships)
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # user_id == user_id_2 cannot happen
                # If friendship between user_id and user_id_2 already exists
                # Don't add friendship between user_id_2 and user_id
                possible_friendships.append( (user_id, friend_id) )


        #** Randomly selected X friendships so that everyone has an average of avg_friendships (The formula for X is num_users * avg_friendships // 2)
        #** Shuffle the array and pick X elements from the front of it.
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        return visited


        #**** Notes for the above funciton ****#
        # Try to get the visited dictionary to look like it does below.
        # visited = {
            # user_id: [path to all friends]
        # }


if __name__ == '__main__':
    sg = SocialGraph()
    # sg.add_user("Tyler")
    # sg.add_user("Aimee")
    # sg.add_user("Eric")
    # sg.add_user("Rachel")
    # sg.add_friendship(0, 1)

    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
