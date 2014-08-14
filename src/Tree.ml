type pos = {x : float; y : int; offset : float}
(* type pos = {mutable x : float; mutable y : float} *)

type tree = Node of string * tree list * pos

module FloatMap = Util.FloatMap

let prefix_fold initial_stack f state =
  let rec bf_rec stack state =
    match stack with
    | [] -> state
    | h :: t ->
      let Node (name, sons, pos) = h in
      let new_state = f state (name, sons, pos) in
      bf_rec (sons @ t) new_state
  in
  bf_rec initial_stack state

let queue_of_tree tree =
  let state = (MyQueue.empty, FloatMap.empty, FloatMap.empty, 0) in
  let f = fun (q, nexts, offsets, depth) (name, sons, pos) ->
    match sons with
    | [] ->
      let y = depth in
      let x = Util.get_in_map nexts depth in
      let self_offset = (max (Util.get_in_map offsets depth)
                           ((Util.get_in_map nexts depth) -. x)) in
      let offsets' = FloatMap.add depth self_offset offsets in
      let nexts' = FloatMap.add depth (x +. 1.) nexts in
      let node = Node (name, [], {x = x; y = y; offset = self_offset }) in
      ((MyQueue.push q (node, 0)), nexts', offsets', depth)
    | _ ->
      let node = Node (name, [], {x = 0.; y = depth; offset = 0. }) in
      ((MyQueue.push q (node, List.length sons)), nexts, offsets, depth+1)
  in
  prefix_fold [tree] f state

let pos_tree_of_queue state =
  let rec aux stack (q, nexts, offsets, depth) =
    if q = MyQueue.empty then
      List.hd stack
    else
      begin
        let (node, nb_sons) ,q' = MyQueue.pop q in
        let Node (name, _, pos) = node in
        let depth = pos.y in
        if nb_sons = 0 then
          aux (node :: stack) (q', nexts, offsets, depth)
        else
          let sons, stack' = Util.npop nb_sons stack in
          let Node (_, _, pos_first) = List.hd sons in
          let Node (_, _, pos_last) = List.hd (List.rev sons) in
          let place = (pos_first.x +. pos_last.x ) /. (float_of_int nb_sons) in
          let self_offset =  (max (Util.get_in_map offsets depth)
                                ((Util.get_in_map nexts depth) -. place)) in
          let offsets' = FloatMap.add depth self_offset offsets in
          let x = place +. self_offset in
          let nexts' = FloatMap.add depth (x +. 1.) nexts in
          let node = Node (name, sons, {x = x; y = pos.y; offset = self_offset}) in
          aux (node :: stack') (q', nexts', offsets', depth)
      end
  in
  aux [] state

let first_pass tree =
  pos_tree_of_queue (queue_of_tree tree)

let offsum_queue_of_tree tree = 
  let state = (MyQueue.empty, 0, 0., 0.) in
  let f = fun (q, height, width, offsum) (name, sons, pos) ->
    let x = pos.x +. offsum in
    let offsum' = offsum +. pos.offset in
    let height' = pos.y in
    let width' = x in
    let node = Node (name, [], {x = x; y = pos.y; offset = pos.offset}) in
    ((MyQueue.push q (node, List.length sons)),
     (max height height'),
     (max width width'),
     offsum')
  in prefix_fold [tree] f state

let pos_tree_of_offsum_queue state =
  let rec aux stack q =
    if q = MyQueue.empty then
      List.hd stack
    else
      let (node, nb_sons) ,q' = MyQueue.pop q in
      let Node (name, _, pos) = node in
      if nb_sons = 0 then
        aux (node :: stack) q'
      else
        let sons, stack' = Util.npop nb_sons stack in
        let node = Node (name, sons, pos) in
        aux (node :: stack') q'
  in
  let (q, height, width, _) = state in
  (width, height, aux [] q)

let second_pass tree =
  pos_tree_of_offsum_queue (offsum_queue_of_tree tree)

let pos_tree_of_tree tree =
  second_pass (first_pass tree)

    
    
    
