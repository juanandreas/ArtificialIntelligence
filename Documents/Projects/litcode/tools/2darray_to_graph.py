from collections import defaultdict

class Graph:
    def __init__(self, parent, maze_rows, maze_cols, condition):
        self.graph = {}
        self.parent = parent
        self.maze_rows = maze_rows
        self.maze_cols = maze_cols
        self.condition = condition

    def get_graph(self):
        for node in self.graph:
            print ("{0}:{1}".format(node, self.graph[node]))

    def make_edges(self, M, r, c):
        adj = []

        # check right
        if c+1 >= 0 and c+1 < self.maze_cols:
            if M[r][c+1] in self.condition:
                    adj.append((r, c+1))

        # check left
        if c-1 >= 0:
            if M[r][c-1] in self.condition:
                    adj.append((r, c-1))
        # check down
        if r+1 >= 0 and r+1 < self.maze_rows:
            if M[r+1][c] in self.condition:
                    adj.append((r+1, c))
        # check up
        if r-1 >= 0:
            if M[r-1][c] in self.condition:
                    adj.append((r-1, c))

        self.graph[(r,c)] = adj

    def maze_to_graph(self, M):
        for r in range(0, self.maze_rows):
            for c in range(0, self.maze_cols):
                if M[r][c] in self.condition:
                    self.make_edges(M, r, c)

    def DFS(self, v, dest, visited, parent):
        visited[v] = True

        if parent == dest:
            print("{} to {} is reachable".format(parent, dest))
            
        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if(self.DFS(neighbor, dest, visited, parent)):
                    return True
            
            elif parent != neighbor:
                return True

        return False

    def is_path(self, dest):
        visited = defaultdict(bool)
        for node in self.graph:
            if visited[node] == False:
                if self.DFS(node, dest, visited, self.parent) == True:
                    return True
        return False

    # A recursive function that uses visited[] and parent to detect 
    # cycle in subgraph reachable from vertex v. 
    def isCyclicUtil(self, v, visited, parent): 

        #Mark the current node as visited  
        visited[v]= True

  
        #Recur for all the vertices adjacent to this vertex 
        for neighbor in self.graph[v]: 

            # If the node is not visited then recurse on it 
            if visited[neighbor]==False :  
                if(self.isCyclicUtil(neighbor, visited, v)): 
                    return True
            # If an adjacent vertex is visited and not parent of current vertex, 
            # then there is a cycle 
            elif  parent != neighbor: 
                return True
          
        return False


    def is_cyclic(self):
        visited = defaultdict(bool)
        # Call the recursive helper function to detect cycle in different 
        #DFS trees 
        for node in self.graph: 
            if visited[node] == False: #Don't recur for u if it is already visited 
                if(self.isCyclicUtil(node, visited, self.parent))== True: 
                    return True
          
        return False

def print_maze(m):
    for row in m:
        print(row)

def find_destination(m, target):
    for r in range(0, rows):
        for c in range(0, cols):
            if m[r][c] == target:
                return (r, c)


if __name__ == "__main__":
    # rows = 2
    # cols = 2
    # maze = [
    #         [0,0],
    #         [1,2]
    #     ]

    rows = 5
    cols = 5
    maze = [
        [0, 0, 1, 1, 0],
        [1, 0, 1, 0 ,0],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 2, 1],
        [1, 1, 1, 1, 1]
    ]

    # rows = 3
    # cols = 4
    # maze = [
    #     ['A', 'A', 'A', 'A'],
    #     ['A', 'B', 'C', 'A'],
    #     ['A', 'A', 'A', 'A']
    # ]

    
    G = Graph((0,0), rows, cols, [0,2])
    G.maze_to_graph(maze)
    G.get_graph()
    print("======")
    # print(G.is_cyclic())


    destination = find_destination(maze, 2)
    print(G.is_path(destination))
