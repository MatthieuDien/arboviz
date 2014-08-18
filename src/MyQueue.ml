type 'a t = { pushlist : 'a list; poplist : 'a list }

let empty =  { pushlist = []; poplist = [] }

exception Empty

let rec pop q =
  match q.poplist with
  | [] -> begin 
    try pop { pushlist = []; poplist = List.rev q.pushlist } 
    with  _ -> raise Empty
  end
  | x :: xs -> (x, { pushlist = q.pushlist; poplist = xs })

let push q x =
  {pushlist = x :: q.pushlist; poplist = q.poplist }

let rec npop q n =
  if n = 0 then
    [],q
  else
    let x, q' = pop q in
    let x', q'' = (npop q' (n-1)) in
    x :: x', q''
