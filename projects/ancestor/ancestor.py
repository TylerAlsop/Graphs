

def earliest_ancestor(ancestors, starting_node):
    ancestors_dict = {}

    for item in ancestors:
        item_key = item[0]
        item_value = item[1]
        if item_key not in ancestors_dict:
            ancestors_dict[item_key] = set()
        ancestors_dict[item_key].add(item_value)

    print(f'Ancestors Dictionary: {ancestors_dict}')

    all_children = ancestors_dict.values()

    print(f'All Children: {all_children}')
    
    for child in all_children:
        if starting_node not in child:
            return -1
        # else:




test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)