open ArbFrontend
open DotBackend
open SvgBackend


let () =
  let ifd = open_in "tree2.arb" in
  let ofd = open_out "tree2.svg" in

  let t = ArbFrontend.parse ifd in
  let (_, _, t') = Tree.pos_tree_of_tree t in
  (* let t' = Tree.pos_tree_of_tree t in *)
  SvgBackend.write ofd t' 20. 20. true
