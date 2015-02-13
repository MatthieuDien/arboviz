open Frontend

module ArbFrontend : Frontend =
  struct
    let name = "Arb Frontend"

    let parse inchan =
      let lexbuf = Lexing.from_channel inchan in
      let res = ArbParser.start ArbLexer.token lexbuf in
      close_in inchan;
      res

    let parse_from_string s =
      let lexbuf = Lexing.from_string s in
      let res = ArbParser.start ArbLexer.token lexbuf in
      res

  end
