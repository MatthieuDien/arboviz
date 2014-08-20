%{
open Tree
open UtilFrontend
%}

%token <string> IDENT

%token COMMA RBRACKET LBRACKET EOF

%start start
%type <Tree.t> start

%%

start:
 | node EOF { $1 }

node:
 | IDENT LBRACKET node_list RBRACKET { make_node $1 $3 }
 | IDENT { make_leaf $1 }

node_list:
 | node { [$1] }
 | node COMMA node_list { $1 :: $3 }

