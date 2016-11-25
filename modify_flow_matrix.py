from math import fabs
from print_helpers import print_array_float
class mod_flow_matrix():
    def __init__(self, hop_matrix, flow_matrix):
        self.hop_matrix = hop_matrix
        self.flow_matrix = flow_matrix
        self.matrix = [[0 for i in range(len(hop_matrix))] for k in range(len(hop_matrix))]
        self.iter_num = 1
        self.max_hop = self.get_max_hop()
        self.unique_vars_in_flow = self.get_unique_flow_values()
        self.temp_flow = [[0 for i in range(len(flow_matrix))] for k in range(len(flow_matrix))]

    def get_max_hop(self):
        m_hop = 0
        for row in self.hop_matrix:
            for col in row:
                if col > m_hop:
                    m_hop = col
        return m_hop


    def next_hop(self):
        temp_matrix = [[0 for i in range(len(self.hop_matrix))] for k in range(len(self.hop_matrix))]
        for i in range(len(self.hop_matrix)):
            for j in range(len(self.hop_matrix)):
                if self.hop_matrix[i][j] <= self.iter_num:
                    temp_matrix[i][j] = self.flow_matrix[i][j]
        self.iter_num += 1
        return temp_matrix

    def matrix_half(self):
        temp1 = [[0 for x in range(len(self.flow_matrix))] for y in range(len(self.flow_matrix))]
        for i in range(len(self.flow_matrix)):
            for j in range(len(self.flow_matrix)):
                temp1[i][j] = self.flow_matrix[i][j] // 2
        return temp1

    def next_min(self):
        val = self.unique_vars_in_flow.pop(0)
        for i in range(len(self.flow_matrix)):
            for j in range(len(self.flow_matrix)):
                if i != j and self.flow_matrix[i][j] >= val:
                    self.temp_flow[i][j] = val
        return self.temp_flow


    def get_unique_flow_values(self):
        temp = set()
        for i in range(len(self.flow_matrix)):
            for j in range(len(self.flow_matrix)):
                if self.flow_matrix[i][j] != 0:
                    temp.add(self.flow_matrix[i][j])
        return sorted(list(temp))

def necessary_first(F, L, C, EP):
    n = len(F)
    R = [[0 for x in range(n)] for y in range(n)]
    L = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            if(F[i][j] <= C[i][j] and C[i][j] < 9999999):
                L[i][j] += F[i][j]
            elif C[i][j] >= 9999999:
                #L[i][j] = C[i][j]
                R[i][j] = F[i][j]
            else:
                L[i][j] = C[i][j]
                R[i][j] = F[i][j] - C[i][j]

    #print("first L ")
    #print_array_float(L)

    for i in range(n):
        for j in range(n):
            if R[i][j] > 0:
                path = EP[i][j]
                count = 0
                for k in range(len(path) - 1):

                    if (C[path[k] - 1][path[k + 1] - 1] < L[path[k] - 1][path[k + 1] - 1] + R[i][j]):
                        count += 1

                if count == 0:
                    for k in range(len(path) - 1):
                        if R[i][j] < C[path[k] - 1][path[k + 1] - 1] - L[path[k] - 1][path[k + 1] - 1]:
                            L[path[k] - 1][path[k + 1] - 1] += R[i][j]
                        #R[i][j] = 0
                        else:
                            print("here - must find new path says ben")

    #print("2nd R")
    #print_array_float(R)
    return L


def compare_matrix(matrix_a, matrix_b):
    temp = [[0 for x in range(len(matrix_a))] for y in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            if matrix_a[i][j] != 0:
                temp[i][j] = ((matrix_a[i][j] - matrix_b[i][j]) / matrix_a[i][j]) * 100
    return temp


def get_actual_adjusted_delay(ma, mb):
    t = [[0 for i in range(len(ma))] for x in range(len(ma))]

    for i in range(len(ma)):
        for j in range(len(ma)):
            t[i][j] = ma[i][j] * mb[i][j]

    return t





