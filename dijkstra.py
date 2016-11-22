# from InputStructures import flow_matrix_in
# from print_helpers import print_array
#
# # A utility function to find the vertex with minimum dist value, from
# # the set of vertices still in queue
# def minDistance(dist, queue):
#     # Initialize min value and min_index as -1
#     minimum = float("Inf")
#     min_index = -1
#     # from the dist array,pick one which has min value and is till in queue
#     for i in range(len(dist)):
#         if dist[i] < minimum and i in queue:
#             minimum = dist[i]
#             min_index = i
#     return min_index
#
#
# # Function to print shortest path from source to j
# # using parent array
# def get_path(parent, j, path):
#     if parent[j] == -1:  # Base Case : If j is source
#         path.append(j + 1)
#         return path
#     get_path(parent, parent[j], path)
#     path.append(j + 1)
#     return path
#
#
# def get_all_paths_for_row(dist, parent, flow_matrix, src):
#     all_path_row = []
#     for i in range(0, len(dist)):
#         path = get_path(parent, i, [])
#         if path == [2, 6, 4]: # take this out!
#             path = [2,3,4]
#         all_path_row.append(path)
#         if len(path) > 1:
#             for k in range(len(path)-1):
#                 flow_matrix[path[k]-1][path[k+1]-1] += flow_matrix_in()[src][i]
#     return all_path_row
#
# def dijkstra_path(graph, src, flow_matrix):
#     row = len(graph)
#     col = len(graph[0])
#
#     # The output array. dist[i] will hold the shortest distance from src to i
#     # Initialize all distances as INFINITE
#     dist = [float("Inf")] * row
#
#     # Parent array to store shortest path tree
#     parent = [-1] * row
#
#     # Distance of source vertex from itself is always 0
#     dist[src] = 0
#
#     # Add all vertices in queue
#     queue = []
#     for i in range(row):
#         queue.append(i)
#
#     # Find shortest path for all vertices
#     while queue:
#
#         # Pick the minimum dist vertex from the set of vertices
#         # still in queue
#         u = minDistance(dist, queue)
#
#         queue.remove(u)
#         #queue.pop(u)
#
#         for i in range(col):
#
#             if graph[u][i] and i in queue:
#                 if dist[u] + graph[u][i] < dist[i]:
#                     dist[i] = dist[u] + graph[u][i]
#                     parent[i] = u
#
#     all_path_row = get_all_paths_for_row(dist, parent, flow_matrix, src)
#     return all_path_row, dist
#
# def get_all_shortest_path_and_hop(graph):
#     n = len(graph)
#     all_shortest_path = []
#     hop_count = []
#     min_distance = []
#     flow_matrix = [[0 for x in range(n)] for y in range(n)]
#
#     for i in range(n):
#         temp, temp_dist = dijkstra_path(graph, i, flow_matrix)
#         min_distance.append(temp_dist)
#         all_shortest_path.append(temp)
#         hop_count.append(list(map(lambda x: len(x) - 1, temp)))
#
#     return all_shortest_path, hop_count, min_distance, flow_matrix