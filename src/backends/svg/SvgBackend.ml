open Backend
open Printf
open Tree

module SvgBackend : Backend =
struct
  let name = "Svg Backend"

    (* show label useless for the moment *)
  let write outchan tree width height width_unit height_unit show_label =
    let f () = fun (name, sons, pos) ->
      List.iter
        (fun (Node (_, _, pos')) ->
          let s = sprintf
            "<line x1=\"%f\" y1=\"%f\" x2=\"%f\" y2=\"%f\" style=\"stroke:rgb(0,0,0);stroke-width:0.1;stroke-linecap:round\" />\n"
            (pos.x *. width_unit)
            ((float_of_int pos.y) *. height_unit)
            (pos'.x *. width_unit)
            ((float_of_int pos'.y) *. height_unit)
          in
          output_string outchan s)
        sons
    in
    output_string outchan "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n";
    output_string outchan ("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\" width =\"" ^ (string_of_float width) ^ "\" height=\"" ^ (string_of_int height) ^ "\" >\n");
    Tree.prefix_fold [tree] f ();
    output_string outchan "</svg>\n";
    close_out outchan
      
end
  
  
