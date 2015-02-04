open Frontend

module DotFrontend : Frontend =
  struct
    let name = "Dot Frontend"

    let parse inchan =
      let lexbuf = Lexing.from_channel inchan in
      let res = DotParser.start DotLexer.token lexbuf in
      close_in inchan;
      res

    let parse_from_string s =
      let lexbuf = Lexing.from_string s in
      let res = DotParser.start DotLexer.token lexbuf in
      res

  end
