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
from modify_flow_matrix import necessary_first
from modify_flow_matrix import compare_matrix
from modify_flow_matrix import get_actual_adjusted_delay

def main():

    print("Edge Matrix - E")
    print_array(edge_matrix())

    print("All pairs shortest path")
    all_pairs_shortest_dist, shortest_path_tree = f_w2(edge_matrix())
    print_array(all_pairs_shortest_dist)

    print("Actual paths")
    all_pairs_actual_path = get_actual_paths(all_pairs_shortest_dist, shortest_path_tree)
    print_array(all_pairs_actual_path)

    print("Hop Count")
    hop_count = get_hop_count(all_pairs_actual_path)
    print_array(hop_count)

    print("Flow Matrix")
    print_array(flow_matrix_in())

    print("Load Matrix")
    load = get_load_matrix(all_pairs_actual_path, flow_matrix_in())
    #print_array(load)

    load = necessary_first(flow_matrix_in(), load, capacity_matrix_in(), all_pairs_actual_path)
    print_array(load)

    print("Capacity Matrix")
    print_array(capacity_matrix_in())

    print("Actual edge delay")
    actual_edge_delay = get_actual_edge_delay(capacity_matrix_in(), load, edge_matrix())
    print_array_float(actual_edge_delay)

    print("Actual path delay")
    actual_path_delay = get_actual_path_delay(actual_edge_delay, all_pairs_actual_path)
    print_array_float(actual_path_delay)

    print("Compared, reduced congestion")
    print_array_float(compare_matrix(get_actual_adjusted_delay(all_pairs_shortest_dist, flow_matrix_in()), actual_path_delay))


    # --revise it ---

    print("Capacity Matrix 2")
    print_array(capacity_matrix_in2())

    print("Actual Edge Delay 2")
    actual_edge_delay_2 = get_actual_edge_delay(capacity_matrix_in2(), load, edge_matrix())
    print_array_float(actual_edge_delay_2)

    print("Actual path delay 2")
    actual_path_delay_2 = get_actual_path_delay(actual_edge_delay_2, all_pairs_actual_path)
    print_array_float(actual_path_delay_2)





# run main function :)
main()
