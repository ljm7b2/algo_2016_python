def print_array(arr):
    for line in arr:
        print('[', end='')
        for val in line:
            if val == 9999999:
                print("NA, ", end="")
            else:
                print(str(val) + ", ", end="")
        print(']')
    print()

def print_array_float(arr):
    for line in arr:
        print('[', end='')
        for val in line:
            if val == 9999999:
                print("NA, ", end="")
            elif val > 9999999:
                print(u"\u221E" + ", ", end="")
            else:
                print("{0:.2f}".format(val) + ", ", end="")
        print(']')
    print()

def print_dist_from_a_b(graph, a, b, path):

    print("From", str(a), "to", str(b))
    for i in range(len(path)-1):
        print(path[i],path[i+1], "-->", graph[path[i]-1][path[i+1]-1])