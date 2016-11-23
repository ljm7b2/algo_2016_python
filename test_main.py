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

from modify_flow_matrix import mod_flow_matrix
from modify_flow_matrix import compare_matrix
import copy

def main():

    em = edge_matrix()
    #all_pairs_shortest_dist2, shortest_path_tree = f_w2(em)
    #print_array_float(all_pairs_shortest_dist2)
    mod_flow = mod_flow_matrix([], flow_matrix_in())


    while True:
        #print("Edge Matrix - E")
       # print_array(em)

        #print("All pairs shortest path")
        all_pairs_shortest_dist, shortest_path_tree = f_w2(em)
        #if i == 0:
        #print_array_float(all_pairs_shortest_dist)

       # print("Actual paths")
        all_pairs_actual_path = get_actual_paths(all_pairs_shortest_dist, shortest_path_tree)
       # print_array(all_pairs_actual_path)

        #print("Hop Count")
        hop_count = get_hop_count(all_pairs_actual_path)
       # print_array(hop_count)

        #print("Flow Matrix")
       # print_array(flow_matrix_in())

       # print("Load Matrix")

        # -----------------------------
        # modify flow matrix #
        # -----------------------------

        #mod_flow = mod_flow_matrix(hop_count, flow_matrix_in())

        if len(mod_flow.unique_vars_in_flow) == 0:
            break

        mod_flow2 = mod_flow.next_min()

       #print_array_float(mod_flow2)

        # if i == 0:
        #     mod_flow = mod_flow.matrix_half()
        # else:
        #     mod_flow = flow_matrix_in()

        load = get_load_matrix(all_pairs_actual_path, flow_matrix_in())
        #print_array(load)

       # print("Capacity Matrix")
        #print_array(capacity_matrix_in())

        #print("Actual edge delay")
        actual_edge_delay = get_actual_edge_delay(capacity_matrix_in(), load, em)
        #print_array_float(actual_edge_delay)

        #print("Actual path delay")
        actual_path_delay = get_actual_path_delay(actual_edge_delay, all_pairs_actual_path)
        print_array_float(actual_path_delay)

        em = copy.deepcopy(actual_edge_delay)

        #
        #if i == 2:
        #print_array_float(all_pairs_shortest_dist2)
        # print_array_float(actual_path_delay)
        #
        #print_array_float(compare_matrix(all_pairs_shortest_dist2, actual_path_delay))
        #
        print("BREAK")





# run main function :)
main()
#print(compare_matrix([[103]],[[130]]))