class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)]
                      for row in range(V)]

    def print_shortest(self, dist, node):
        if int(dist[node]) >= 10 ** 7:
            print(-1)
        else:
            print(dist[node])

    def search_minDistance(self, dist, sptSet):
        current_path = 10 ** 8
        min_index = 0
        # если вершина не просмотрена, находим наименьшее расстояние до нее
        for v in range(self.V):
            if dist[v] < current_path and not sptSet[v] and dist[v] != -1:
                current_path = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, start, end):

        dist = [10 ** 8] * self.V  # минимальное расстояние до вершин
        dist[start] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            # выбираем минимальную вершину из непросмотренных
            u = self.search_minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        not sptSet[v] and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_shortest(dist, end)


V, start, end = list(map(int, input().split()))
g = Graph(V)
matrix = [list(map(int, input().split())) for i in range(V)]
g.graph = matrix
start -= 1  # начало индексации с нуля
end -= 1
g.dijkstra(start, end)
