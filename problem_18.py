triangle_string = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
""".strip()

triangle = []
for line in triangle_string.splitlines():
    triangle.append([int(i) for i in line.split()])

# recursive method that taking as input:
# tree: the whole tree
# cur_node: 2d coordinates representing level of tree and position of cur_node in level
# cur_path_len: length of path from global root of tree to cur_node
#
# returns the maximum path length from root to leaf
#
def greedy_max_path(tree, cur_node, cur_path_len):
    cur_node_level = cur_node[0]
    cur_node_pos = cur_node[1]
    cur_node_val = tree[cur_node_level][cur_node_pos]

    # cur_node is not a leaf node
    if (cur_node_level < len(tree)-1):
        children = [[cur_node_level+1, cur_node_pos], [cur_node_level+1, cur_node_pos+1]]
        new_path_len = cur_path_len + cur_node_val
        return max(greedy_max_path(tree, children[0], new_path_len), greedy_max_path(tree, children[1], new_path_len))
    # cur_node is a leaf node
    else:
        return cur_path_len + cur_node_val

print(greedy_max_path(triangle, [0,0], 0))
