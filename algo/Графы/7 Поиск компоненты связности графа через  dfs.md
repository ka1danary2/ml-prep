При запуске из одной вершины, dfs гарантированно обойдет все ее вершины. Для поиска всех компонент связности, нам нужно обходить каждую непосещенную вершину. То есть пока в словаре всех вершин есть вершины с меткой не посещенные, мы будем двигать цикл

- Вход: Граф G в виде списка смежностей
- Выход: Количество компонент связности

```
# 5 компонент связности
5
2 2 2 2 2

# 1 компонента связности
5
1 2 2 2 3
```

![[IMG_8208.jpeg]]

Мое решение через dfs:
```python

def dfs(vertexes_local, visited_local, start_vertex):
    visited_local[start_vertex] -= 1

    for vertex in vertexes_local:
        if vertex != start_vertex:
            if visited_local[vertex] != 0:
                dfs(vertexes_local, visited_local, vertex)

v = int(input())

vertexes = list(map(int, input().split()))
visited = {}
counter = 0

for i in range(v):
    if vertexes[i] not in visited:
        visited[vertexes[i]] = 0
    
    visited[vertexes[i]] += 1


for vertex in vertexes:
    if visited[vertex] != 0:
        dfs(vertexes, visited, vertex)
        counter += 1

print('Количество компонент связности - ', counter)

```