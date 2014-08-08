open Backend
open Printf
open Tree

module DotBackend : Backend =
  struct
    let name = "Dot Backend"

    let string_of_pos pos width_unit height_unit =
      sprintf "pos = \"%f,%f!\""
        (pos.x *. height_unit)
        (pos.y *. width_unit)

    let rec write_nodes outchan stack width_unit height_unit show_label id =
      match stack with
      | [] -> ()
      | h :: t ->
        begin
          match h with
          | Leaf (name, pos) ->
            begin
              output_string outchan ((string_of_int id) ^ " [\n");
              (if show_label then
                  output_string outchan ("label=\"" ^ name ^ "\""));
              (* output_string outchan ((string_of_pos pos width_unit height_unit) ^ "\n]\n"); *)
              output_string outchan ("\n]\n");
              write_nodes outchan t width_unit height_unit show_label (id+1)
            end
          | Node (name, childs, pos) -> 
            begin
              output_string outchan ((string_of_int id) ^ "[\n");
              (if show_label then
                  output_string outchan ("label=\"" ^ name ^ "\""));
              (* output_string outchan ((string_of_pos pos width_unit height_unit) ^ "\n]\n"); *)
              output_string outchan ("\n]\n");
              write_nodes outchan (childs @ t) width_unit height_unit show_label (id+1)
            end
        end

    let rec write_edges outchan stack ids cid =
      match stack with
      | [] -> ()
      | h :: t ->
        begin
          match h with
          | Leaf (name, pos) ->
            begin
              let (id,c) = List.hd ids in
              output_string outchan ((string_of_int id) ^ "--" ^ (string_of_int cid) ^ ";\n");
              if c = 1 then
                write_edges outchan t (List.tl ids) (cid+1)
              else
                write_edges outchan t ((id, c-1) :: (List.tl ids)) (cid+1)
            end
          | Node (name, childs, pos) -> 
            begin
              let (id,c) = List.hd ids in
              output_string outchan ((string_of_int id) ^ "--" ^ (string_of_int cid) ^ ";\n");
              if c = 1 then
                write_edges outchan (childs @ t) ((cid, List.length childs)::(List.tl ids)) (cid+1)
              else
                write_edges outchan (childs @ t) ((cid, List.length childs)::(id,c-1)::(List.tl ids)) (cid+1)
            end
        end
      

    let write outchan tree width_unit height_unit show_label =
      output_string outchan "graph G {\n";
      output_string outchan "graph [ordering=\"out\"]\n";
      write_nodes outchan [tree] width_unit height_unit show_label 0;
      (match tree with
      | Leaf _ -> ()
      | Node (_,childs,_) -> write_edges outchan childs [(0,List.length childs)] 1);
      output_string outchan "}\n";
      close_out outchan
              
end
