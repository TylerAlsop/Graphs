
def earliest_ancestor(ancestors, starting_node):
    ancestors_dict = {}
    stack = []

    stack.append(starting_node)

    current_parents = []

    for item in ancestors:
        item_key = item[0]
        item_value = item[1]
        if item_key not in ancestors_dict:
            ancestors_dict[item_key] = set()
        ancestors_dict[item_key].add(item_value)

    print(f'Ancestors Dictionary: {ancestors_dict}')

    # all_children = ancestors_dict.values()

    # print(f'All Children: {all_children}')
    
    while len(stack) > 0:
        current_node = stack.pop()

        if current_node not in ancestors_dict.values():
            return -1
        else:
            search_person = input(current_node)
            for parent, children in ancestors_dict.items():
                if children == search_person:
                    current_parents.append(parent)
                    print(f'Current Parents: {current_parents}')




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)