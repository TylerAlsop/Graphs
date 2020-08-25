
def earliest_ancestor(ancestors, starting_node):

    ancestors_dict = {}

    for item in ancestors:
        if item[1] in ancestors_dict:
            ancestors_dict[item[1]].append(item[0])
 
        else:
            ancestors_dict[item[1]] = [item[0]]
    
    if starting_node not in ancestors_dict:
        return -1
    
    curr_parents = ancestors_dict[starting_node]
        
    while True:
        new_parents = []
        
        for parent in curr_parents:
            if parent in ancestors_dict:
                new_parents = new_parents + ancestors_dict[parent]

            if len(new_parents) == 0:
                return curr_parents[0]

            else:
                
                curr_parents = new_parents
                
    print(ancestors_dict)



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 1)