{
open ArbParser
}

let ident = ['A'-'Z' 'a'-'z']['-' '_' 'A'-'Z' 'a'-'z' '0'-'9']*
let lbracket = '['
let rbracket = ']'
let comma = ','
let space = [' ' '\t']*
let newline = ['\n' '\r']

rule token = parse
| ident as s { IDENT (s) }
| lbracket { LBRACKET }
| rbracket { RBRACKET }
| comma { COMMA }
| space { token lexbuf }
| newline { token lexbuf }
| eof { EOF }

{
}
