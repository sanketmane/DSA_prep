# check if node can be visited from source node in a graph.

from collections import deque

# Input
arr = [[1,2],[1,4],[2,4],[2,3],[3,5],[5,6],[4,5]]
n = len(arr)

# create an empty adjacency matrix of n+1 nodes
adj_lst = [[] for x in range(n)]
for i in arr:
  ele1 = i[0]
  ele2 = i[1]
  adj_lst[ele1].append(ele2)
  adj_lst[ele2].append(ele1)

q = deque()

# create a visited array of n+1 nodes
visited = [False] * n

# Add the source node to queue and mark it as True in visited array
# Keep popping nodes and check its neighbours are marked visited.
# If not add them to queue and mark them visited

q.append(1)
visited[1] = True
while len(q) > 0:
  front = q.popleft()
  ele_size = len(adj_lst[front])
  for i in range(ele_size):
    v = adj_lst[front][i]
    if visited[v] is False:
      visited[v] = True
      q.append(v)

print(visited)





