open Backend
open Printf
open Tree

module DotBackend : Backend =
  struct
    let name = "Dot Backend"

    let string_of_pos _ height pos width_unit height_unit =
      sprintf "pos=\"%f,%f!\""
        (pos.x *. width_unit)
        (height -. (float_of_int pos.y) *. height_unit)

    let write_nodes outchan tree width height width_unit height_unit show_label =
      let current_id = 0 in
      let f =  fun current_id (name, _, pos) ->
       begin
         output_string outchan ((string_of_int current_id) ^ " [");
         (if show_label then
             output_string outchan ("label=\"" ^ name ^ "\" ")
          else
             output_string outchan ("shape=\"point\" "));
         output_string outchan ((string_of_pos width height pos width_unit height_unit) ^ "]\n");
         (* output_string outchan ("\n]\n"); *)
         current_id + 1
       end
      in
      ignore (Tree.prefix_fold [tree] f current_id)

    let write_edges outchan first_sons =
      let state = [(0, List.length first_sons)],1 in
      let f = fun (ids,cid) (name, childs, pos) ->
        match childs with
        | [] ->
          begin
            let (id,c) = List.hd ids in
            output_string outchan ((string_of_int id) ^ "->" ^ (string_of_int cid) ^ ";\n");
            if c = 1 then
              (List.tl ids), (cid+1)
            else
              ((id, c-1) :: (List.tl ids)), (cid+1)
          end
        | _ ->
          begin
            let (id,c) = List.hd ids in
            output_string outchan ((string_of_int id) ^ "->" ^ (string_of_int cid) ^ ";\n");
            if c = 1 then
              ((cid, List.length childs)::(List.tl ids)), (cid+1)
            else
              ((cid, List.length childs)::(id,c-1)::(List.tl ids)), (cid+1)
          end
      in
      ignore (Tree.prefix_fold first_sons f state)
      
    let write outchan tree width height width_unit height_unit show_label =
      output_string outchan "digraph G {\n";
      output_string outchan "graph [ordering=\"out\"]\n";
      write_nodes outchan tree width (float_of_int height) width_unit height_unit show_label;
      (match tree with
      | Node (_,[],_) -> ()
      | Node (_,childs,_) -> write_edges outchan childs);
      output_string outchan "}\n";
      close_out outchan

end
