open Frontend

module DotFrontend : Frontend =
  struct
    let name = "Dot Frontend"

    open DotLexer
    open Format
    open Lexing

    let print_loc fmt lb =
      let pos = lexeme_start_p lb in
      let c = (pos.pos_cnum - pos.pos_bol) in
      fprintf fmt "File \"%s\", line %d, characters %d-%d:" pos.pos_fname
        pos.pos_lnum c c

    let parse inchan =
      let lexbuf = Lexing.from_channel inchan in
      lexbuf.lex_curr_p <- { lexbuf.lex_curr_p with pos_fname = "stdin" };
      let res = match DotParser.start DotLexer.token lexbuf with
        | exception (Parsing.Parse_error) ->
          eprintf "%a@\nsyntax error@\n" print_loc lexbuf; exit 1
        | exception e -> eprintf "%s@\n" (Printexc.to_string e); exit 1
        | r -> r
      in
      close_in inchan;
      res

    let parse_from_string s =
      let lexbuf = Lexing.from_string s in
      let res = DotParser.start DotLexer.token lexbuf in
      res

  end
