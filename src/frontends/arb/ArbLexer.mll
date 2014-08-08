{
open ArbParser
}

let ident = ['A'-'Z' 'a'-'z']['-' '_' 'A'-'Z' 'a'-'z' '0'-'9']*
let lbracket = '['
let rbracket = ']'
let comma = ','

rule token = parse
| ident as s { IDENT (s) }
| lbracket { LBRACKET }
| rbracket { RBRACKET }
| comma { COMMA }
| eof { EOF }

{
}
