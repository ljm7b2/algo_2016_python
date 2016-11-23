from math import fabs
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



        pass

    def get_unique_flow_values(self):
        temp = set()
        for i in range(len(self.flow_matrix)):
            for j in range(len(self.flow_matrix)):
                if self.flow_matrix[i][j] != 0:
                    temp.add(self.flow_matrix[i][j])
        return sorted(list(temp))





def compare_matrix(matrix_a, matrix_b):
    temp = [[0 for x in range(len(matrix_a))] for y in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            if matrix_a[i][j] != 0:
                temp[i][j] = (fabs(matrix_a[i][j] - matrix_b[i][j]) / matrix_a[i][j]) * 100
    return temp





