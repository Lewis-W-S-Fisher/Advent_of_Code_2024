import os
import re

def get_matrix(file):
    matrix = [x.strip() for x in file.readlines()]
    return matrix

def find_xmas_in_strings(input):
    pattern = r"XMAS"
    forward_result = re.findall(pattern, input)
    reverse_result = re.findall(pattern, input[::-1])
    return sum([len(forward_result), len(reverse_result)])

# def find_x_mas_in_strings(input):
#     pattern = r"MAS"
#     forward_result = re.findall(pattern, input)
#     reverse_result = re.findall(pattern, input[::-1])
#     return sum([len(forward_result), len(reverse_result)])

def search_verticle_horizontal(matrix):
    n_row = len(matrix)
    n_col = len(matrix[0])

    # Search vertical
    horizontal_strings = [matrix[x] for x in range(n_col)]
    verticle_strings = []
    for i in range(n_row):
        verticle_strings.append("".join([matrix[x][i] for x in range(n_col)]))
    # search horizontal
    horizontal_xmas = sum([find_xmas_in_strings(x) for x in horizontal_strings])
    verticle_xmas = sum([find_xmas_in_strings(x) for x in verticle_strings])
    return sum([horizontal_xmas, verticle_xmas])

def get_diagnals(matrix):
    n_row = len(matrix)
    n_col = len(matrix[0])
    count = 0
    for i in range(0, n_row):

        # create palidrome of pairs and the reverse
        diag = list(range(0, i+1))

        top_left = [ [x, y] for x, y in zip(diag, diag[::-1])]
        bottom_right = [[n_col-e[0]-1, n_col- e[1]-1] for e in top_left]
        top_right_list2 = [n_col- x -1 for x in list(range(0, i+1))][::-1]
        top_right = [[x, y] for x, y in zip(list(range(0, i+1)),top_right_list2 )]
        bottom_left = [[x[1],x[0]] for x in top_right]

        if not i == n_row - 1:  
            top_left_string = "".join([matrix[x[0]][x[1]] for x in top_left])  
            top_right_string = "".join([matrix[x[0]][x[1]] for x in top_right])
            bottom_left_string = "".join([matrix[x[0]][x[1]] for x in bottom_left])
            bottom_right_string = "".join([matrix[x[0]][x[1]] for x in bottom_right])
            
        else:
            top_left_string = "".join([matrix[x[0]][x[1]] for x in top_left])  
            top_right_string = "".join([matrix[x[0]][x[1]] for x in top_right])
            bottom_left_string  = ""
            bottom_right_string = ""

        
        top_left_result = find_xmas_in_strings(top_left_string)
        top_right_result = find_xmas_in_strings(top_right_string)
        bottom_left_result = find_xmas_in_strings(bottom_left_string)
        bottom_right_result = find_xmas_in_strings(bottom_right_string)

        count += top_left_result
        count += top_right_result
        count += bottom_left_result
        count += bottom_right_result

    return count

def sliding_window(window, matrix):
    n_row = len(matrix)
    n_col = len(matrix[0])
    x_mas_number = 0
    for i in range(window, n_row + 1):
        rows = matrix[i-window:i]
        for j in range(window, n_col + 1):
            windows += 1
            box = [x[j-window:j]for x in rows]
            box_centre = box[1][1]
            if not box_centre =="A":
                continue
            
            # 00 11 22
            # 02 11 20
            list_range = list(range(window))
            top_right_to_bottom_left = "".join([box[x][y] for x,y in zip(list_range, list_range)])
            top_left_to_bottom_right = "".join([box[x][y] for x, y in zip(list_range, list_range[::-1])])

            x_mas = all([(top_right_to_bottom_left == "MAS" or top_right_to_bottom_left == "SAM"),
                    (top_left_to_bottom_right == "MAS" or top_left_to_bottom_right == "SAM")])
    
            if x_mas:
                
                x_mas_number += 1

    return x_mas_number

def main():
    with open(os.path.join("/Users/lf16/Documents/GitHub/AoC_files/files", "04_AoC_2024_input.txt")) as file:


        # top left
        # [[1,1], 
        #  [2,1], [1,2], 
        #  [1,3], [2,2], [3,1]]

        # Bottom Left
        # [[9, 0],
        # [8,0],[1,9],
        # [7,0],[1,8],[9,2]]
        
        # Top Right
        # [[0,9],
        #  [0,8],[1,9],
        #  [0,7],[1,8],[2,9]]

        # Bottom Right
        # [[10,10],
        #  [9,10],[10,9],
        #  [8,10],[9,9],[10,8]
        #  [7, 10],[8,9],[9,8], [10,7]]
        matrix = get_matrix(file)
        verticle_results = search_verticle_horizontal(matrix)
        horizontal_result = get_diagnals(matrix)
        part_1_result = sum([verticle_results, horizontal_result])
        print(f"Part 1 Result: {part_1_result}")

        part_2_result = sliding_window(3, matrix)
        print(f"Part2 Result: {part_2_result}")

        # Notes to find make algorithm
                # top left
        # [[1,1], 
        #  [2,1], [1,2], 
        #  [1,3], [2,2], [3,1]]

        # Bottom Left
        # [[9, 0],
        # [8,0],[1,9],
        # [7,0],[1,8],[9,2]]
        
        # Top Right
        # [[0,9],
        #  [0,8],[1,9],
        #  [0,7],[1,8],[2,9]]

        # Bottom Right
        # [[10,10],
        #  [9,10],[10,9],
        #  [8,10],[9,9],[10,8]
        #  [7, 10],[8,9],[9,8], [10,7]]
        
if __name__ == "__main__":
    main()

