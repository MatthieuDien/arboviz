module FloatMap = Map.Make(struct type t = int let compare = compare end)

let get_in_map map x =
  if FloatMap.mem x map then
    FloatMap.find x map
  else
    0.

let rec npop n l =
  if n = 0 then
    ([],l)
  else
    let x,l' = npop (n-1) (List.tl l) in
    ((List.hd l) :: x), l'
