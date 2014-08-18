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

let stack_of_tree tree =
  let state = ([], FloatMap.empty, FloatMap.empty, 0) in
  let f = fun (stack, nexts, offsets, depth) (name, sons, pos) ->
    match sons with
    | [] ->
      begin
        let y = depth in
        let x = Util.get_in_map nexts depth in
        let self_offset = (max (Util.get_in_map offsets depth)
                             ((Util.get_in_map nexts depth) -. x)) in
        let offsets' = FloatMap.add depth self_offset offsets in
        let nexts' = FloatMap.add depth (x +. 1.) nexts in
        let node = Node (name, [], {x = x; y = y; offset = self_offset }) in
        
        (* let open Printf in *)
        (* printf "push in queue Leaf 0\n"; *)
        

        (* ((MyQueue.push q (node, 0)), nexts', offsets', depth) *)
        (((node, 0) :: stack), nexts', offsets', depth)
      end
    | _ ->
      begin
        let node = Node (name, [], {x = 0.; y = depth; offset = 0. }) in
        
        (* let open Printf in *)
        (* printf "push in queue Node %d\n" (List.length sons); *)
        
        (* ((MyQueue.push q (node, List.length sons)), nexts, offsets, depth+1) *)
        (((node, List.length sons) :: stack), nexts, offsets, depth+1)
      end
  in
  prefix_fold [tree] f state

let pos_tree_of_stack state =
  let rec aux q (stack, nexts, offsets, depth) =
    if stack = []  then
      let res, _ = MyQueue.pop q in
      res
    else
      begin
        let (node, nb_sons) = List.hd stack in

        (* let open Printf in *)
        (* printf "nb_sons : %d ; stack length : %d\n" nb_sons (List.length stack); *)

        let Node (name, _, pos) = node in
        let depth = pos.y in
        if nb_sons = 0 then
          aux (MyQueue.push q node) ((List.tl stack), nexts, offsets, depth)
          (* aux (node :: stack) (q', nexts, offsets, depth) *)
        else
          begin
            let sons, q' = MyQueue.npop q nb_sons in
            let Node (_, _, pos_first) = List.hd sons in
            let Node (_, _, pos_last) = List.hd (List.rev sons) in
            let place = (pos_first.x +. pos_last.x ) /. (float_of_int nb_sons) in
            let self_offset =  (max (Util.get_in_map offsets depth)
                                  ((Util.get_in_map nexts depth) -. place)) in
            let offsets' = FloatMap.add depth self_offset offsets in
            let x = place +. self_offset in
            let nexts' = FloatMap.add depth (x +. 1.) nexts in
            let node = Node (name, sons, {x = x; y = pos.y; offset = self_offset}) in
            aux (MyQueue.push q' node) ((List.tl stack), nexts', offsets', depth)
            (* aux (node :: stack') (q', nexts', offsets', depth) *)
          end
      end
  in
  aux MyQueue.empty state

let first_pass tree =
  pos_tree_of_stack (stack_of_tree tree)

let offsum_stack_of_tree tree = 
  let state = ([], 0, 0., 0.) in
  let f = fun (stack, height, width, offsum) (name, sons, pos) ->
    let x = pos.x +. offsum in
    let offsum' = offsum +. pos.offset in
    let height' = pos.y in
    let width' = x in
    let node = Node (name, [], {x = x; y = pos.y; offset = pos.offset}) in
    (((node, List.length sons) :: stack),
     (max height height'),
     (max width width'),
     offsum')
  in prefix_fold [tree] f state

let pos_tree_of_offsum_stack state =
  let rec aux q stack =
    if stack = [] then
      let res, _ = MyQueue.pop q in
      res
    else
      let (node, nb_sons) = List.hd stack in
      let Node (name, _, pos) = node in
      if nb_sons = 0 then
        aux (MyQueue.push q node) (List.tl stack)
      else
        let sons, q' = MyQueue.npop q nb_sons in
        let node = Node (name, sons, pos) in
        aux (MyQueue.push q' node) (List.tl stack)
  in
  let (stack, height, width, _) = state in
  (width, height, aux MyQueue.empty stack)

let second_pass tree =
  pos_tree_of_offsum_stack (offsum_stack_of_tree tree)

let pos_tree_of_tree tree =
  second_pass (first_pass tree)

    
    
    
