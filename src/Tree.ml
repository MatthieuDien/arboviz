type pos = {x : float; y : int; offset : float}
(* type pos = {mutable x : float; mutable y : float} *)

type t = Node of string * t list * pos

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

let stack_of_queues_of_tree tree =
  let rec traversal to_visit current_level stack nexts offsets =
    match to_visit with
    | [] -> (current_level :: stack), nexts, offsets (* rappeler sur current_level ? *)
    |  (Node (name, sons, pos), depth) :: t ->
      begin
        match sons with
        | [] ->
          begin
            let y = depth in
            let x = Util.get_in_map nexts depth in
            let self_offset = (max (Util.get_in_map offsets depth)
                                 ((Util.get_in_map nexts depth) -. x)) in
            let offsets' = FloatMap.add depth self_offset offsets in
            let nexts' = FloatMap.add depth (x +. 1.) nexts in

            let open Printf in
            (* printf "name %s x %f y %d \n" name x y; *)

            let node = Node (name, [], {x = x; y = y; offset = self_offset }) in
            
            traversal t current_level stack nexts' offsets'
          end


let stack_of_tree tree =
  let rec traversal to_visit visited nexts offsets =
    
    (* let open Printf in *)
    (* printf "get_in_map nexts 1 %f\n" (Util.get_in_map nexts 1); *)

    match to_visit with
    | [] -> visited, nexts, offsets
    | (Node (name, sons, pos), depth) :: t ->
      begin

        let open Printf in
        printf "ici name %s\n" name;

        match sons with
        | [] ->
          begin
            let y = depth in
            let x = Util.get_in_map nexts depth in
            let self_offset = (max (Util.get_in_map offsets depth)
                                 ((Util.get_in_map nexts depth) -. x)) in
            let offsets' = FloatMap.add depth self_offset offsets in
            let nexts' = FloatMap.add depth (x +. 1.) nexts in

            let open Printf in
            (* printf "name %s x %f y %d \n" name x y; *)

            let node = Node (name, [], {x = x; y = y; offset = self_offset }) in                  
            traversal t  ((node, 0) :: visited) nexts' offsets'
          end
        | _ ->
          begin
            let node = Node (name, [], {x = 0.; y = depth; offset = 0. }) in
            let sons_with_depth = List.map (fun x -> (x,(depth+1))) sons in
            traversal (sons_with_depth @ t) ((node, List.length sons) :: visited) nexts offsets
              (* TODO : supprimer list.rev et rendre le npop tail recursif *)
          end
      end
  in
  traversal [(tree, 0)] [] FloatMap.empty FloatMap.empty

let rec npop n l =
  if n = 0 then
    ([],l)
  else
    let x,l' = npop (n-1) (List.tl l) in
    ((List.hd l) :: x), l'

let pos_tree_of_stack state =
  let rec aux s (stack, nexts, offsets) =

    let open Printf in
    (* printf "get_in_map nexts 1 %f\n" (Util.get_in_map nexts 1); *)
    (* printf "get_in_map offsets 1 %f\n" (Util.get_in_map offsets 1); *)

    match stack with
    | [] -> List.hd s
    | h :: t ->
      begin
        let (node, nb_sons) = h in
        let Node (name, _, pos) = node in

        let open Printf in
        printf "aqui name %s \n" name;

        let depth = pos.y in
        if nb_sons = 0 then
          aux (node :: s) (t, nexts, offsets)
        else
          begin
            let sons, s' = npop nb_sons s in
            let Node (_, _, pos_first) = List.hd sons in
            let Node (_, _, pos_last) = List.hd (List.rev sons) in
            let place = (pos_first.x +. pos_last.x ) /. 2. in
            (* printf "place %f\n" place; *)
            let self_offset =  (max (Util.get_in_map offsets depth)
                                  ((Util.get_in_map nexts depth) -. place)) in
            (* printf "self_offset %f \n" self_offset; *)
            let offsets' = FloatMap.add depth self_offset offsets in
            let x = place +. self_offset in
            (* printf "x %f \n" x; *)
            let nexts' = FloatMap.add depth (x +. 1.) nexts in
            let node = Node (name, sons, {x = x; y = depth; offset = self_offset}) in
            aux (node :: s') (t, nexts', offsets')
          end
      end
  in
  aux [] state

let first_pass tree =
  pos_tree_of_stack (stack_of_tree tree)


let offsum_stack_of_tree tree =
  let rec traversal to_visit visited height width =
    match to_visit with
    | [] -> visited, height, width
    | (Node (name, sons, pos), offsum) :: t ->
      begin

        (* let open Printf in  *)
        (* printf "%s offsum %f\n" name offsum; *)

        let x = pos.x +. offsum in
        let offsum' = offsum +. pos.offset in
        let height' = max pos.y height in
        let width' = max x width in
        let node = Node (name, [], {x = x; y = pos.y; offset = pos.offset}) in
        let sons_with_offsum = List.map (fun x -> (x,offsum')) sons in
        traversal (sons_with_offsum @ t) ((node, List.length sons) :: visited) height' width'
      (* TODO : supprimer list.rev et rendre le npop tail recursif *)
      end
  in
  traversal [(tree, 0.)] [] 0 0.

let pos_tree_of_offsum_stack state =
  let rec aux s stack =
    match stack with
    | [] -> List.hd s
    | h :: t ->
      begin
        let (node, nb_sons) = h in
        let Node (name, _, pos) = node in
        
        (* let open Printf in *)
        (* printf "aqui2 name %s\n" name; *)
        
        if nb_sons = 0 then
          aux (node ::s) t
        else
          let sons, s' = npop nb_sons s in
          let node = Node (name, sons, pos) in
          aux (node :: s') t
      end
  in
  let (stack, height, width) = state in
  (width, height, aux [] stack)

let second_pass tree =
  pos_tree_of_offsum_stack (offsum_stack_of_tree tree)


let pos_tree_of_tree tree =
  second_pass (first_pass tree)

    
    
    
