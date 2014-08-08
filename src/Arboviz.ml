open ArbFrontend
open DotBackend


let () =
  let ifd = open_in "tree.arb" in
  let ofd = open_out "tree.dot" in
  
  let t = ArbFrontend.parse ifd in
  DotBackend.write ofd t 0. 0. true
