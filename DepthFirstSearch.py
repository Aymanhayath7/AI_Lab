graph = {
  'A' : ['B','D'],
  'B' : ['C', 'E'],
  'D' : ['E'],
  'C' : [],
  'E' : ['A','F'],
  'F' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'E')
