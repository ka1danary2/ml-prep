В дереве, в котором есть 2 и более вершины всегда есть хотя бы одна висячая вершина
Висячая вершина - это вершина, степень которой = 1. То есть она инцидентная всего 1 другой вершине

Граф отличается от дерева тем, что граф - это любое представление вершин и связей, в них могут быть и циклы и петли и все что угодно

Дерево - это строгая иерархическая структура, из корня которой выходят предки. В дереве запрещены циклы, между жвумя любыми узлами существует только 1 возможный путь и дерево должно быть полностью связанным

Доказать существование наличия такой вершины очень просто, достаточно представить граф в виде лабиринта, по которому мы гуляем. Сколько бы мы не ходили, мы всегда упремся в стену (в лист)

Но, прежде чем искать висячие вершины, стоит убедиться, что нам дано дерево, а не обычный граф. 

<mark style="background:#d2cbff">В дереве не может быть циклов и граф должен быть полность связным, то есть у него может быть всего 1 компонента связанности</mark>

Чтобы проверить граф на наличие циклов, нужно использовать dfs 

```python
import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """


    def dfs(graph: dict[str, list], visited: dict[str, int], start: str, parent=None) -> bool:
    # мы пришли в вершину, мы в процессе ее обхода, поэтому статус = 1
        visited[start] = 1

        for to in graph[start]:
            if to == parent:
                continue
            if visited[to] == 0:
                if dfs(graph, visited, to, start):
                    return True
            elif visited[to] == 1:
                return True
        
        visited[start] = 2

        return False


    n = int(input())

    vertextNames = list(map(str, input().split()))

    graph = {name: [] for name in vertextNames}
    # статусы могут быть 0 (не были), 1 (в процессе обхода), 2 (полностью обошли вершину в глубину)
    visited = {name: 0 for name in vertextNames}

    hasCicles = False
    hasOneMoreСonnectivity= False
    hasSheet = False

    m = int(input())

    for _ in range(m):
        a, b = map(str, input().split())

        graph[a].append(b)
        graph[b].append(a)
    
    for values in graph.values():
        if len(values) == 1:
            hasSheet = True
    
    hasCicles = dfs(graph, visited, 'A')
    
    print(visited)

    if 0 in visited.values():
        hasOneMoreСonnectivity = True
        
    if not hasOneMoreСonnectivity and not hasCicles and hasSheet:
        print('YES')
    else:
        print('NO')
   
    pass


if __name__ == '__main__':
    main()

```