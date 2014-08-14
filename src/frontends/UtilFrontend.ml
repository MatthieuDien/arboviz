open Tree

let make_node name childs = Node (name, childs, {x = 0.; y = 0; offset = 0.})

let make_leaf name = Node (name, [], {x = 0.; y = 0; offset = 0.})
