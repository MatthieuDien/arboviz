module FloatMap = Map.Make(struct type t = int let compare = compare end)

let get_in_map map x =
  if FloatMap.mem x map then
    FloatMap.find x map
  else
    0.


let npop n l =
  let rec npop_rec n l acc =
    if n = 0 then
      (acc,l)
    else
      npop_rec (n-1) (List.tl l) ((List.hd l) :: acc)
  in
  let pops, l' = npop_rec n l [] in
  (List.rev pops), l'
