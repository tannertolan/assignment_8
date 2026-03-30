import json
import random
import time
import argparse
from collections import deque

# -----------------------------------------------------------
# PART 1: BREADTH-FIRST SEARCH (BFS)
# -----------------------------------------------------------

def bfs(graph, start, target):
    """
    Breadth-First Search for shortest path between two users.
    graph: dict mapping user -> list of friends
    start: starting user
    target: goal user
    returns: shortest path as a list of user IDs or [] if not connected
    """
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == target:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
    return []


# -----------------------------------------------------------
# PART 2: DEPTH-FIRST SEARCH (DFS)
# -----------------------------------------------------------

def dfs(graph, start, visited=None):
    """
    Depth-First Search to find all reachable nodes from start.
    graph: dict mapping user -> list of friends
    start: starting user
    returns: a set of all reachable users
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


# -----------------------------------------------------------
# PART 3: TESTING & BENCHMARKING
# -----------------------------------------------------------

def load_graph(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def test_bfs():
    graph = load_graph("network_100.json")
    start, target = random.sample(list(graph.keys()), 2)
    print(f"Testing BFS shortest path from {start} to {target}")
    path = bfs(graph, start, target)
    print("Shortest path:", path if path else "No connection found")

def test_dfs():
    graph = load_graph("network_100.json")
    start = random.choice(list(graph.keys()))
    print(f"Testing DFS reachability from {start}")
    reachable = dfs(graph, start)
    print(f"Users reachable from {start}: {len(reachable)}")

def benchmark():
    sizes = [100, 500, 1000]
    for size in sizes:
        filename = f"network_{size}.json"
        graph = load_graph(filename)
        print(f"\nBenchmarking on network of {size} users")

        # BFS Benchmark
        start, target = random.sample(list(graph.keys()), 2)
        start_time = time.time()
        path = bfs(graph, start, target)
        bfs_time = time.time() - start_time
        print(f"BFS: {bfs_time:.6f} seconds | Path length: {len(path)}")

        # DFS Benchmark
        start = random.choice(list(graph.keys()))
        start_time = time.time()
        visited = dfs(graph, start)
        dfs_time = time.time() - start_time
        print(f"DFS: {dfs_time:.6f} seconds | Reachable: {len(visited)} users")

# -----------------------------------------------------------
# Command-line interface
# -----------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-bfs", action="store_true")
    parser.add_argument("--test-dfs", action="store_true")
    parser.add_argument("--benchmark", action="store_true")
    args = parser.parse_args()

    if args.test_bfs:
        test_bfs()
    elif args.test_dfs:
        test_dfs()
    elif args.benchmark:
        benchmark()
    else:
        print("Use one of the following options:")
        print("  python graph_traversal.py --test-bfs")
        print("  python graph_traversal.py --test-dfs")
        print("  python graph_traversal.py --benchmark")
