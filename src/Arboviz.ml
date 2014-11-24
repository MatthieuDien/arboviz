open Printf
open Options

open ArbFrontend
open DotFrontend

open SvgBackend
open DotBackend


let () =

  let version_str = "arboviz -1.42" in

  let usage = "Usage: arboviz <opt> <input tree>" in

  let banner = "
      ...:'....:'':...':......
    :''   ._   .  `.  \\   ,   '':
    ':  .   \" .|    \\  `>/   _.-':               ===       ===             A
   .:'  .`'.   `-.  '. /'  ,..  .:            ______      ______           R
  :'        `.    ` \\| \\./   ' :       |     /      \\____/      \\   ----   B
  :. ,,-'''''  \"-.   |   | ....:     -----  |      o /  \\ o      |         O
   '.      ..'''  `\\ :   |             |     \\______/    \\______/   ----   V
     ''''''''       \\'   |                                                 I
                     |  =|                                                 Z
                     |   |
                     |-  |
  "
  in

  Arg.parse [
    ("-version", Arg.Unit
      (fun () -> printf "%s\n%!" version_str ; exit 0),
     " : print version information");
    ("-verbose", Arg.Int
      (fun n ->
        if n < 0 then
          begin
            eprintf "Error: wrong verbosity level %d => must be positive\n...aborting\n%!" n ;
            exit 1;
          end
        else
          global_options.verbosity <- n),
     "<n> : set the verbosity level to <n>  (a positive integer)");
    ("-T", Arg.String
      (fun x ->
        if List.exists (fun a -> a = x)
          ["svg"; "dot"]
        then
          global_options.output_type <- x
        else
          begin
            eprintf "Error format %s not supported ... aborting\n%!" x;
            exit 1
          end),
     "[svg, dot] : output format");
    ("-o", Arg.String
      (fun x -> global_options.output_name <- x),
     "<name> : name of the output file");
    ("-w", Arg.Float
      (fun x ->
        if x <= 0. then
          begin
            eprintf "Please, don't do stupid things";
            exit 1
          end
        else
          global_options.width_ratio <- x),
     "<float> : set the width ratio multiplier");
    ("-h", Arg.Float
      (fun x ->
        if x <= 0. then
          begin
            eprintf "Please, don't do stupid things";
            exit 1
          end
        else
          global_options.height_ratio <- x),
     "<float> : set the height ratio multiplier");
    ("-s", Arg.Unit
      (fun () -> global_options.show_label <- true ),
     " : show label")
  ]
    (fun arg -> global_options.input_name <- arg)
    usage;

  if (global_options.verbosity) > 0 then
    printf "%s\n%!" banner;

  let in_ext =
    if global_options.input_name = "" then
      "arb"
    else
      Util.get_ext global_options.input_name
  in

  let out_ext = global_options.output_type in

  if not (List.exists (fun a -> a = in_ext) ["arb"; "dot"]) then
    begin
      eprintf "Error : not supported input file format ... aborting \n%!";
      exit 1
    end;
  
  let ifd =
    if global_options.input_name = "" then
      stdin
    else
      open_in global_options.input_name
  in
  let ofd = open_out (global_options.output_name ^ "." ^
                        global_options.output_type) in
  
  let t =
    match in_ext with
    | "arb" -> ArbFrontend.parse ifd
    | "dot" -> DotFrontend.parse ifd                                 
    | _ -> assert false
  in

  let width, height, t' = Tree.pos_tree_of_tree t in

  let write =
    match out_ext with
    | "svg" -> SvgBackend.write 
    | "dot" -> DotBackend.write
    | _ -> assert false
  in
  
  write ofd t' width height 
    global_options.width_ratio
    global_options.height_ratio
    global_options.show_label;

  exit 0
