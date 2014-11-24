%{
open Tree
open UtilFrontend
open Hashtbl

let get_lbl = function
  | Some s -> s
  | None -> ""
      
let tbl = Hashtbl.create 100000

let add_arrow_tbl k v =
  if Hashtbl.mem tbl k then
    let lbl, sons = Hashtbl.find tbl k in
    Hashtbl.replace tbl k (lbl, v :: sons)
  else
    Hashtbl.add tbl k ("", [v])

let add_node_tbl k lbl =
  if Hashtbl.mem tbl k then
    let lbl, sons = Hashtbl.find tbl k in
    Hashtbl.replace tbl k (lbl, sons)
  else
    Hashtbl.add tbl k (lbl, [])
  
module StringSet = Set.Make(
                       struct
                         type t = string
                         let compare = compare
                       end)

let npop n l =
  let rec aux n l acc =
    if n = 0 then
      (l, acc)
    else
      aux (n-1) (List.tl l) ((List.hd l) :: acc)
  in
  aux n l []
                           
let make_tree nodes sons =
  let roots_ids = StringSet.elements (StringSet.diff nodes sons) in
  if (List.length roots_ids) != 1 then
    failwith "This is not a tree !"
  else
    begin
      let root_id = List.hd roots_ids in
      let root = Hashtbl.find tbl root_id in
      let lbl, sons = root in
      let tree_list = ref [(lbl, List.length sons)] in
      let sons_ids = ref sons in
      while !sons_ids != [] do
        let son_id = List.hd !sons_ids in
        let son = Hashtbl.find tbl son_id in
        let lbl, sons_son = son in
        tree_list := (lbl, List.length sons_son) :: !tree_list;
        sons_ids := sons_son @ (List.tl !sons_ids)
      done;

      let to_build = ref [] in
      while !tree_list != [] do
        let (lbl, arity) = List.hd !tree_list in
        let new_builds, sons = npop arity !to_build in
        to_build := (make_node lbl sons) :: new_builds;
        tree_list := List.tl !tree_list
      done;

      List.hd !to_build
    end
      
      
      
                           
%}
 
%token <string> IDENT STR

%token DIGRAPH LABEL
%token EQUAL COMMA SEMICOLON RBRACKET LBRACKET RBRACE LBRACE ARROW EOF

%start start
%type <Tree.t> start

%%

start:
    | DIGRAPH IDENT LBRACE graph RBRACE EOF{
                let nodes, sons = $4 in
                make_tree nodes sons
              }
    | DIGRAPH LBRACE graph RBRACE EOF{
                let nodes, sons = $3 in
                make_tree nodes sons
              }

graph:
    | DIGRAPH attrs graph { $3 }
    | node_decl { let n = $1 in
                  ((StringSet.add n StringSet.empty), StringSet.empty)
                }
    | arrow_decl { let p,s = $1 in
                   ((StringSet.add s (StringSet.add p StringSet.empty)),
                    (StringSet.add s StringSet.empty))
                 }
    | node_decl graph { let n = $1 in
                        let nodes, sons = $2 in
                        ((StringSet.add n nodes), sons)
                       }
    | arrow_decl graph { let p,s = $1 in
                         let nodes, sons = $2 in
                         ((StringSet.add s (StringSet.add p nodes)),
                          (StringSet.add s sons))
                       }

node_decl:
    | IDENT SEMICOLON { add_node_tbl $1 ""; $1 }
    | IDENT attrs SEMICOLON { add_node_tbl $1 $2; $1 }
    | IDENT { add_node_tbl $1 ""; $1 }
    | IDENT attrs { add_node_tbl $1 $2; $1 }


arrow_decl:
    | IDENT ARROW IDENT SEMICOLON { add_arrow_tbl $1 $3; ($1, $3) }
    | IDENT ARROW IDENT attrs SEMICOLON { add_arrow_tbl $1 $3; ($1, $3) }
            
attrs:
    | LBRACKET attr_list RBRACKET {
                 try
                   List.find (fun x -> if x = "" then false else true) (List.map get_lbl $2)
                 with
                   Not_found -> ""
               }

attr_list:
    | attr { [$1] }
    | attr attr_list { $1 :: $2 }
    | attr COMMA attr_list { $1 :: $3}
    | attr SEMICOLON attr_list { $1 :: $3 }

attr:
    | LABEL EQUAL STR { Some $3 }
    | IDENT EQUAL STR { None }
    | IDENT EQUAL IDENT { None }
