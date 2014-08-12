type pos = {mutable x : float; mutable y : float; mutable offset : float}

type tree = Leaf of string * pos | Node of string * tree list * pos

module IntMap = Map.make (int)

let get_in_map map x =
  if IntMap.mem x map then
    IntMap.find x map
  else
    0

let rec first_pass t nexts offset depth k =
  match t with
  | Leaf (name, pos) ->
    begin
      pos.y <- depth;
      let place = get_in_map nexts depth in
      pos.x <- place;
      pos.offset <- (max (get_in_map offset depth)
                       ((get_in_map nexts depth) -. place));
      let nexts' = IntMap.add depth (pos.x+1) nexts in
      let offset' = IntMap.add depth pos.offset offset in
      k t
    end
  | Node (name, childs, pos) ->
    begin
      pos.y <- depth;
      let k' = fun x ->
