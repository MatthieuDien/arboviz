module MyQueue =
  struct
    type 'a t = { pushlist : 'a list; poplist : 'a list }

    let create () = { pushlist = []; poplist = [] }

    let rec pop q =
      match q.poplist with
      | [] -> pop { pushlist = []; poplist = List.rev q.pushlist }
      | x :: xs -> (x, { pushlist = q.pushlist; poplist = xs })

    let push q x =
      {pushlist = x :: q.pushlist; poplist = q.poplist }
  end

let rec fill n q =
  if n = 0 then q else fill (n-1) (MyQueue.push q n)

let rec unfill n q =
  if n = 0 then q else let (_,q') = MyQueue.pop q in unfill (n-1) q'

let _ = 
  let myqueue = MyQueue.create () in
  ignore (fill 1000000 myqueue |> unfill 500000  |> fill 1000000 |> unfill 150000)

