graph={
    'a':['b','d'],
    'b':[],
    'c':[],
    'd':['e','g'],
    'e':['c'],
    'f':[],
    'g':['f']
    
}

def dfs(graph,source):
    stack=[]
    stack.append(source)
    while stack:
        node=stack.pop(-1)
        print(node)
        for i in graph[node]:
            stack.append(i)
            
dfs(graph,'a')

print()

def bfs(graph,source):
    queue=[]
    queue.append(source)
    while queue:
        node=queue.pop(0)
        print(node)
        for i in graph[node]:
            queue.append(i)
            
bfs(graph,'a')
    
