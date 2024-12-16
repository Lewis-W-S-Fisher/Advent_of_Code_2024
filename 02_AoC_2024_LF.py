import os
from collections import Counter

def find_level_distances(level_list, distance):
    '''
    Description: Returns True if the difference between neighbouring indices <= distance. must all be increasing or decreasing
    return: Bool
    '''
    difference_list = []
    increasing = []
    for i in range(1, len(level_list)):
        difference = level_list[i-1] - level_list[i]
        increasing.append(difference)
        difference_list.append((abs(difference) < distance))

    # check is all differences are either increasing or decresing. Return True if all are +ve or all are -ve
    increase_bool = [x > 0 for x in increasing]
    decrease_bool = [x < 0 for x in increasing]
    check1 = None
    if all(increase_bool) or all(decrease_bool):
        check1 = (all(increase_bool) or all(decrease_bool))
        
    # print(f"{increase_bool}\n{decrease_bool}\n{difference_list}")
    check2 = all(difference_list)
    return all([check1, check2])

def main():
    distance = 4
    # with open(os.path.join("files", "02_AoC_2024_input.txt")) as in_file:
    with open(os.path.join("files", "02_AoC_2024_input.txt")) as in_file:

        safety_levels = [list(map(int, x.strip().split(" "))) for x in in_file.readlines()]
        safe_reports = 0
        safe_reports_pt2 = 0
        # part 1
        for level_list in safety_levels:
            # print(level_list)
            safety_status = find_level_distances(level_list, distance)
            if safety_status:
                safe_reports += 1
                safe_reports_pt2 += 1
            else:
                # part 2
                # Removing a single index at at time and itertively check for "unsafeness"
                safety_status_list = []
                # print(level_list)
                for i in range(0, len(level_list)):
                    new_list = level_list[:i] + level_list[i+1:]
                    part1 = find_level_distances(new_list, distance)
                    safety_status_list.append(part1)
                    # print(new_list, part1)
                safety_counts = Counter(safety_status_list)
                # print(safety_counts, "\n")

                if True in safety_counts.keys():
                    safe_reports_pt2 += 1

    print(f"Safe Reports: {safe_reports}\nSafe Reports pt2: {safe_reports_pt2}")



if  __name__ == "__main__":
    # distance = 3
    # level_list = [1, 3, 5, 2] # Unsafe fails both
    # level_list = [1, 2, 2, 3, 4, 2] # unsafe fails all either increase/decrease
    # level_list = [1, 2, 3, 5, 6] # safe all increasing < 3
    # level_list = [6, 4, 3, 2, 1] # safe all decreasing < 3
    # level_list = [6, 4, 3, 3, 1] # one bad 
    # level_list = [4, 4, 3, 3, 1] # two bad

    # part 2 expectations
    # level_list = [7, 6, 4, 2, 1] # safe
    # level_list = [1, 2, 7, 8, 9] # unsafe
    # level_list = [9, 7, 6, 2, 1] # unsafe
    # level_list = [1, 3, 2, 4, 5] # safe
    # level_list = [8, 6, 4, 4, 1] # safe
    # level_list = [1, 3, 6, 7, 9] # safe

    # part1, part2  = find_level_distances(level_list, distance)
    # print(part2)

    main()