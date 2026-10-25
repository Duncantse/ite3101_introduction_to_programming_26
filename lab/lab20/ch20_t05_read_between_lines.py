import os
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "inputs/ch20_t05o_output.txt")

my_file = open("ch20_t05o_output.txt", "r")

print(my_file.readline())
my_file.close()
