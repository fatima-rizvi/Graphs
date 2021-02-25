from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # first, instantiate the graph
    lineage = Graph()

    for parent in ancestors:
        # We're going to create the graph
        if parent[0] not in lineage:        # if parent is not in lineage, add them to lineage
            lineage.add_vertex(parent[0])

        if parent[1] not in lineage:
            lineage.add_vertex(parent[1])

    paths = lineage.dft_recursive(starting_node) # This finds all of the paths that lead to our node, with our node being first and the possible ancestor being last (look at method code)

    # This is kinda messy, but basically the max length of the path will be the length of the longest path in our list comp if the length of paths is greater than 0
    max_len_path = max([len(path) for path in paths]) if len(paths) > 0 else 0  # Kinda like a ternery statement. If it returns 0, we'll eventually return -1.

    possible = []

    for path in paths:
        if len(path) == max_len_path:
            possible.append(path) # If the length of any of these paths leading to our vertex is as long as the max possible length, append to the list of possible paths.

    if len(possible) == 1:      #only one path is the longest
        return possible[0][-1] # Return the path and grab the very first item (the full path) and the last line on it (the ancestor)

    elif len(possible) > 1:
        current_ancestor = possible[0][-1]
        
        for path in possible:
            if path[-1] < current_ancestor: # This is checking to see which ancestor has the lowest numeric id, liek teh README asks
                current_ancestor = path[-1]

        return current_ancestor

    return -1
