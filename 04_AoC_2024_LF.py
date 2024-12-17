import os

with open(os.path.join("files", "04_AoC_2024_test.txt")) as file:
    file = [x.strip() for x in file.readlines()]
    print(len(file), len(file[0]))
    window = 4
    n_col = len(file[0])
    n_row = len(file)
    search_strings = {"XMAS", "SAMX"}
    xmas_count = 0
    # find string rows and columns
    # [[1,1], 
    #  [2,1], [1,2], 
    #  [1,3], [2,2], [3,1]]

    # [[1,10],
    #  [1,9],[2,10],
    #  [1,8],[2,9],[3,10]]

    # [[10,10],
    #  [9,10],[10,9],
    #  [8,10],[9,9],[10,8]]
    for i in range(0, n_row):
        row = file[i]
        col = "".join([x[i] for x in file])
        # create palidrome of pairs and the reverse
        diag = list(range(0, i+1))
        # diag_rev = diag[::-1]
        diag_rev = list(range(0, i+1))

        diag1 = [[x, y] for x, y in zip(diag, diag_rev)]
        diag2 = [[x, y] for x, y in zip(diag_rev, diag)]
        diag1_string = "".join([file[x[0]][x[1]] for x in diag1])
        diag2_string = "".join([file[x[0]][x[1]] for x in diag2])
        print(diag1)
        print(diag2)
        # print(diag1_string)
        # print(diag2_string)
        # print(row)

        # print(diag1_string, "\n")
        # print(len(diag1_string), len(diag2_string))
        # print(diag1, "\n")
        for j in range(window, n_row):
            if row[j-window:j] in search_strings:
                xmas_count += 1 
            if col[j-window:j] in search_strings:
                xmas_count += 1
            if len(diag1_string) < window:
                # print(diag1_string)
                continue
            # if len(diag1_string) > j:
            #     print(len(diag1_string), j)
            #     continue
            if diag1_string[j-window:j] in search_strings:
                xmas_count += 1
            if diag2_string[j-window:j] in search_strings:
                xmas_count += 1

    print(xmas_count)




