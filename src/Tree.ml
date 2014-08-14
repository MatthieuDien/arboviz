(* type pos = {mutable x : float; mutable y : float; mutable offset : float} *)
type pos = {mutable x : float; mutable y : float}

type tree = Node of string * tree list * pos

(* module IntMap = Map.Make(struct type t = int let compare = compare end) *)

let prefix_fold initial_stack f state =
  let rec bf_rec stack state =
    match stack with
    | [] -> state
    | h :: t ->
      let Node (name, childs, pos) = h in
      let new_state = f state (name, childs, pos) in
      bf_rec (childs @ t) new_state
  in
  bf_rec initial_stack state
    
(* let get_in_map map x = *)
(*   if IntMap.mem x map then *)
(*     IntMap.find x map *)
(*   else *)
(*     0 *)

(* let get_queue tree = *)
(*   let state = (MyQueue.create (), 0) in *)
  

(* let rec first_pass t nexts offset depth k = *)
(*   match t with *)
(*   | Leaf (name, pos) -> *)
(*     begin *)
(*       pos.y <- depth; *)
(*       let place = get_in_map nexts depth in *)
(*       pos.x <- place; *)
(*       pos.offset <- (max (get_in_map offset depth) *)
(*                        ((get_in_map nexts depth) -. place)); *)
(*       let nexts' = IntMap.add depth (pos.x+1) nexts in *)
(*       let offset' = IntMap.add depth pos.offset offset in *)
(*       k t *)
(*     end *)
(*   | Node (name, childs, pos) -> *)
(*     begin *)
(*       let k' = fun x -> *)
(*         pos.y <- depth; *)


