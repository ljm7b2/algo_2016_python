def edge_matrix():
    NA = 9999999
    matrix = [
        [0, 7, NA, 7, NA, 9],
        [NA,0,  5,NA, 10, 3],
        [9, 10, 0, 8,  4, 6],
        [9,  4, 2, 0, NA,NA],
        [3,  5, 10,10, 0,NA],
        [NA, 5, 8, 10, NA,0]
    ]
    return matrix

def flow_matrix_in():
    matrix = [
        [ 0,  9, 11, 12,  8, 12],
        [18,  0, 15, 10, 17, 18],
        [17, 18,  0, 14, 10, 10],
        [17,  8, 10,  0, 17, 18],
        [15,  9, 12, 14,  0, 16],
        [18, 16, 15,  8,  9,  0]
    ]
    return matrix

def flow_matrix_in2():
    matrix = [
        [ 0,  1, 1, 1,  1, 1],
        [1,  0, 1, 1, 1, 1],
        [1, 1,  0, 1, 1, 1],
        [1,  1, 1,  0, 1, 1],
        [1,  1, 1, 1,  0, 1],
        [1, 1, 1,  1,  1,  0]
    ]
    return matrix

def capacity_matrix_in():
    NA = 9999999
    matrix =[
        [0, 13, NA, 33, NA, 20],
        [NA, 0, 67, NA, 5, 55],
        [5, 5, 0, 32, 134, 17],
        [23, 34, 55, 0, NA, NA],
        [68, 47, 20, 14, 0, NA],
        [NA, 16, 44, 16, NA, 0]
    ]
    return matrix

def capacity_matrix_in2():
    NA = 9999999
    matrix = [
        [0, 14, NA, 38, NA, 19],
        [NA, 0, 65, NA, 5, 57],
        [5, 5, 0, 25, 136, 7],
        [15, 31, 47, 0, NA, NA],
        [72, 41, 9, 19, 0, NA],
        [NA, 19, 39, 13, NA, 0]
    ]
    return matrix