from InputStructures import edge_matrix
from InputStructures import capacity_matrix_in
from InputStructures import flow_matrix_in
from InputStructures import capacity_matrix_in2
from print_helpers import print_dist_from_a_b
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
from import_structures import read_file
from import_structures import get_all_files_in_dir
import copy
import time

def main():

    for file_name in get_all_files_in_dir("input"):

        start_time = time.clock()



        em, F, C, start_node, fin_node = read_file(file_name)

        all_pairs_shortest_dist, shortest_path_tree = f_w2(em)



        #print_array(all_pairs_shortest_dist)
        all_pairs_actual_path = get_actual_paths(all_pairs_shortest_dist, shortest_path_tree)

        path = all_pairs_actual_path[start_node-1][fin_node-1]

        hop_count = get_hop_count(all_pairs_actual_path)

        load2 = necessary_first(F, [], C, all_pairs_actual_path)

        actual_edge_delay = get_actual_edge_delay(C, load2, em)

        actual_path_delay = get_actual_path_delay(actual_edge_delay, all_pairs_actual_path)

        print(", ", file_name.split('\\')[-1], ", Time: ",time.clock() - start_time)
        #print_array_float(compare_matrix( get_actual_adjusted_delay(all_pairs_shortest_dist, F), actual_path_delay ))

        print("predicted edge length")
        print_dist_from_a_b(em, start_node, fin_node, path)

        print("actual edge length")
        print_dist_from_a_b(actual_edge_delay, start_node, fin_node, path)

        print("predicted path length")
        print_dist_from_a_b(all_pairs_shortest_dist, start_node, fin_node, path)

        print("actual path length")
        print_dist_from_a_b(actual_path_delay, start_node, fin_node, path)

        print("hop count:", hop_count[start_node - 1][fin_node - 1])

        print("\n\n")


# run main function :)
main()
