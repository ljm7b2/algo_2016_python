from InputStructures import edge_matrix
from InputStructures import capacity_matrix_in
from InputStructures import flow_matrix_in
from InputStructures import capacity_matrix_in2
from print_helpers import print_array
from print_helpers import print_array_float
from CongestionCalculation import get_actual_edge_delay
from CongestionCalculation import get_actual_path_delay
from floyd_warshall import f_w2
from floyd_warshall import get_actual_paths
from floyd_warshall import get_hop_count
from floyd_warshall import get_load_matrix
from modify_flow_matrix import compare_matrix
from modify_flow_matrix import necessary_first
from modify_flow_matrix import get_actual_adjusted_delay

import copy

def main():

    em = copy.deepcopy(edge_matrix())

    for i in range(1):

        all_pairs_shortest_dist, shortest_path_tree = f_w2(em)

        print_array(all_pairs_shortest_dist)
        all_pairs_actual_path = get_actual_paths(all_pairs_shortest_dist, shortest_path_tree)

        hop_count = get_hop_count(all_pairs_actual_path)

        load = get_load_matrix(all_pairs_actual_path, flow_matrix_in())

        load2 = necessary_first(flow_matrix_in(), load, capacity_matrix_in2(), all_pairs_actual_path)

        #print("Load")
        #print_array_float(load2)

        actual_edge_delay = get_actual_edge_delay(capacity_matrix_in2(), load2, em)

        actual_path_delay = get_actual_path_delay(actual_edge_delay, all_pairs_actual_path)

        print("actual path delay")
        print_array_float(actual_path_delay)

        em = copy.deepcopy(actual_edge_delay)

        print_array_float(compare_matrix( get_actual_adjusted_delay(all_pairs_shortest_dist, flow_matrix_in()), actual_path_delay ))


# run main function :)
main()
