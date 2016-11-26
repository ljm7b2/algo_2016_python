import os
def read_file(fileN):
    fileName = fileN
    file_data = open(fileName, "r")
    count = 0
    all_data = []
    for line in file_data:
        if count > 0:
            line = line.strip()
            line = line.split(',')
            if line[0] != '':
                all_data.append(line)
        else:
            params = line.strip().split(',')
        count += 1
    file_data.close()
    return build_matrices(params, all_data)


def build_matrices(params, all_data):
    n, start, fin = params
    print("N value: ", n, end = " ")
    n = int(n)
    E = [[0 for x in range(n)] for y in range(n)]
    F = [[0 for x in range(n)] for y in range(n)]
    C = [[0 for x in range(n)] for y in range(n)]
    for val in all_data:
        if val[0] == 'E':
            if int(val[1]) - 1 != int(val[2]) - 1:
                E[int(val[1]) - 1][int(val[2]) - 1] = int(val[3])
            else:
                E[int(val[1]) - 1][int(val[2]) - 1] = 9999999
        elif val[0] == 'F':
            F[int(val[1]) - 1][int(val[2]) - 1] = int(val[3])
        elif val[0] == 'C':
            if int(val[1]) - 1 != int(val[2]) - 1:
                C[int(val[1]) - 1][int(val[2]) - 1] = int(val[3])
            else:
                C[int(val[1]) - 1][int(val[2]) - 1] = 9999999
    for i in range(n):
        for j in range(n):
            if i != j:
                if E[i][j] == 0:
                    E[i][j] = 9999999
                if C[i][j] == 0:
                    C[i][j] = 9999999
    return E, F, C


def get_all_files_in_dir(directory):
    all_files = os.listdir(os.path.join(os.getcwd(), directory))

    return list(map(lambda x: os.path.join(directory, x), all_files))