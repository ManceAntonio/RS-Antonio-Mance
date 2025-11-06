import heapq

def dijkstra(graph, start):
    dist = {cvor: float("inf") for cvor in graph}
    dist[start] = 0
    red = [(0, start)]

    while red:
        udaljenost, cvor = heapq.heappop(red)
        if udaljenost > dist[cvor]:
            continue
        for susjed, tezina in graph[cvor]:
            nova = udaljenost + tezina
            if nova < dist[susjed]:
                dist[susjed] = nova
                heapq.heappush(red, (nova, susjed))
    return dist

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}

print(dijkstra(graph, "A"))