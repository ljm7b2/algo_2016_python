import copy
def f_w2(graph):
    temp_graph = copy.deepcopy(graph)
    n = len(temp_graph)
    next = [[i+1 for i in range(n)] for x in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if temp_graph[i][k] + temp_graph[k][j] < temp_graph[i][j]:
                    temp_graph[i][j] = temp_graph[i][k] + temp_graph[k][j]
                    next[i][j] = next[i][k]
    a_paths = get_actual_paths(temp_graph, next)
    get_hop_count(a_paths)
    return temp_graph, next

def get_actual_paths(dist, next):
    actual_path_matrix = []
    for i in range(len(next)):
        temp = []
        for j in range(len(next)):
            if i != j:
                u, v = i + 1, j + 1
                actual_path = [u]
                while u != v:
                    u = next[u-1][v-1]
                    actual_path.append(u)
                temp.append(actual_path)
            else:
                temp.append([i+1])
        actual_path_matrix.append(temp)
    return actual_path_matrix

def get_hop_count(graph):
    n = len(graph)
    hop_count = []
    for i in range(n):
        hops = list(map(lambda x : len(x)-1, graph[i]))
        hop_count.append(hops)
    return hop_count

def get_load_matrix(graph, flow):
    n = len(graph)
    load_matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            path = graph[i][j]
            for k in range(len(path)-1):
                load_matrix[path[k]-1][path[k+1]-1] += flow[i][j]
    return load_matrix





