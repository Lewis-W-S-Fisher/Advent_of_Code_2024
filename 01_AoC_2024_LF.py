import os
from collections import Counter

# Part 1 
with open(os.path.join("files", "01_AoC_2024_input.txt"), "r") as in_file:
    list0 = []
    list1 = []
    for line in in_file.readlines():
        # ensure type is int, text file delimited by three spaces
        if line:
            # line = line.strip().split("   ")
            # assert(len(line) == 2)
            l0, l1 = list(map(int, line.strip().split("   ")))
            list0.append(l0)
            list1.append(l1)

    list0.sort()
    list1.sort()

    diff_list = [abs(l0 - l1) for l0, l1 in zip(list0, list1)]
    total_difference = sum(diff_list)
    print(f"Total Difference: {total_difference}")

    # Part 2 
    # create dictionary of counts
    l1_counts = Counter(list1)
    # fine all l0 in l1 and calculate similarity score
    similarities = [l0 * l1_counts[l0] for l0 in list0 if l0 in set(l1_counts.keys())]
    similarity_score = sum(similarities)
    print(f"Similarity Score: {similarity_score}")


