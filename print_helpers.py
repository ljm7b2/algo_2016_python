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
            if val >= 9999999:
                print("NA, ", end="")
            else:
                print("{0:.2f}".format(val) + ", ", end="")
        print(']')
    print()