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
