import os

def part_input(file):
    page_instructions = []
    page_orders = []
    for line in file:
        if len(line.split("|")) == 2:
            page_instructions.append(line)
        elif line:
            page_orders.append(line)

    # print(page_instructions)
    # print(page_orders)
    return page_instructions, page_orders
def determine_correct_order():
    pass

def main():
    with open(os.path.join("/Users/lf16/Documents/GitHub/AoC_files/files", "05_AoC_2024_test.txt")) as file:
        file = [x.strip() for x in file.readlines()]
        page_instructions, page_orders = part_input(file)
        order_index_dict = {page:idx for idx, page in enumerate(page_orders)}
        # page_instructions_dict = {x.split("|")[0]:x.split("|")[1] for x in page_instructions}

        # print(len(page_orders), len(order_index_dict))
        for order in page_orders:
            order = list(map(int, order.split(",")))
            order_index_dict = {page:idx for idx, page in enumerate(order)}
            # print(order_index_dict)
            # print(order)
            order_len = len(order)
            for page in order:
                # print(page)
                for instruction in page_instructions:
                    # print(instruction)
                    # print(page)
                    instruction_list = list(map(int, instruction.split("|")))
                    page_before, page_after = instruction_list
                    # print(instruction_list)
                    # print(f"{page}\n{page_before}   {page_after}")
                    


                    if not page_before in order_index_dict or not page_after in order_index_dict:
                        continue
                    
                    if order_index_dict[page_before] > order_index_dict[page_after]:
                        continue


                    print(order_index_dict)
                    
                    print(f"{page}\n{page_before}  {page_after}")
                    # page_before_order = order_index_dict[page] 
                    # page_after_order = order_index_dict[page] 
                    # print(instruction)
                    # print(page_before_order, page_after_order)


if __name__ == "__main__":
    main()
