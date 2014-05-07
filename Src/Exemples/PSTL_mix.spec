
// grammar file for binary trees (counting leaves and internal nodes)
// with parameters to obtain trees of size about 100000

set min 100000;
set max 1000000;
set try 300000;

/*
BinNode ::=  Leaf + BinNode * BinNode*<z>;
*/

/*
UnBin ::= Leaf*<z> + UnBin*<z> + UnBin*UnBin*<z>;
*/

Quin ::= Leaf*<z> + Quin*<z> + Quin*Quin*<z> + Quin*Quin*Quin*<z>  + Quin*Quin*Quin*Quin*<z> + Quin*Quin*Quin*Quin*Quin*<z>;