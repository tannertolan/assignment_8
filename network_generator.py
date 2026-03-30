import json
import random

def generate_social_network(num_users, min_friends=2, max_friends=8):
    graph = {}
    users = [f"user_{i}" for i in range(1, num_users + 1)]
    for user in users:
        num_friends = random.randint(min_friends, max_friends)
        friends = random.sample(users, num_friends)
        if user in friends:
            friends.remove(user)
        graph[user] = list(set(friends))
    return graph

def save_network(graph, filename):
    with open(filename, 'w') as f:
        json.dump(graph, f, indent=2)

def main():
    for size in [100, 500, 1000]:
        graph = generate_social_network(size)
        filename = f"network_{size}.json"
        save_network(graph, filename)
        print(f"Generated {filename} with {size} users.")

if __name__ == "__main__":
    main()
