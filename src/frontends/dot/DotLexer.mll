{
open DotParser
}

let ident = ['A'-'Z' 'a'-'z' '0'-'9']['_' 'A'-'Z' 'a'-'z' '0'-'9']*
let str = '"' ['a'-'z' 'A'-'Z' '0'-'9' '-' '_' '!' '.' ',' ';' ]* '"'
let equal = '='                                                                 
let lbracket = '['
let rbracket = ']'
let lbrace = '{'
let rbrace = '}'               
let comma = ','
let semicolon = ';'
let arrow = "->"
let space = [' ' '\t']*
let newline = ['\n' '\r']

rule token = parse
            | ident as s { match s with
                           | "digraph" -> DIGRAPH
                           | "label" -> LABEL
                           | _ -> IDENT s
                         }
            | str as s { let open String in
                         STR (sub s 1 ((length s) - 2))
                       }
            | equal { EQUAL }
            | lbracket { LBRACKET }
            | rbracket { RBRACKET }
            | lbrace { LBRACE }
            | rbrace { RBRACE }
            | comma { COMMA }
            | semicolon { SEMICOLON }
            | arrow { ARROW }
            | space { token lexbuf }
            | newline { token lexbuf }
            | eof { EOF }

{
}
