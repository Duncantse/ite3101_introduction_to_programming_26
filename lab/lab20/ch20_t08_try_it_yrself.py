import os
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "outputs/ch20_t08o_output.txt")

with open("outputs/ch20_t08o_output.txt", "w") as my_file:
    my_file.write("mi")
