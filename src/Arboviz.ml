open ArbFrontend
open DotBackend


let () =
  let ifd = open_in "tree.arb" in
  let ofd = open_out "tree.dot" in
  
  let t = ArbFrontend.parse ifd in
  let (_, _, t') = Tree.pos_tree_of_tree t in
  DotBackend.write ofd t' 1. 1. true
