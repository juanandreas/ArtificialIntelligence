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


def solve(maze, rows, cols):
    ALL_LED = {}
    for i in range(0, rows):
        for j in range(0, cols):
            if maze[i][j] not in ALL_LED:
                ALL_LED[maze[i][j]] = (i, j)
    # print(ALL_LED) # ALL_LED = ['A', 'B', 'C']

    ALL_GRAPHS = {}
    for led in ALL_LED:
        G = Graph(ALL_LED[led], rows, cols, [led])
        ALL_GRAPHS[led] = G
        G.maze_to_graph(maze)
    
    # for led in ALL_GRAPHS:
    #     print(led)
    #     print(ALL_GRAPHS[led].get_graph())
    #     print("====")

    for led in ALL_GRAPHS:
        if ALL_GRAPHS[led].is_cyclic():
            print('yes')
            return

    
    print('no')
    return



if __name__ == "__main__":
    rows = 3
    cols = 4
    maze = [
        ['A', 'A', 'A', 'A'],
        ['A', 'B', 'C', 'A'],
        ['A', 'A', 'A', 'A']
    ]

    solve(maze, rows, cols)


'''
basically, you're trying to see if there is a loop you can make out of the distinct LED lights
represented in a grid.

super basically, find a cycle for each graph that consists of a single node. if one of them is a cycle,
return yes, else no.

in this example, u can make a cycle out of the nodes 'A', but not 'B' and 'C' but since one cycle exists,
return 'yes'
'''