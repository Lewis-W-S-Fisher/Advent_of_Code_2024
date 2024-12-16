import os
import re

test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open(os.path.join("files", "03_AoC_2024_input.txt"), "r") as file:
    file = "".join([x.strip() for x in file.readlines()])
    running_count2 = 0
    pattern1 = r"mul(\(\d{1,},\d{1,}\))"
    x = re.findall(pattern1, file)
    x = [i.rstrip("\)").lstrip("(").split(",") for i in x]
    x = [int(i[0])*int(i[1]) for i in x]
    part1_count = sum(x)
    # 174960292
    # Part 2
    pattern2 = r"don't\(\).*?do\(\)"
    z = re.sub(pattern2, "", file)
    pattern3 = r"don't\(\)"
    pattern4 = r"do\(\)"
    first_dont = re.search(r"don't\(\)", z)
    all_donts = [i for i in re.finditer(pattern3, z)]
    all_dos = [i for i in re.finditer(pattern4, z)]

    if all_donts:
        dont_start = all_donts[0].start(0)
        z = z[0:dont_start]
    else:
        pass

    z = re.findall(pattern1, z)
    
    z = [i.rstrip("\)").lstrip("(").split(",") for i in z]
    z = [int(i[0])*int(i[1]) for i in z]
    part2_count = sum(z)
    # 56275602
    print(f"Part 1: {part1_count}\nPart 2: {part2_count}")

# test
# pattern2 = r"don't\(\).*do\(\)?"
# test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
# y = re.findall(pattern2, test_string)
# # This toy example works too
# z = re.sub(pattern2, "", test_string)
# z = re.findall(pattern1, z)
# z = [i.rstrip("\)").lstrip("(").split(",") for i in z]
# z = [int(i[0])*int(i[1]) for i in z]
