start_number = 1


num_rows = 7
num_columns = 7


for row in range(1, num_rows + 1):
    for column in range(0, num_columns):
        current_number = start_number + column * num_rows + row - 1
        print(f"{current_number:2}", end=" ")
    print()
