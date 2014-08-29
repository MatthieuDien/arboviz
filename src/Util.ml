open Printf


(* Float Map Utilities *)
module FloatMap = Map.Make(struct type t = int let compare = compare end)

let get_in_map map x =
  if FloatMap.mem x map then
    FloatMap.find x map
  else
    0.

(* List Utilities *)

let rec npop n l =
  if n = 0 then
    ([],l)
  else
    let x,l' = npop (n-1) (List.tl l) in
    ((List.hd l) :: x), l'

(* String Utilities *)
let get_ext s =
  try
    let dot_pos = 1 + (String.rindex s '.') in
    String.sub s dot_pos ((String.length s) - dot_pos)
  with
  | _ -> 
    begin
      eprintf "Error : can not find the input file format\n%!";
      exit 1
    end
