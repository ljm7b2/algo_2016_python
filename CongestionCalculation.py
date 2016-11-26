def get_actual_edge_delay(C, L, E):
    n = len(C)
    G = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if L[i][j] <= C[i][j]:
                G[i][j] = ((C[i][j] + 1) / ( C[i][j] + 1 - L[i][j])) * E[i][j]
            else:
                G[i][j] = 9999999
    return G

def get_actual_path_delay(graph, paths):
    n = len(graph)
    actual_delay = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(len(paths[i][j])-1):
                if len(paths[i][j]) > 1:
                    temp = paths[i][j]
                    actual_delay[i][j] += graph[temp[k]-1][temp[k+1]-1]

    return actual_delay