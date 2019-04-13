from queue import Queue
MAX = 100
V = 9 # Đỉnh
E = 8 # Cạnh
# graph = [[] for i in range(V+1)]
# for i in range(E):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
visited = [False for i in range(V+1)]
root = 2
graph = [[], [2, 3, 4], [1], [1], [1, 5, 6], [4], [4, 8, 7], [6, 9], [6], [7]]
q = Queue()
visited[root] = True
q.put(root)
while q.empty() == False:
	print(q.queue)
	u = q.get()
	for v in graph[u]:
		if visited[v] == False:
			visited[v] = True
			q.put(v)
print(visited[1::])
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.qsize())
# print(q.queue)
# q.get() 
# q.get() 

# print(q.queue)