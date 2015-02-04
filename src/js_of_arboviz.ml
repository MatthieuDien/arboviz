

open ArbFrontend
open DotFrontend

let error f = Printf.ksprintf (fun s -> Firebug.console##error (Js.string s); failwith s) f
let debug f = Printf.ksprintf (fun s -> Firebug.console##log(Js.string s)) f
let alert f = Printf.ksprintf (fun s -> Dom_html.window##alert(Js.string s); failwith s) f

let (@>) s coerce = Js.Opt.get (coerce @@ Dom_html.getElementById s) (fun () -> error "can't find element %s" s)


let fact = 1.

let parse_and_draw area canvas _ =
  let t = ArbFrontend.parse_from_string (Js.to_string area##value) in
  let width, height, t = Tree.pos_tree_of_tree t in
  canvas##height <- height * (1 + (int_of_float fact));
  canvas##width <- int_of_float @@ width *. fact;
  let ctx = canvas##getContext (Dom_html._2d_) in
  (* ctx##beginPath(); *)
  (* ctx##moveTo(10., 10.); *)
  (* ctx##lineTo(30.,30.); *)
  (* ctx##closePath(); *)
  debug "%d %f" height width;
  let open Tree in
  let rec draw father_pos (Node (s, childrens, pos)) =
    ctx##beginPath();
    ctx##moveTo(fact *. pos.x, fact *. float_of_int pos.y);
    begin match father_pos with
        None -> () | Some p -> ctx##lineTo(fact *. p.x, fact *. float_of_int p.y);
    end;
    ctx##stroke();
    ctx##closePath();
    List.iter (draw (Some pos)) childrens
  in
  draw None t;
  Js._true


let _ =
  let open Dom_html in
  window##onload <- handler (fun _ ->
      let area = "tarea" @> CoerceTo.textarea in
      let compute_btn = "compute_button" @> CoerceTo.button in
      let c = "canvas" @> CoerceTo.canvas in
      compute_btn##onclick <- (handler @@ parse_and_draw area c);
      Js._false
    )
