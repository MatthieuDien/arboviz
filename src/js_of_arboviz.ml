

open ArbFrontend
open DotFrontend









let onload _ =
  let open Dom_html in
  let area = createTextarea document in
  let compute_button = createButton document in
  Dom.appendChild document##body area;
  area##rows <- 80;
  area##cols <- 80;
  Dom.appendChild document##body compute_button;
  compute_button##onclick <- handler (fun _ ->
      let _ = Firebug.console##log (Js.string "lol") in
      let _ = Firebug.console##log (area##text) in
      Js._true
    );
  compute_button##innerHTML <- Js.string"Compute";
  Js._false





let _ = Dom_html.window##onload <- Dom_html.handler onload
