def view_array_in_loop(left, right, number_of_elements):
    for i in range(number_of_elements):
        line_out = ""
        line_out += left + "[" + str(i) + "] := "
        line_out += right + "[" + str(i) +"];"
        print(line_out)


view_array_in_loop("#some_array", "#some_array", 12)