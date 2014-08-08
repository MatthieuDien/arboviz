open Tree

let make_node name childs = Node (name, childs, {x = 0.; y = 0.})

let make_leaf name = Leaf (name, {x = 0.; y = 0.})
